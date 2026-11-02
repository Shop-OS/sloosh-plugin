# Story, edit and pages

This file holds the copy holds, the beat grid in tl.py, the shared edit.py, the page contract and the caption layer.

## Copy holds

Reading holds count only settled time.

| On screen | Minimum settled hold |
|---|---|
| 1 punch word | 0.6 to 0.8 s (at least 0.83 s if it carries meaning) |
| 2 to 4 word phrase | 0.3 s per word, plus 0.4 s |
| 5 to 10 word line | 0.33 s per word, or characters / 15 per second, whichever is longer |
| Stat and label | 1.2 to 2.0 s |
| End card | at least 2.0 s; only the final 0.5 s is frozen |

Over footage (the caption layer), add 25% to every hold. Nothing that must be read goes faster than 17 characters per second.

## Story on the beat grid (tl.py)

A type film is a list of scenes on one beat grid, plus fields (the colour behind them). The default is Bold Poster, 15 s, 120 BPM: a beat is 0.5 s and a bar is 2 s. The full file is `examples/bold-poster/tl.py`. Its core:

```python
BPM = 120.0; B = 60.0 / BPM; GENRE, KEY = "house", "Am"; SAFE = "reels"
DROP = 16 * B; T_BREATH = DROP - 0.1; T_END = 24 * B; LEN = 30 * B
def S(id, move, a, b, beats=None, **o): return dict(id=id, move=move, t=[a, b], beats=beats or [], **o)
PAPER, INK_, ACC = "#F3EEE4", "#121212", "#FF4A1C"
FIELDS = [(0.0, PAPER, INK_, ACC, "cut"), (4*B, ACC, INK_, PAPER, "up"), (8*B, INK_, PAPER, ACC, "left"),
          (12*B, PAPER, INK_, ACC, "down"), (DROP, ACC, INK_, PAPER, "cut"), (20*B, INK_, PAPER, ACC, "cut"), (T_END, PAPER, INK_, ACC, "right")]
TYPE = {"kt": [
  S("tick", "ticker", 0, LEN, y=0.74, size=60, speed=150, gaps=[(DROP, 20*B)]),
  S("hook", "stack", 0, 4*B, [0.5*B, 1.5*B, 2.5*B], kicker="DROP 04  ·  SS27", accent=[1], inv=[(3*B, 2, -1, 0.25)]),
  S("stat", "count", 4*B, 8*B, [4.5*B], kicker="ALL WEEKEND", dur=0.9),
  S("every", "stretch", 8*B, 11.5*B, [8.5*B, 9.5*B], accent=[1]),
  S("ends", "slam", 12*B, 15*B, [12*B, 13*B, 14*B], accent=[2], inv=[1], exit="cut"),
  S("now", "zoom", 15*B, DROP + 1.0, [15*B], dur=1.0),
  S("grid", "grid", DROP, 20*B, [DROP + 2*B, DROP + 3*B, DROP + 3.5*B], rows=9, cols=3, z=5),
  S("sale", "frame", 20*B, 23.5*B, [20*B], accent=True),
  S("end", "end", T_END, LEN, size=110)]}
COPY = {"hook": ["NEW", "SEASON", "DROP"], "stat": ["40%", "OFF EVERYTHING"], "end": ["YOUR BRAND", "BRAND.COM  ·  ENDS SUNDAY"]}
```

The offer in the example is a placeholder. Replace every word with the user's approved copy.

- Field row (t, bg, ink, accent, how): the field is fully in at t, so a wipe (up, down, left, right or iris, 0.36 s) lands on the beat. A cut is instant. Text colours follow the field (--ink, --acc), so an accent block flips its accent to paper by itself.
- Scene row S(id, move, in, out, beats, options): beats are landing times, one per line, word or step. A scene's exit takes 0.2 to 0.25 s after out. The next scene lands at least 0.25 s after the previous out, unless the exit is cut.

| Time | Beats | Scene (move) | Field | Type moment | SFX |
|---|---|---|---|---|---|
| 0 to 2.0 | 0 to 3 | hook (stack) | paper | NEW / SEASON / DROP land on beats 1 to 3; DROP inverts on beat 3 | tick x3, shutter |
| 2.0 to 4.0 | 4 to 7 | stat (count) | orange wipes up | 40% rolls in on an odometer, the label lands | whoosh, ticks, impact |
| 4.0 to 5.75 | 8 to 11 | every (stretch) | ink wipes left | EVERY then THING squeeze to fill, width 62 to 125 | whoosh x2 |
| 6.0 to 7.5 | 12 to 14 | ends (slam) | paper wipes down | ENDS / THIS (inverted) / SUNDAY, one per beat | impact x3, shutter |
| 7.5 to 9.0 | 15 to 17 | now (zoom) | orange cut at 8.0 | NOW lands, its O opens on orange, the camera flies through | impact, whoosh, subdrop |
| 8.0 to 10.0 | 16 to 19 | grid (grid) | orange | a grid of DROP 04; inversion waves on 3 beats | shutter x3, punch |
| 10.0 to 11.75 | 20 to 23 | sale (frame) | ink cut | SALE stretches to fill the safe height; a negative hit | impact and subdrop |
| 12.0 to 15.0 | 24 to 29 | end (end) | paper wipes right | the brand name tracks in, a rule, the URL | impact, sparkle |

