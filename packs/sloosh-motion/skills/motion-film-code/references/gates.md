# Gates, master and delivery

Read this file after every render and before you deliver. A render that fails a gate is not finished. A render that passes every gate is still not an approved film.

## The contact sheet

Make a contact sheet after every render and look at it before you run the next step.

- The director's qa.py writes out/qa/contact.png, out/qa/phone360.png and out/qa/report.json. The report adds loudness, true peak, cuts, flash frames and audio clicks.
- `scripts/gates.py` with --sheet writes a 4 x 3 sheet of the whole film. Use it on drafts.
- To look at one moment, use qa.py at with the times, or render one frame with the still method of the route.

Describe each frame of the sheet in one sentence before you judge it. Look for these on the sheet: type that is cut off or outside the safe zone, wrong words, a frame with no subject, two sections that look the same, a missing hero moment, and page chrome such as a scroll bar. All-black frames from the HTML route can mean that headless Chromium has no WebGL: draw that layer with 2D drawing or CSS instead.

## The gates

Run `scripts/gates.py` on every render. It prints PASS or FAIL for each gate and exits with 1 if one fails.

| Gate | It passes when | If it fails |
|---|---|---|
| decodes | ffprobe finds a video stream and ffmpeg decodes every frame with no error | Render again. Check the last lines of the render log. |
| not blank | no one-colour run longer than 0.5 s before the end hold, and at most 10% blank frames | Check that READY waits for fonts and images (HTML), or that each delayRender has its continueRender (Remotion). A planned black breath before the drop is 3 to 4 frames, so it passes. |
| moves | the mean frame difference before the end hold is at least 0.15 (on a 0 to 255 grey scale) | Add motion: a drift, a push-in, a type move or a light move in every section. |
| no flats | no run of more than 3 unchanged frames before the end hold | Find the time in the report. Give that span a slow drift or a scale of 1 to 2%. A held card still moves. A blank (one-colour) breath does not count here; not blank checks it. |
| end hold | the still frames at the very end last 0.6 to 1.4 s | Change T_END or LEN in tl.py and render again. The end card can animate first; only its last still frames count. |
| master (with --master) | H.264, yuv420p, BT.709 colour tags, and faststart | See the master section. |

The thresholds are options of the script (--flat, --moves, --hold). Change them only when the user asks for a different look, such as a slow ambient loop. Write the change in NOTE.md.

For a seamless loop, also compare the first and the last frame. render(0) and render(LEN) must give the same picture, and the move must keep its speed across the join. A loop has no end hold, so run the gates with --hold 0 0.1 and write that in NOTE.md.

## The master

- The delivery file is H.264, yuv420p, BT.709 and faststart, with AAC sound.
- audio.py muxes the score with libx264, yuv420p and faststart, at -14 LUFS with a true peak at or under -1 dBTP, under its MAX_MB.
- The mux can drop the colour tags. Run `scripts/gates.py` with --master on the muxed file. If only bt709 fails, run it with --retag out/final.mp4. That copies the video with BT.709 tags and faststart and does not encode it again. Then run the gates on out/final.mp4.
- For a vertical copy of a wide film, use the `reel-export` skill on out/final.mp4. Do not re-render the film for it unless the user wants a native vertical layout.
- Keep the frame rate of tl.py. Do not change it in the master.

## The poster

Pick the frame that shows the hero moment or the end card, with readable type. Write it with `scripts/gates.py` and --poster T out/poster.jpg. Look at it before you deliver it.

## NOTE.md

Write NOTE.md in the film folder. Use short lines. It holds:

1. What the film is: length, format, fps, engine (Remotion or HTML) and the version that was delivered.
2. The timeline: BPM, DROP, T_PAY, T_END and LEN from tl.py.
3. The files: out/final.mp4, out/poster.jpg, the source files that make the film, and how to render it again.
4. The words on screen, exactly as they appear.
5. What is real, what is illustrative and what Sloosh made: each file and the shot it fills. No prices and no internal ids.
6. The sound: the synth score, the user's track or a hand-off, and the loudness from the report.
7. The gate results with their numbers (end hold, mean motion, loudness), with any threshold that was changed and why.
8. Rights and licenses: the fonts (OFL license files in fonts/), each of the user's files and its rights, and the Remotion license rule if the film uses Remotion.
9. Open points: what the user should check by eye and by ear, and what the next pass would improve.

## What you tell the user

- Give the paths of out/final.mp4, out/poster.jpg, the film folder and NOTE.md.
- Say which gates passed. Say that the gates check the file, not the film.
- Never say that the film is good, finished or approved. Ask the user to watch it with sound and to say what to change.
