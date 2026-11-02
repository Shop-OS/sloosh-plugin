# The auto-edit skill tree

Read this first. It decides which branch a clip takes and which references and prompts apply. Every branch
shares the same spine: transcript, cut, beats, optional Sloosh generations, render, mix, check.

```
                                  raw footage + (script or VO)
                                              |
                                   classify (section 1)
                                              |
            +---------------------------------+---------------------------------+
            |                                 |                                 |
   A. TALKING HEAD                    B. NO SPEAKER ON CAMERA              C. HYBRID
   one person speaks to camera        voiceover or script drives it        speaker + long B-roll runs
            |                                 |                                 |
   A1 world-edit hook                 B1 B-roll film with VO                 run A for the speaker shots,
   A2 split-screen explainer (RPN)    B2 product or packshot                 B for everything else,
   A3 clean caption cut               B3 screen or app demo                  one finish, one mix
   A4 kinetic type hook               B4 montage from stills or generations
```

What film.py renders on its own: one full-frame speaker plate with the cut, the camera, depth of field,
captions, the kinetic type moves, a world-edit plate switch, the end card, the finish and the mix. A1, A3
and A4 are complete with it. A2, B and C need extra compositing (split layout, B-roll sequencing, device
frames) built with ffmpeg or custom code on top of `fx.py` and `pro.py`. Tell the user this before you
promise one of those branches.

## 1. Classify the footage (free)

1. Run `prep.py --transcript-only` on the clip. Words with timings mean there is speech.
2. On macOS, prep.py's Apple Vision face track shows whether a face is on camera. Elsewhere, look at a
   contact sheet of one frame a second. A face in more than 60 % of frames, mouth moving on the words, is
   **A, talking head**. Speech but no face, or a face that is not the speaker (a demo with hands, a product
   being held), is **B**. Both, in long runs, is **C**.
3. No speech at all: ask the user for the script or a voiceover recording they own. Without one, the edit
   has no spine.

## 2. Branch A: talking head

What every A edit does before its own moves:

- **Frame the person.** The face track sets the crop. With `--vertical`, a landscape source becomes a
  1080x1920 edit whose camera follows the face. Keep the face the same size across plates and cuts.
- **Camera that breathes.** `camera.style` `breathe` or `push`, one direction per shot. A pull is allowed
  on a reveal (`drift` `out`). Never a zoom in then out inside one shot. See `references/camera-moves.md`.
- **Shallow depth of field.** `dof.blur` 16 to 24 on the room behind the matte, bokeh on the practicals.
  The RPN studio look is a long lens on a dim room with warm practicals. See `references/dof.md`.
- **One finish** over the whole piece: film.py's vignette, grain and bloom.

### A1. World-edit hook (6 to 20 s)

The clip's world is rebuilt around the speaker per beat with a Sloosh video edit, lip sync kept. Grammar in
`references/edit-grammar.md`, the prompt in `references/prompts.md` section 1, the tool steps in
`references/sloosh-mcp.md` section 4. Hybrid reveal (the real room, then the world on a word), captions only.

### A2. Split-screen explainer (30 to 90 s), the RPN format

Measured from reference reels (`references/rpn-grammar.md`): vertical 9:16; B-roll on top, the speaker
below with shallow depth of field; cuts every 1.0 to 1.5 s on B-roll runs and every 3 to 4 s while the
speaker holds; small captions on the seam; full-screen B-roll takeovers on the strongest shots; a title card
at the top. B-roll comes from the user's own footage first (log it locally, `references/prompts.md`
section 4), then from Sloosh generations (section 3). Build a shot list from the transcript: one B-roll idea
per sentence, noun-led. film.py renders the speaker plate. The split layout is custom compositing.

### A3. Clean caption cut (any length)

Jump cuts, breathing camera, depth of field, captions, finish. No world, no type moves. The default when the
user says "just clean it up".

### A4. Kinetic type hook (6 to 16 s)

Type behind the head, a counter, lights down, flicker, a payoff logo (`references/beats.md`). For hype
reels and product launches, with the trailer bed and kit effects. Not for cinematic pieces.

## 3. Branch B: no speaker on camera

The voiceover is the spine. `prep.py` transcribes it the same way, so every move still lands on a word.

### B1. B-roll film with VO (the lab format)

The lab reference: 77 cuts in 110 s, hands, machines, desks, a person moving through a space; small serif and
monospace captions; floating app-icon stickers; a corner scoreboard card; picture in picture of the previous
attempt. Shot list from the VO; log the user's footage locally; fill gaps with Sloosh image_gen then
video_gen clips in the same light; cadence 1.0 to 1.5 s.

### B2. Product or packshot

One hero product. The `product-video` and `product-imagery` skills from the core Sloosh plugin make the
plates. This skill cuts them to the VO with the breathing camera and the finish. Captions in the brand's
type, one accent if the brand has one.

### B3. Screen or app demo

Screen recordings get a crop and push to the active region per sentence (the push is the edit), a soft
shadow on a blurred backplate (blur a still of the desktop locally with ffmpeg), cursor-led cuts, `key_tap`
on real clicks only, and captions below the device.

### B4. Montage from stills or generations

A script, no footage: every beat becomes an image (image_gen with one reference sheet for consistency) and a
4 to 6 s video_gen push from it. Cut on the VO, one finish, an underscore from the user's licensed track or
a published Space.

## 4. Branch C: hybrid

The speaker is on camera for parts, and the rest is B-roll runs longer than a sentence. Run A2 for the
speaker sections (split or full), B1 for the runs, with one shot list, one finish, one mix, and one caption
style throughout. The switch between modes is a hard cut on a word onset.

## 5. What every branch shares

| Step | Tool | Reference |
| --- | --- | --- |
| Connection | `get_connection` | `references/sloosh-mcp.md` §0 |
| Transcript, cut | `prep.py` | SKILL.md workflow |
| Shot log | a local contact sheet of the user's footage | `references/prompts.md` §4 |
| World, B-roll | mode video_edit, or image_gen then video_gen | `references/prompts.md` §1, §3 |
| Underscore | the user's licensed track, a published Space, or `synth_kit.py` (A4 only) | `references/prompts.md` §2 |
| Kit effects | the same sources, on cuts only | `references/sloosh-mcp.md` §3 |
| Camera and DoF | `beats.json` `camera`, `dof` | `references/camera-moves.md`, `references/dof.md` |
| Finish | film.py on the composite | `references/edit-grammar.md` §4 |
| Check | `film.py check`: re-transcribe the mix, loudness, contact sheet | `references/finish-standard.md` |
