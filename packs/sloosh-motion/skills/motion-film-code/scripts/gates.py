#!/usr/bin/env python3
"""gates.py: the technical gates for a code-rendered film (motion-film-code).

  python3 <skill>/scripts/gates.py out/film_v2.mp4                          -> prints the gates; exit 1 if one fails
  python3 <skill>/scripts/gates.py out/film_v2_final.mp4 --master --json out/qa/gates.json --sheet out/qa/sheet.jpg
  python3 <skill>/scripts/gates.py out/film_v2_final.mp4 --poster 12.4 out/poster.jpg
  python3 <skill>/scripts/gates.py out/film_v2_final.mp4 --retag out/final.mp4      -> BT.709 tags + faststart, no re-encode

Gates (every render):
  decodes   ffprobe finds a video stream and ffmpeg decodes every frame with no error
  not blank no blank (one-colour) run longer than 0.5 s, and at most 10% of all frames blank
  moves     the picture changes: the mean frame difference before the end hold is at least --moves
  no flats  no run of more than 3 flat (unchanged) frames before the end hold; a blank breath is checked by not blank
  end hold  the still frames at the very end last 0.6 to 1.4 s
Master checks (with --master): H.264, yuv420p, BT.709 colour tags, and the moov atom before the media data (faststart).

It reads only the file it is given and writes only the files you name. It downloads and installs nothing.
It needs ffmpeg, ffprobe and numpy.
"""
import argparse, json, os, struct, subprocess, sys

import numpy as np

SIDE = 256                                   # frames are compared at 256 x 256 grey


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=codec_name,pix_fmt,width,height,r_frame_rate,color_space,color_primaries,color_transfer",
                          "-show_entries", "format=duration", "-of", "json", path], capture_output=True, text=True)
    if out.returncode != 0:
        return None
    data = json.loads(out.stdout or "{}")
    streams = data.get("streams") or []
    if not streams:
        return None
    s = streams[0]
    num, _, den = (s.get("r_frame_rate") or "0/1").partition("/")
    s["fps"] = float(num) / float(den or 1) if float(den or 1) else 0.0
    s["duration"] = float((data.get("format") or {}).get("duration") or 0.0)
    return s


def decode(path):
    """Stream the film at 256 x 256 grey; keep only per-frame numbers, never the whole film."""
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-map", "0:v:0", "-vf",
                          f"scale={SIDE}:{SIDE}:flags=area,format=gray", "-f", "rawvideo", "-"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    size, prev, diffs, stds = SIDE * SIDE, None, [], []
    while True:
        buf = p.stdout.read(size)
        if len(buf) < size:
            break
        cur = np.frombuffer(buf, np.uint8).astype(np.int16)
        stds.append(float(cur.std()))
        if prev is not None:
            diffs.append(float(np.abs(cur - prev).mean()))
        prev = cur
    err = p.stderr.read().decode(errors="replace").strip()
    code = p.wait()
    return np.array(diffs), np.array(stds), code, err


def runs(mask):
    """[start, length] of each run of True values."""
    out, start = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and start is None:
            start = i
        elif not v and start is not None:
            out.append([start, i - start]); start = None
    return out


def faststart(path):
    """True when the moov atom comes before the first mdat atom."""
    with open(path, "rb") as f:
        size_all = os.fstat(f.fileno()).st_size; pos = 0
        while pos + 8 <= size_all:
            f.seek(pos); size, kind = struct.unpack(">I4s", f.read(8)); head = 8
            if size == 1:
                size = struct.unpack(">Q", f.read(8))[0]; head = 16
            elif size == 0:
                size = size_all - pos
            if kind == b"moov":
                return True
            if kind == b"mdat":
                return False
            if size < head:
                return False
            pos += size
    return False


