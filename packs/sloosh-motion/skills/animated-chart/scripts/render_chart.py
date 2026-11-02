#!/usr/bin/env python3
"""render_chart.py: render a seek(t) chart page to stills, an MP4 and a looping GIF, and check the loop seam.

  python3 <skill>/scripts/render_chart.py work/chart.html --stills 0,1,2,4,7     # look-again stills only
  python3 <skill>/scripts/render_chart.py work/chart.html --mp4 --gif           # every frame, then both exports
  python3 <skill>/scripts/render_chart.py work/chart.html --mp4 --out out/q3   # names out/q3.mp4

The page must set window.seek(t), window.DURATION, window.FPS and window.READY (assets/chart.html does).
The script serves the page's folder on 127.0.0.1, so a plate image in that folder loads without a file:// error.
Every frame is drawn by seek(i / fps) and read back from the page's first <canvas> as a PNG, so frames do not
depend on the screen refresh rate.

Outputs (next to --out, default: the page name in the page's folder):
  <out>_stills/t<sec>.png   one PNG per --stills time
  <out>.mp4                 H.264, yuv420p, 30 fps by default, +faststart
  <out>.gif                 25 fps, a two-pass palette, loops forever (-loop 0), --gif-width wide (default 720)
Seam check (always runs): seek(0) and seek(DURATION) must give identical pixels, and the last frame before
DURATION must be close to frame 0. A failed check prints FAIL and the script exits 2.

Needs Python 3.9+, the playwright package with its Chromium browser, and ffmpeg on PATH for --mp4 or --gif.
Ask the user before installing anything. Install playwright in a virtual environment.
"""
import base64
import functools
import http.server
import os
import shutil
import subprocess
import sys
import tempfile
import threading


def opt(args, key, default=None):
    return args[args.index(key) + 1] if key in args and args.index(key) + 1 < len(args) else default


def serve(folder):
    handler = functools.partial(QuietHandler, directory=folder)
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


GRAB = "() => document.querySelector('canvas').toDataURL('image/png')"
# Compares two seek times inside the page, so no image library is needed here.
DIFF = """([a, b]) => {
    const c = document.querySelector('canvas');
    const g = c.getContext('2d', { willReadFrequently: true });
    window.seek(a);
    const x = g.getImageData(0, 0, c.width, c.height).data;
    window.seek(b);
    const y = g.getImageData(0, 0, c.width, c.height).data;
    let changed = 0, total = 0;
    for (let i = 0; i < x.length; i += 4) {
        const d = Math.abs(x[i] - y[i]) + Math.abs(x[i + 1] - y[i + 1]) + Math.abs(x[i + 2] - y[i + 2]);
        total += d;
        if (d > 0) changed++;
    }
    return { changed, mean: total / (x.length / 4) / 3 };
}"""


def save_png(page, t, path):
    page.evaluate("(t) => window.seek(t)", t)
    data = page.evaluate(GRAB)
    with open(path, "wb") as f:
        f.write(base64.b64decode(data.split(",", 1)[1]))


def ffmpeg(args):
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg is not on PATH. Ask the user before installing it.")
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    page_path = os.path.abspath(args[0])
    folder, name = os.path.split(page_path)
    out = os.path.abspath(opt(args, "--out", os.path.join(folder, os.path.splitext(name)[0])))
    stills = opt(args, "--stills")
    want_mp4 = "--mp4" in args
    want_gif = "--gif" in args
    gif_width = int(opt(args, "--gif-width", "720"))
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("The playwright package is missing. Ask the user before installing it in a virtual environment.")

    server = serve(folder)
    url = f"http://127.0.0.1:{server.server_address[1]}/{name}?t=0"
    status = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_function("window.READY === true", timeout=30000)
        info = page.evaluate("() => ({ d: window.DURATION, fps: window.FPS, w: window.WIDTH, h: window.HEIGHT })")
        duration, fps = float(info["d"]), int(opt(args, "--fps", info["fps"]))
        print(f"page {info['w']}x{info['h']}, {duration:g} s at {fps} fps")

        seam = page.evaluate(DIFF, [0, duration])
        near = page.evaluate(DIFF, [duration - 1 / fps, 0])
        print(f"seam: seek(0) vs seek({duration:g}) changed pixels = {seam['changed']}")
        print(f"seam: last frame vs first frame mean difference = {near['mean']:.3f} of 255")
        if seam["changed"] != 0 or near["mean"] > 2.0:
            print("FAIL: the loop has a seam. Fix the return so the last state equals the first.")
            status = 2

        if stills:
            still_dir = out + "_stills"
            os.makedirs(still_dir, exist_ok=True)
            for value in stills.split(","):
                t = min(float(value), duration)
                path = os.path.join(still_dir, f"t{t:g}.png")
                save_png(page, t, path)
                print(path)

        if want_mp4 or want_gif:
            frames = tempfile.mkdtemp(prefix="chart_frames_")
            count = int(round(duration * fps))
            for i in range(count):
                save_png(page, i / fps, os.path.join(frames, f"f{i:05d}.png"))
            print(f"{count} frames drawn")
        browser.close()
    server.shutdown()

    if want_mp4:
        ffmpeg(["-framerate", str(fps), "-i", os.path.join(frames, "f%05d.png"),
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow",
                "-movflags", "+faststart", out + ".mp4"])
        print(out + ".mp4")
    if want_gif:
        palette = os.path.join(frames, "palette.png")
        scale = f"fps=25,scale={gif_width}:-1:flags=lanczos"
        ffmpeg(["-framerate", str(fps), "-i", os.path.join(frames, "f%05d.png"),
                "-vf", f"{scale},palettegen=stats_mode=diff", palette])
        ffmpeg(["-framerate", str(fps), "-i", os.path.join(frames, "f%05d.png"), "-i", palette,
                "-lavfi", f"{scale}[x];[x][1:v]paletteuse=dither=sierra2_4a", "-loop", "0", out + ".gif"])
        print(out + ".gif")
    if want_mp4 or want_gif:
        shutil.rmtree(frames, ignore_errors=True)
    sys.exit(status)


if __name__ == "__main__":
    main()
