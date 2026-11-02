# Start and end frames

A video model can take a start frame, an end frame or both. `list_models` with mode `video_gen` reports each model's frame
support: the start frame is required, optional or not taken, and the end frame is optional or not taken. Some models take an
end frame only together with a start frame. Pick a model that supports the frames you pass. Do not choose a model from memory.

In a quote, an image asset goes in with the role start_frame or end_frame. Both frames use the film's aspect ratio.

## Animated plate

| Goal | Start frame | End frame | Prompt |
|---|---|---|---|
| Slow living background | the approved still | none | one slow camera move, the clean type band stays clean |
| Seamless loop | the approved still | the same still | the camera drifts and returns to its start; nothing new enters |
| Clean last frame behind the end card | the approved still | a second approved still | the camera settles on the second framing |

- Make the second still in the same still round, from the first still as the reference. Keep the lens, framing, light direction and clean type band the same. Two frames that disagree make the model swing the camera to join them.
- Ask the user to approve both stills before the clip round.
- Use no generated audio, and keep every surface free of writing.

## A-to-B type morph

The default for one line becoming another is the swap move in code. It is exact on every frame and costs nothing. Its words
slide out of masks and rise in, so never pay a model for that motion.

A generated morph is worth it only for a material change that code cannot draw: the ink of the first line softens and flows
into the shapes of the second line, like wet ink or molten metal. Offer it only when the user asks for that look. State the
risk: letters can wobble or turn into wrong glyphs in the middle frames.

This is the one exception to the director's QA rule of no text in generated footage. The only text allowed in the clip is
the two code-rendered lines in the start and end frames. Check the clip at both ends and on every frame between them.

Limits:

- At most 4 words in each state.
- The same layout, the same field colour and the same type size in both states.
- The shortest clip the model takes, 3 to 5 s at most.
- One morph per film.

Steps:

1. Build both states as scenes in tl.py, each with a settled hold, and render the film as in the build steps.
2. Take one settled frame of each state from the render: ffmpeg -ss TIME_A -i out/NAME_v1.mp4 -frames:v 1 refs/morph_a.png. Do the same for B.
3. Read both frames and check every letter. Fix the copy in tl.py, not in the frame. After a copy fix, render the frames again. A changed frame needs a new quote and a new approval.
4. Bring both frames into Sloosh: follow the server's upload instruction.
5. Call `list_models` with mode `video_gen`. Pick a model that takes a start frame and an end frame.
6. Call `quote_generation` with frame A as the start frame and frame B as the end frame, at the film's aspect ratio, with no generated audio.
7. Show the quote and wait for the user, as the round rules in SKILL.md say.
8. Call `generate` with a stable key, for example `motion-kt-serum-morph-9x16-v1`.
9. If `show_generation` is available, call `show_generation` once with the operation id. When the user says the result is ready, call `get_generation` once to read its outputs.
10. If not, poll `get_generation` with the operation id about every 15 seconds until it settles.
11. When it is done, call `get_asset` with its kind and id. Download the clip into clips/morph.mp4.
12. Make a full-rate sheet of the clip: python3 lib/sheets.py dense clips/morph.mp4 0 CLIP_LENGTH --fps FILM_FPS. It burns the frame number into every frame. Read every sheet.
13. If any frame shows a wrong letter, a wrong word or a new mark, do not use the clip. Tell the user, and deliver the swap move in code.
14. Deliver the clip on its own. Ask the user before you cut it into the film.
15. To cut it in, add it as one fk.CutList row at the scene's time in edit.py (see the director skill's footage rules).
16. Keep the type layer off while the clip plays.

Morph prompt (positive phrasing only):

```
Start exactly on the first frame and end exactly on the last frame. The ink of the first line softens and flows,
like wet ink on paper, into the shapes of the second line, with a smooth weighted ease that settles without overshoot.
The camera stays locked. The background colour and the type size stay the same. Nothing new enters the frame.
```

- Describe the change of material between the frames. Never ask the model to type, spell or scramble letters.
- Never put a brand, product line or public figure in the prompt.
