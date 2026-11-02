# The RPN grammar, measured from four reference reels

Four vertical explainer reels were measured with scene detection and contact sheets: a 110 s lab piece (a
3D-print contest), a 36 s hybrid piece, a 62 s split-screen car explainer and a 52 s split-screen software
explainer. This file is what the auto-edit copies from them. Nothing here is about their content.

## Cadence

| piece | length | cuts | mean shot |
| --- | --- | --- | --- |
| lab piece (no speaker) | 110 s | 77 | 1.4 s |
| hybrid piece | 36 s | 33 | 1.1 s |
| car explainer (split screen) | 62 s | 17 | 3.4 s |
| software explainer (split screen) | 52 s | 34 | 1.5 s |

Rules that follow: B-roll runs cut every 1.0 to 1.5 s, on the noun of the sentence. A speaker shot holds
3 to 4 s. Nothing holds longer than a sentence. A cut lands on a word onset, never between words.

## Layout (9:16, 1080x1920)

- Split screen. Top panel: B-roll, 16:9 letterboxed inside the top 45 % or so (the black bars are part of
  the look), or full-bleed when the shot is vertical. Bottom panel: the speaker, seated, chest-up, at a
  desk, a handheld or arm mic in frame, slightly off centre, the face at about 0.62 of the panel height.
  The seam sits at about 0.47 of the frame.
- Full-screen takeover. The strongest B-roll shot takes the whole frame for one or two shots, then the split
  returns. About one takeover every 10 s.
- Picture in picture. A small rounded rectangle, upper right, about 0.28 of the width, shows the previous
  attempt or the wide shot while the main frame is a close-up. Lab format only.
- Scoreboard card. Upper left, a white card with a logo and a name on two lines and a result on the right.
  Updated per contender. Lab format only.

## Type

- Captions. A monospace face (JetBrains Mono is vendored in the sloosh-motion-director skill), capitals,
  about 26 px at 1080 wide, white, letterspaced, a soft dark shadow, one to three words. Centred on the seam
  in split mode, at about 0.55 of the height on full-screen shots. They arrive as a group on the first
  word's onset and leave with the group. No pills, no karaoke.
- Title card. The first 1 to 2 s: a two-line title, serif italic for the connective words and a condensed
  sans in capitals for the nouns, one word in one colour. Centred in the top panel.
- Labels on B-roll. Occasional serif italic single words or a small monospace descriptor near the object,
  never centred with the captions.
- App-icon stickers. Rounded-square icons float around the speaker or over a shot, three to six at a time,
  with a slow drift. Use the user's own icon files. Never reproduce another company's mark.
- Prompt card. A white rounded card, typed on, centred, when the piece is about prompting something.

## Camera and picture

- The speaker plate barely moves: a slow push of about 3 % per shot, with the alternate-shot jump-cut cover.
  Shallow depth of field on the room, with warm practicals (a ring light, a lamp) as bokeh discs.
- B-roll is handheld and close: hands, objects, real motion. Generated B-roll must match: a slow push or a
  handheld drift, never a static render.
- Grade: slightly warm, lifted blacks, no heavy look. The engine's finish (grain and a light vignette)
  matches it.

## Sound

- Voice up front, dry and compressed. A quiet bed with no drop, about 20 dB under. Diegetic sound from the
  B-roll kept and used (a printer, a drop, a click). Effects only on cuts and on UI moments.

## How the auto-edit copies it

- Branch A2 or B1 in skill-tree.md.
- film.py renders a single plate: the speaker, full frame. It has no split layout, no picture in picture
  and no monospace caption option. A full split-screen RPN reel needs custom compositing on top of
  `fx.py` and `pro.py`. Say so to the user before you promise one.
- What film.py does give you for A2: `camera.style` `push` (or `breathe`), `base` 1.0, `settle` 0.03,
  `dof.blur` 18, captions in short chunks, and the cadence above for the cut list.
- Shot list from the transcript, one line per sentence: word index, noun, shot idea, source (the user's
  library or a generation).