A ticker band at 74% of the height runs through all of it and steps aside for the grid.

- Short (8 to 10 s): hook, stat, ends, zoom, end (LEN = 20*B, the drop on beat 12).
- Long (20 s): add a second stack after the grid and an echo stack (move="echo") before the end. Keep a new field every bar.

Every scene change is a cut. The default has 9 scenes and 7 field changes in 15 s: at least 8 cuts and at least 6 distinct windows.

## The edit (edit.py)

edit.py is shared by every preset. Per frame it does this:

1. Fields, or the plate with its slow push.
2. The type layer.
3. The plate's subject cut-out in front of the type.
4. Punches on tl.PUNCH: scale 1 + 0.045 e^(-t/0.1), plus a 10 px RGB split that decays in 0.05 s.
5. Zoom blur through type-as-camera windows, centred, because the page puts the counter at frame centre.
6. fk.hits(tl.HITS): negative, duo, red, glitch, smear, white. These hit the type too.
7. Finish: grain 3 to 5. No contrast curve and no vignette on flat fields, so brand colours stay true. Vignette 0.25 only with a plate.
8. A 2-frame flash at the punch-through.

Effect budget per 10 to 15 s: one signature move repeated 3 to 6 times, plus at most 3 support moves. At most 4 whole-frame hits, exactly 1 drop moment and at most 1 type-as-camera. Never stack 3 effects on one word.

## Pages

A page is about 20 lines: @font-face rules for its families (the files are in the film's fonts/ folder), the theme classes .d .s .m .it .board, a div with id stage, the director's kit.js, then ktkit.js, and one boot call:

```js
KT.boot({ fonts: ['900 100px Archivo', 'italic 400 100px "Instrument Serif"'], axes: { wdth: [62, 125] }, slnt: -10, caption: false });
```

- KT.boot loads the fonts before it measures. It reads TL.TYPE.kt and TL.COPY, builds and measures each scene, and defines window.render(t).
- Each frame, render(t) sets --bg, --ink and --acc from FIELDS and calls every scene's pure render(t). No CSS animation and no timer. Use seeded hashes only.
- An unknown move or a missing COPY[id] throws, and kt_sheet.py prints it.
- slnt is the skew in degrees for the wave move's snaps. Leave it out for no skew.

Scene options for any move: id (the COPY key), move, t=[in, out], beats, then size (px at 1080), max, y (0 top to 1 bottom of the box), box=[l, top, r, bot] (fractions; noRail=True for decorative or top bands), align (center or left), accent, outline, axes, inv, exit (wipe, up, squeeze or cut), kicker and z. Per-move options are in `references/moves.md`.

## The caption layer (kinetic type over another style)

1. In the base film: copy <kinetic-typography>/lib/ktkit.js, kt.css and ktfield.py into lib/, and copy <kinetic-typography>/examples/caption-layer/ui/kt_caption.html into ui/. The fonts are already in fonts/.
2. Paste examples/caption-layer/tl_captions.py into the base tl.py below COPY. Captions live only in TYPE["kt"] and COPY[id], so the director's ui/type.html never sees them.
3. Run python3 tl.py, then python3 lib/render_html.py ui/kt_caption.html --dur LEN --out frames/kt_caption --jobs 1.
4. In edit.py, add CAP = fk.Overlay("frames/kt_caption"). In render(t), right after the director type layer, add img = CAP.over(img, t). That is before fk.hits, so hits hit the captions too.
5. In audio.py, import ktfield as kf, then loop over kf.sfx_cues(tl, layer=True) and place ak.tick(), ak.impact(0.9) or ak.shutter().
6. Keep captions in the middle band (CAPTION_BOX, 47% to 65% of the height on 9:16), left of the rail. Never put a caption over a face. Never put a caption in the beats of a director lockup, echo or slam. Start at least 1 beat after a director lockup's out.
7. Take word times from beats, or from voice-over or lyric timestamps minus 0.05 s. Add 25% to holds.

lockA, slam, stack and echo also work in the caption page, for hype words over footage.
