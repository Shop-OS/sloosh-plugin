# beats.json

Every key except `captions` is optional. Leave out a move and `film.py` skips it, with its sounds.
Word numbers are the edit indices that prep prints last (`prep/edl.json` `words`). film.py stops with a
message if one is out of range. Times come from each word's measured onset, so moves land on the syllable.
Every piece of on-screen text comes from this file. The code writes no text of its own. The example is a
reference build. A clip without a number has no `counter`. A clip without a logo uses `text`.

```json
{
  "hook": {
    "text": "EDITING",
    "word": 0,
    "size": 296,
    "accent": { "text": "nowadays", "word": 1 }
  },
  "counter": {
    "start_word": 3,
    "land_word": 4,
    "land_offset": 0.16,
    "to": 100,
    "prefix": "",
    "suffix": "%"
  },
  "stack": { "text": "AUTOMATED", "word": 5, "size": 196 },
  "punches": [{ "word": 14, "amount": 0.13 }],
  "lights_down": { "word": 16, "until_word": 26 },
  "flicker": {
    "word": 24,
    "words": ["IMAGES", "VIDEO", "3D", "AUDIO", "WORLDS", "EVERYTHING"],
    "step": 0.105
  },
  "payoff": {
    "word": 26,
    "logo": "brand/logo.png",
    "hold": 2.6,
    "logo_height": 150
  },
  "world": { "from_word": 4, "flash": 0.12 },
  "captions": {
    "chunks": [
      [6, 7, 8],
      [9, 10, 11],
      [12, 13]
    ],
    "emphasis": [13],
    "size": 74
  },
  "end_card": { "logo": "brand/logo.png", "text": "", "seconds": 1.15 },
  "music": { "drop_on_word": 26, "under_voice_db": [18, 15] },
  "camera": { "style": "breathe", "base": 1.04, "drift": ["in", "out", "in", "in", "none"], "settle": 0.03 },
  "dof": { "blur": 18, "bokeh": 0.5, "ramp": 0.0 },
  "segment_zoom": [1.0, 1.1, 1.0, 1.1, 1.0],
  "theme": { "ink": [0.067, 0.067, 0.067], "accent": [0.067, 0.067, 0.067] }
}
```

## The moves

| key | what happens | why these defaults |
| --- | --- | --- |
| `hook` | The word rises letter by letter out of a slot behind the speaker's head, in Archivo condensed Bold sized to the frame. The head covers its foot. With little headroom, more of the word sits behind the head: check the still. `accent` adds a small serif word above its right shoulder. | The subject in front of the type makes it read as designed, not overlaid. The serif accent is the editorial touch. |
| `counter` | A rolling odometer from 0 to the integer `to`, with an optional `prefix` and `suffix` ("%", "x", "K"). It starts on `start_word` and lands `land_offset` s after `land_word` with a camera punch, a colour pulse and an impact. It shrinks to fit the width. | An odometer with motion blur reads as real. Easing out makes the last digits land on the beat. |
| `stack` | A second word types itself under the counter, one key tap per letter, while the counter lifts and shrinks. | Builds a headline in two beats. |
| `punches` | A quick push-in on a word. `amount` is the zoom added. A negative amount pulls out; `seconds` sets its length. | Emphasis by camera, one direction within the shot. |
| `lights_down` | From `word`, the set falls to a warm spotlight around the head, and the speaker dims a little. At `until_word` (default: the payoff word) a light burst from behind the head turns the room back on. | A visible tension and release, timed to the music build and drop. |
| `flicker` | Words flash behind the head, one every `step` seconds, until the payoff. | "You can do everything": show the everything. |
| `payoff` | A light burst, the music drop, and above the head either `logo` (a PNG) or `text` (a word built letter by letter, `size`), held `hold` s. With neither, only the burst and the drop. Leave the payoff word out of the captions when it gets a logo or text. | The brand lands on the payoff word and holds 2.5 s at least. When the payoff is the last word, put the mark on the end card instead. |
| `world` | From `from_word` to `until_word` (default: the end) the picture is the world edit that `world.py import` prepared, with that plate's matte and face under the same camera. A short light `flash` (seconds, 0 for none) and the `portal` sound cover the switch. `ink` sets the type colour over the world (default white). | The real room sells the claim. The world arrives on the turn or the payoff. |
| `captions` | Word-by-word captions. `chunks` are groups of word indices (2 or 3 words, never across a cut). `emphasis` words switch to the serif, larger. Trailing commas and periods are dropped; `"keep_punctuation": true` keeps them. `"space": false` joins words for scripts that use no spaces. `y` sets the baseline. Words covered by big type are usually left out. | Chunk by breath like an editor. A group leaves before the next one arrives. |
| `end_card` | A push-through into a light card with the `logo` (built and glinted) and an optional line of `text` under it, such as a handle or a call to action. `background` sets the card colour. | Ends the hook on the brand. |
| `music` | Offsets the bed so its measured drop lands on `drop_on_word`. `under_voice_db` is how far the bed sits under the voice before and after the drop. | 18 dB before and 15 dB after, set by ear. Louder fights the voice. |
| `camera` | The camera's manner. `style`: `alternate` (default: shots alternate 1.0 and 1.10 so jump cuts read as intentional), `push` (one resting zoom, each shot drifts in), `still` (no drift) or `breathe` (a slow in-and-out of about 0.6 % on a 4 s period). `base`: resting zoom (1.0). `drift`: one direction per shot, `in`, `out` or `none`, so a shot can pull out for a reveal. `drift_amount` (0.02). `settle`: a micro push after every cut (0.035). | A subtle move keeps a static talking head alive. One direction per shot keeps it from pumping. |
| `dof` | Shallow depth of field. The background plate behind the person matte is blurred by `blur` px (16 feels like a 50 mm lens wide open, 28 like a long lens). Highlights above `bokeh_threshold` bloom into soft discs scaled by `bokeh`, and blacks lift a touch. Optional `from_word`, `until_word` and `ramp` seconds rack into it. The subject is never blurred. | A blurred room is the biggest cinema-camera cue a phone clip can borrow. |
| `segment_zoom` | Base zoom per segment between cuts. It overrides `camera.style`. | Alternating framing is the classic jump-cut cover. |
| `theme` | `ink` for type on a light wall (white is used while the lights are down), `accent` for the stack word. | One accent at most. |
| `fonts` | Paths to `.ttf` or `.otf` files that replace `display`, `sans`, `sans-reg` or `serif`, for example a CJK or Arabic family. | The vendored families cover Latin only. |

Logos: a PNG with transparency keeps its colours. An opaque dark-on-light PNG gets its alpha from luminance.
Set `"ink": [r, g, b]` on `payoff` or `end_card` to recolour it, for example white on a dark world.

## Fonts

pro.py reads the OFL fonts that ship in the sloosh-motion-director skill (its assets/fonts folder):
Archivo (condensed Bold) for `display`, Inter Tight Bold and Regular for `sans` and `sans-reg`, and
Instrument Serif for `serif`. Set `AUTOEDIT_FONTS` to another folder with the same file names, or name
your own files under `fonts`. Nothing is downloaded.