def main():
    ap = argparse.ArgumentParser(description="Technical gates for a rendered film.")
    ap.add_argument("video")
    ap.add_argument("--master", action="store_true", help="also check H.264, yuv420p, BT.709 and faststart")
    ap.add_argument("--flat", type=float, default=0.05, help="mean grey difference below which a frame is flat")
    ap.add_argument("--moves", type=float, default=0.15, help="lowest mean grey difference before the end hold")
    ap.add_argument("--hold", type=float, nargs=2, default=[0.6, 1.4], help="end hold range in seconds")
    ap.add_argument("--json", help="write the report here")
    ap.add_argument("--sheet", help="write a 4 x 3 contact sheet (JPEG) here")
    ap.add_argument("--retag", metavar="PATH", help="copy the video to PATH with BT.709 colour tags and faststart (no re-encode)")
    ap.add_argument("--poster", nargs=2, metavar=("T", "PATH"), help="write the frame at T seconds here as the poster")
    a = ap.parse_args()

    rep = {"file": a.video, "gates": {}, "notes": []}
    info = probe(a.video)
    diff, stds, code, err = decode(a.video) if info else (np.zeros(0), np.zeros(0), 1, "no video stream")
    n = len(stds)
    ok = info is not None and code == 0 and n > 1 and not err
    rep["gates"]["decodes"] = ok
    if not ok:
        rep["notes"].append(f"decode: {err or 'fewer than 2 frames'}")
    fps = (info or {}).get("fps") or 30.0
    rep.update({"frames": n, "fps": round(fps, 3), "duration": round((info or {}).get("duration", 0.0), 3)})

    if n > 1:
        flat = diff < a.flat
        tail = 0
        while tail < len(flat) and flat[len(flat) - 1 - tail]:
            tail += 1
        hold_frames = tail + 1 if tail else 0                      # k flat steps at the end = k + 1 still frames
        hold_s = hold_frames / fps
        body = diff[: len(diff) - tail] if tail else diff
        rep["end_hold_s"] = round(hold_s, 3)
        rep["gates"]["end_hold"] = bool(a.hold[0] <= hold_s <= a.hold[1])
        if not rep["gates"]["end_hold"]:
            rep["notes"].append(f"end hold {hold_s:.2f} s; it must be {a.hold[0]} to {a.hold[1]} s")

        blank = stds < 2.0                                         # one colour; a fade to black in the end hold is allowed
        body_blank = blank[: n - hold_frames] if hold_frames else blank
        long_blank = [[round(s / fps, 2), round(k / fps, 2)] for s, k in runs(body_blank) if k / fps > 0.5]
        rep["blank_runs"] = [[round(s / fps, 2), k] for s, k in runs(blank)]
        rep["gates"]["not_blank"] = bool(body_blank.size) and not long_blank and bool(body_blank.mean() <= 0.10)
        if long_blank:
            rep["notes"].append(f"blank for more than 0.5 s at {long_blank} (start s, length s)")

        # A blank still (the black breath before the drop) is policed by not_blank, so it is not a flat here.
        flats = [[round((s + 1) / fps, 2), k + 1] for s, k in runs(flat[: len(flat) - tail] if tail else flat)
                 if k + 1 > 3 and not blank[s: s + k + 1].all()]
        rep["flat_runs"] = flats                                   # [start s, still frames]
        rep["gates"]["no_flats"] = not flats
        if flats:
            rep["notes"].append(f"{len(flats)} run(s) of more than 3 flat frames before the end hold, first at {flats[0][0]} s")

        mean_motion = float(body.mean()) if body.size else 0.0
        rep["mean_motion"] = round(mean_motion, 3)
        rep["gates"]["moves"] = bool(mean_motion >= a.moves)
        if not rep["gates"]["moves"]:
            rep["notes"].append(f"mean frame difference {mean_motion:.3f} is below {a.moves}: the picture hardly moves")
    else:
        for g in ("not_blank", "moves", "no_flats", "end_hold"):
            rep["gates"][g] = False

    if a.master and info:
        rep["master"] = {
            "h264": info.get("codec_name") == "h264",
            "yuv420p": info.get("pix_fmt") == "yuv420p",
            "bt709": all(info.get(k) == "bt709" for k in ("color_space", "color_primaries", "color_transfer")),
            "faststart": bool(faststart(a.video)),
        }
        rep["gates"]["master"] = bool(all(rep["master"].values()))
        if not rep["master"]["bt709"]:
            rep["notes"].append("colour tags: " + ", ".join(f"{k}={info.get(k)}" for k in ("color_space", "color_primaries", "color_transfer")))

    dur = rep["duration"] or (n / fps if fps else 0.0)
    if a.sheet and dur > 0:
        os.makedirs(os.path.dirname(a.sheet) or ".", exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", a.video, "-vf", f"fps={12 / dur:.6f},scale=480:-2,tile=4x3",
                        "-frames:v", "1", "-q:v", "3", a.sheet], check=False)
        rep["sheet"] = a.sheet
    if a.retag and info and info.get("codec_name") == "h264":
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", a.video, "-map", "0", "-c", "copy", "-bsf:v",
                        "h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1",
                        "-movflags", "+faststart", a.retag], check=True)
        rep["retagged"] = a.retag
        rep["notes"].append(f"wrote {a.retag} with BT.709 tags and faststart; run the gates on it")
    if a.poster:
        t, path = float(a.poster[0]), a.poster[1]
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", a.video, "-frames:v", "1", "-q:v", "2", path], check=False)
        rep["poster"] = path

    passed = bool(all(rep["gates"].values()))
    rep["passed"] = passed
    if a.json:
        os.makedirs(os.path.dirname(a.json) or ".", exist_ok=True)
        with open(a.json, "w") as fh:
            json.dump(rep, fh, indent=1)
    for g, v in rep["gates"].items():
        print(f"{'PASS' if v else 'FAIL'}  {g}")
    for note in rep["notes"]:
        print("  -", note)
    print(f"{n} frames at {fps:.2f} fps, end hold {rep.get('end_hold_s', 0)} s, mean motion {rep.get('mean_motion', 0)}")
    print("gates passed. This is a technical check, not a judgement of the film." if passed else "gates FAILED")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
