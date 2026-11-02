# The edit grammar: what makes it read as film, not as a thumbnail

A hype-reel edit (trailer boom, coloured slam type, a whoosh on every beat) reads as slop once the world
edit looks like cinema. These rules are the default for every world-edit hook (branch A1). The kinetic
type moves in beats.md are for branch A4 only.

## 1. Structure: the hybrid reveal

The viewer needs the "before" to read the "after". The real room plays for the first beat (the question or
the claim). The world edit comes in as a hard cut on the first word of the second beat and plays to the end.
No dissolve, no flash longer than two frames, no lights-down gag. One cut, on a word onset, is the whole trick.

In beats.json: `"world": {"from_word": N, "flash": 0.06}` with N the first word of the second beat. Leave
out `lights_down`, `flicker`, `hook`, `counter` and `stack`.

If the first beat is itself a strong world, still open on the real room. The contrast is the explanation.

## 2. Camera: one move, one cut

One slow push for the whole piece, about 1.00 to 1.08 over six seconds, never reversing
(`camera.style` `push`, `drift_amount` about 0.05, `settle` 0). On the payoff word, a cut-in, never a zoom:
a punch with `amount` 0.10 and `seconds` 0.04, so the same plate is about 10 % tighter at once. After the
last word, cut to a plain end card for 1.2 to 1.5 s (`end_card` with `seconds`, and a logo only when
the brand needs one).

## 3. Type: captions carry it

- Captions only, by default: the sans at about `size` 42 at 1080p, low in the frame (`y` at about 0.90 of
  the height), at most three words per chunk, word by word on the onset, gone before the next group.
- No display type on the hype beat. A slammed word in a bright colour is the thumbnail reflex. The world
  on screen already says it.
- One quiet display moment is allowed on the number or the payoff: the line set small in the serif, in
  the empty side of the frame, under 120 px, no colour.
- The closing line on the end card in the sans, centred, one sentence, no handle unless the user asks.
- No accent colour. The world edit owns the colour.

## 4. Grade: one finish over both plates

The real room and the generated world must share one look, or the cut between them reads as a glitch. The
engine runs one finish over every frame of the composite: a soft vignette, luminance-weighted grain and a
gentle bloom (`pro.finish` and `pro.bloom`, called by film.py). Do not grade the plates separately. If the
world plate is far warmer or cooler than the room, say so in the world-edit prompt (the light on the face
follows each world) rather than fixing it after.

## 5. Sound: three layers

- Voice: the chain in `pro.process_voice` (high-pass, de-mud, presence, de-ess, gentle compression,
  limiter). Always on top.
- Bed: a filmic underscore with no drop for a world-edit hook (felt piano, a low drone, a pulse that swells
  and collapses), about 20 dB under the voice and ducked by it. It comes from the user's own licensed track
  or from a published Space. The synthesized bed from `synth_kit.py --music` is a trailer bed with a drop,
  for hype reels (A4), not for this.
- Kit effects: at most one, on the hard cut (`whoosh_air`), or none. film.py places a sound only when its
  file exists in audio/sfx, so keep only the sounds you want there (`synth_kit.py --only whoosh_air`).
  Never a boom on the payoff: the payoff is the silence after the party.
- Master at -14 LUFS with true peak under -1 dBTP. Re-transcribe the mix: every word must survive.

## 6. Prompting the world edit

- Write the five-block prompt in prompts.md as it stands. The prompt enhancer does not take edit modes, so
  quote with the enhancer off and keep the LOCKED block and the NO TEXT block word for word.
- No screens, monitors, dashboards, posters or signs in any beat. The edit grows pseudo-text on them.
- Light on the face follows each world. The identity, mouth shapes, wardrobe, mic and camera are locked.
- Use the delivery resolution for the real run. A lower resolution is only for a look test.

## 7. What to look at before calling it done

Stills at: the first frame, the frames before and after the world cut, each beat, the cut-in and the held
frame. The cut between plates should look like a cut in one film. If the type is the first thing you notice,
remove it.
