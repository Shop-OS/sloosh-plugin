#!/usr/bin/env python3
"""Helpers that turn one long talking video into short clips for the auto-edit skill.

  proxy   SRC OUT                     a small 360p copy, so the long transcript runs fast
  windows PROJECT [--out DIR]         timestamped phrase lines from PROJECT/prep/words_src.json,
                                      split into overlapping windows when the source is long
  rank    CANDIDATES OUT [--top N]    check the picked highlights, drop overlaps, keep the best N
  cut     SRC RANKED OUTDIR [--pad S] copy each ranked highlight out of SRC, with padding, no re-encode
  trim    PROJECT FIRST LAST OUT      cut PROJECT/prep/sdr.mp4 from word FIRST to word LAST (fallback)
  voiceover SHORT VOICE OUT [--at S] [--duck V]
                                      mix a voice-over file into a finished short, the speech lowered under it

Standard library only. ffmpeg and ffprobe must be on PATH.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

PHRASE_GAP = 0.6
PHRASE_WORDS = 14
LONG_SOURCE = 30 * 60
WINDOW = 20 * 60
OVERLAP = 60
MIN_LEN, MAX_LEN = 10.0, 90.0


def need(tool):
    if not shutil.which(tool):
        sys.exit(f'{tool} is not on PATH. Install ffmpeg first.')


def run(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        sys.exit(f'{cmd[0]} failed:\n{res.stderr[-2000:]}')
    return res.stdout


def duration(path):
    need('ffprobe')
    out = run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', path])
    return float(json.loads(out)['format']['duration'])


def stamp(t):
    m, s = divmod(max(t, 0.0), 60)
    return f'{int(m):02d}:{s:04.1f}'


def load_words(project):
    path = os.path.join(project, 'prep', 'words_src.json')
    if not os.path.exists(path):
        sys.exit(f'{path} is missing. Run the auto-edit prep.py with --transcript-only first.')
    with open(path) as f:
        words = json.load(f)
    if not words:
        sys.exit(f'{path} has no words.')
    return words


def start_of(w):
    return float(w.get('onset', w['s']))


def phrases(words):
    out, cur = [], []
    for w in words:
        if cur and (start_of(w) - float(cur[-1]['e']) > PHRASE_GAP or len(cur) >= PHRASE_WORDS
                    or cur[-1]['w'].rstrip().endswith(('.', '?', '!'))):
            out.append(cur)
            cur = []
        cur.append(w)
    if cur:
        out.append(cur)
    return [(start_of(p[0]), float(p[-1]['e']), ' '.join(w['w'].strip() for w in p)) for p in out]


def cmd_proxy(a):
    need('ffmpeg')
    if os.path.exists(a.out) and not a.force:
        sys.exit(f'{a.out} exists. Add --force to make it again.')
    run(['ffmpeg', '-v', 'error', '-y', '-i', a.src, '-map', '0:v:0', '-map', '0:a:0',
         '-vf', 'scale=-2:360,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '30',
         '-c:a', 'aac', '-b:a', '96k', '-ac', '1', a.out])
    print(f'proxy: {a.out} ({stamp(duration(a.out))}, same timeline as the source)')


def cmd_windows(a):
    lines = phrases(load_words(a.project))
    end = lines[-1][1]
    spans = [(0.0, end)]
    if end > LONG_SOURCE:
        spans, t = [], 0.0
        while t < end:
            spans.append((t, min(t + WINDOW, end)))
            t += WINDOW - OVERLAP
    os.makedirs(a.out, exist_ok=True)
    for n, (t0, t1) in enumerate(spans, 1):
        path = os.path.join(a.out, f'window-{n:02d}.txt')
        with open(path, 'w') as f:
            for s, e, text in lines:
                if s >= t0 and s < t1:
                    f.write(f'[{s:.1f}-{e:.1f}] {text}\n')
        print(f'{path}: {stamp(t0)} to {stamp(t1)}')
    print(f'{len(lines)} phrases, {stamp(end)} of speech, {len(spans)} window(s)')


def cmd_rank(a):
    with open(a.candidates) as f:
        cands = json.load(f)
    if not isinstance(cands, list):
        sys.exit('The candidates file must hold a JSON list.')
    good = []
    for n, c in enumerate(cands):
        try:
            s, e, score = float(c['start']), float(c['end']), float(c['score'])
            hook, title, reason = str(c['hook']), str(c['title']), str(c['reason'])
        except (KeyError, TypeError, ValueError):
            print(f'skip {n}: it needs start, end, score, hook, title and reason')
            continue
        if not (0 <= score <= 100) or e <= s:
            print(f'skip {n}: score must be 0 to 100 and end after start')
            continue
        if not (a.min <= e - s <= a.max):
            print(f'skip {n}: {e - s:.1f} s is outside {a.min:.0f} to {a.max:.0f} s')
            continue
        good.append(dict(start=s, end=e, score=score, hook=hook, title=title, reason=reason))
    kept = []
    for c in sorted(good, key=lambda c: -c['score']):
        if all(c['end'] <= k['start'] or c['start'] >= k['end'] for k in kept):
            kept.append(c)
    kept = sorted(kept[:a.top], key=lambda c: -c['score'])
    for n, c in enumerate(kept, 1):
        c['id'] = f'short-{n:02d}'
    with open(a.out, 'w') as f:
        json.dump(kept, f, indent=2)
    for c in kept:
        print(f"{c['id']}  {c['score']:5.1f}  {stamp(c['start'])}-{stamp(c['end'])}  "
              f"{c['end'] - c['start']:4.1f}s  {c['title']}")
    print(f'{len(kept)} of {len(cands)} kept in {a.out}')


def cmd_cut(a):
    need('ffmpeg')
    with open(a.ranked) as f:
        ranked = json.load(f)
    only = set(a.only.split(',')) if a.only else None
    os.makedirs(a.outdir, exist_ok=True)
    total = duration(a.src)
    for c in ranked:
        if only and c['id'] not in only:
            continue
        t0 = max(0.0, c['start'] - a.pad)
        t1 = min(total, c['end'] + a.pad)
        out = os.path.join(a.outdir, f"{c['id']}.mp4")
        if os.path.exists(out) and not a.force:
            print(f'{out} exists, kept')
            continue
        run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t0:.3f}', '-i', a.src, '-t', f'{t1 - t0:.3f}',
             '-map', '0:v:0', '-map', '0:a:0', '-c', 'copy', '-avoid_negative_ts', 'make_zero', out])
        print(f'{out}: {stamp(t0)} to {stamp(t1)}')


def cmd_trim(a):
    need('ffmpeg')
    words = load_words(a.project)
    if not (0 <= a.first <= a.last < len(words)):
        sys.exit(f'Word indices must be 0 to {len(words) - 1}, first before last.')
    sdr = os.path.join(a.project, 'prep', 'sdr.mp4')
    if not os.path.exists(sdr):
        sys.exit(f'{sdr} is missing. Run the auto-edit prep.py with --transcript-only first.')
    t0 = max(0.0, start_of(words[a.first]) - 0.1)
    t1 = min(duration(sdr), float(words[a.last]['e']) + 0.3)
    run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t0:.3f}', '-i', sdr, '-t', f'{t1 - t0:.3f}',
         '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '192k', a.out])
    print(f'{a.out}: {stamp(t0)} to {stamp(t1)} of {sdr}')


def cmd_voiceover(a):
    need('ffmpeg')
    if not 0.0 <= a.duck <= 1.0:
        sys.exit('--duck must be 0 to 1.')
    total = duration(a.short)
    if a.at >= total:
        sys.exit(f'--at must be before the end of the short ({total:.1f}s).')
    delay = int(round(a.at * 1000))
    mix = (f'[0:a]volume={a.duck}[bed];[1:a]adelay={delay}|{delay},apad[vo];'
           f'[bed][vo]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]')
    run(['ffmpeg', '-v', 'error', '-y', '-i', a.short, '-i', a.voice, '-filter_complex', mix,
         '-map', '0:v:0', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
         '-t', f'{total:.3f}', a.out])
    print(f'{a.out}: voice from {stamp(a.at)}, speech at {a.duck:.2f}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('proxy'); p.add_argument('src'); p.add_argument('out')
    p.add_argument('--force', action='store_true'); p.set_defaults(fn=cmd_proxy)
    p = sub.add_parser('windows'); p.add_argument('project')
    p.add_argument('--out', default='windows'); p.set_defaults(fn=cmd_windows)
    p = sub.add_parser('rank'); p.add_argument('candidates'); p.add_argument('out')
    p.add_argument('--top', type=int, default=5)
    p.add_argument('--min', type=float, default=MIN_LEN); p.add_argument('--max', type=float, default=MAX_LEN)
    p.set_defaults(fn=cmd_rank)
    p = sub.add_parser('cut'); p.add_argument('src'); p.add_argument('ranked'); p.add_argument('outdir')
    p.add_argument('--pad', type=float, default=1.5); p.add_argument('--only', help='ids, such as short-01,short-03')
    p.add_argument('--force', action='store_true'); p.set_defaults(fn=cmd_cut)
    p = sub.add_parser('trim'); p.add_argument('project'); p.add_argument('first', type=int)
    p.add_argument('last', type=int); p.add_argument('out'); p.set_defaults(fn=cmd_trim)
    p = sub.add_parser('voiceover'); p.add_argument('short'); p.add_argument('voice'); p.add_argument('out')
    p.add_argument('--at', type=float, default=0.0, help='seconds into the short where the voice starts')
    p.add_argument('--duck', type=float, default=0.3, help='volume of the original speech under the voice')
    p.set_defaults(fn=cmd_voiceover)
    a = ap.parse_args()
    a.fn(a)


if __name__ == '__main__':
    main()
