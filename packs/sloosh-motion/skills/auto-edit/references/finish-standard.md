# The finish standard

Every rule here comes from a rejected cut. Hold all of them.

## Picture

- 24 fps. Average 4 sub-frame samples per frame across a 180 degree shutter. Samples never cross a cut, a
  plate switch or the end card.
- Camera: float transforms only, never integer-rounded crops. One continuous move per shot, monotone in zoom
  and position: no zoom in then out, no back and forth. Emphasis comes from the cut and the sound.
- Never decode HDR (HLG or PQ) as SDR. prep.py tone-maps it first, keeps the camera's colour and tags the
  output BT.709.
- Type: Archivo condensed Bold for display, Inter Tight Bold for captions and labels, Instrument Serif for
  emphasis. These are the OFL fonts vendored in the sloosh-motion-director skill. Keep their license texts
  with them if you share the fonts. One accent colour at most.
- Shadows: two layers, a wide soft ambient shadow and a tight contact shadow. Type behind the subject casts
  a soft shadow on the wall, and the subject casts a soft shadow on the type.
- Labels are plain typeset captions or panel headers. Never dark rounded pills with a coloured dot.
- No garbled pseudo-text in any frame. No em dashes in on-screen text.
- Optics: a short colour pulse on big hits, a gentle bloom on highlights, fine grain and a light vignette.
  Subtle.
- Captions: word by word on the measured onset (opacity, a small rise and a defocus that resolves), groups
  of 2 or 3 words by breath, never across a cut. A group is gone before the next one arrives.
- A logo holds at least 2.5 s and keeps one screen position across cuts.

## Sound

- Sound sources, in this order: the user's own licensed files, the output of a published Sloosh Space saved
  into audio/, or local synthesis with `synth_kit.py`. Kit effects mark cuts and type events (the hook, the counter, the stack, the payoff, the world switch
  and the end card), never a plain spoken word.
- Lay a music bed when there is one. audio_prep.py measures its drop; land it on the payoff word.
- Voice chain: high-pass about 85 Hz, cut about 2.5 dB at 280 Hz, add about 2 dB at 3.6 kHz, a little air,
  de-ess, 3:1 compression.
- Music about 18 dB under the voice before the drop and about 15 dB after, ducked by the voice. Impacts
  stay under the word they land on.
- Master to -14 LUFS integrated, true peak under -1 dBTP.

## Encode

- H.264, yuv420p, BT.709 tags, 24 fps, the -14 LUFS mix. `film.py encode` does this and will not replace an
  existing out/edit.mp4 without `--force`.

## Verification (cheap, always)

- Re-transcribe the cut and the final mix: every word must survive (`film.py check`).
- Measure the loudness of the final file.
- Look at the contact sheet of the whole timeline and at full-size frames around every cut, flash and plate
  switch.
