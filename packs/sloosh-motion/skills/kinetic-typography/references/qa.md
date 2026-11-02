# QA checklist and fixes

- One-sentence test: the message reads from the contact sheet alone. Every string matches the approved copy. Every number came from the user.
- One boss per frame, with at least 8:1 scale contrast between the hero and the labels.
- No overlaps: no word on a word, an exiting scene gone before the next one lands, no slivers after wipes, nothing over the plate's face.
- Safe zone: readable copy sits inside it and left of the rail. On 9:16 that keeps it out of the top 14%, the bottom 35% and 6% at each side. Only texture (ticker, grid, ghosts, stretch-to-frame) goes full-bleed.
- Fonts: the glyphs are the specified face, not a fallback. Check Archivo's wide R and Fraunces' ball terminals.
- Beats: every landing sits on its beat (within 1 frame). Fields land on bars. The drop is the loudest frame.
- Holds follow the hold table in `references/story-and-edit.md`. The end card holds at least 2 s.
- Hits and budget: at most 4 hits, 1 drop and 1 fly-through. Grain is on, so there is no banding.
- Generated footage: a plate or plate clip has no text. A morph clip shows only the two code-rendered lines, and every frame passes the full-rate check in `references/start-end-frames.md`.
- Audio: an SFX on every landing word, -14 LUFS, and the user listened.

| What a critical viewer sees | Fix |
|---|---|
| "Template" or "slideshow" | Fill the width (fill, KT.fit), tighten tracking, raise scale contrast, a new field every bar, inversions on two beats |
| "Timid" | Slam-fill and stretch-to-frame for the hero word, a type-as-camera at the drop, an echo walk, punches from the drop |
| Words float or feel mushy | Landings must be on the beat (the 0.07 s lead is built in); exits shorter than entrances; hard-cut phrases on the beat |
| Words collide during a change | The next scene comes in at least 0.25 s after out, or use exit="cut"; swap uses tight masks |
| A line is clipped by the frame or the rail | Never position by hand; set box or y and let the fit and the rail run; check with --boxes |
| Fallback font | new_film.sh copies the fonts into fonts/; the @font-face family name must match .d, and the font must be in KT.boot |
| Accent unreadable on a block | The field row's own accent (the 4th value) must contrast with that bg |
| Muddy dark field | Hazes sit on the home field only; do not add hazes to dark blocks |
| The subject hides the masthead | Prompt the still again (head top at 30%, clean top band) or move the masthead's box |
| Colour banding | Keep GRAIN at 3 to 5 |
