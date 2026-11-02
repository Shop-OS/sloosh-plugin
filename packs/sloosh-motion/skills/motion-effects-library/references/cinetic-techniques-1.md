# Cinetic techniques, part 1 of 2

This part covers these groups: Opening hooks, Transitions, Camera, Typography in motion, UI choreography, Data and numbers, Product demo. Part 2 covers the other groups.

Each technique is one named move for a motion film. The entries are condensed and adapted from the cinetic technique library (MIT). See `THIRD-PARTY-NOTICES.md` in this folder.

## How to read an entry

- Looks like: what the viewer sees.
- Use when: the film or moment it suits.
- Avoid when: where it fails.
- Timing: lengths in frames (f) at 60 fps. 60 f is 1 s. px is pixels on a 1920x1080 frame. Scale the pixel values to the real frame size.
- Made with: the sloosh-motion skill that builds it.

The ease names in the timing lines describe the shape of a move:

- ease-out: fast start, gentle stop. Use it for things that arrive.
- ease-in: gentle start, fast end. Use it for things that leave.
- ease-in-out and smooth ease: gentle at both ends.
- soft ease-out and glide ease: a long, light landing.
- UI ease: a short, crisp move for interface parts.
- contact ease: speeds up into a landing, with a small squash on contact.
- camera ease and dolly ease: slow, weighted camera moves.
- whip ease: a very fast move with a hard stop.
- settle ease: the last small move into rest.
- typing ease: an even rhythm for typed characters.
- linear: constant speed.


## Opening hooks (10)

### Problem pile-up, freeze, turn

- Looks like: The film opens inside the problem: cards, alerts or rows pile in faster and faster while a counter climbs, the picture freezes for a breath of true silence, and the turn hits on the downbeat.
- Use when: Problem-first launches whose pain is volume: notifications, tickets, tabs, invoices.
- Avoid when: The pain is not about quantity, the brand film is calm, or the film already uses its one freeze elsewhere.
- Timing: 14 arrivals in about 100 f (gaps 14, 12, 11, 9.5, 8.4 ... down to 4 f); freeze of 15 f at most; turn on the next downbeat.
- Made with: sloosh-motion-director

### Sparse intro, drop on the first hard cut

- Looks like: (Sound and picture.) The first ~2 s carry only light plucks or a filtered, wide pad under the opening type; the low end and the kick land exactly on the frame where the punchline card or first product shot cuts in.
- Use when: Almost any film that opens on type and then shows the product with a tension-and-release shape.
- Avoid when: Stings under 4 s, openers designed to be loud from frame 0 (live grid, macro scramble), or a drop that cannot land on a whole-frame cut.
- Timing: Intro 117-156 f (1.95-2.6 s); about +14 dB from intro to body; sub 8-12 f before the cut; kick on the cut frame (within 1 f).
- Made with: sloosh-motion-director

### A click starts the film

- Looks like: From frame 0 a cursor is already travelling toward the one button on an otherwise bare stage; it presses, and the button floods open into the first scene.
- Use when: UI walkthroughs and feature films where a single action is the product ('one click to ...').
- Avoid when: Products that act on their own, or films where the cursor never returns after the hook (it breaks continuity).
- Timing: Cursor arrives f18; press f22 (4 f down, 8 f recoil); iris f21-45; first scene live from f45.
- Made with: sloosh-motion-director

### Cursor into a field, two-stage push, typed provocation

- Looks like: A small search pill sits still on a dark stage; a text cursor drifts in, the camera pushes in twice to a macro framing, and a provocative query types into the field before any brand appears.
- Use when: AI, search or command products, or any opener whose hook is a question the product answers.
- Avoid when: The product has no input field, the film's camera grammar is flat, or the query runs past about 40 characters (the macro framing cannot hold it).
- Timing: Camera still for 24 f while the cursor flies in from frame 0 (30 f on glide ease); push 1 42 f (f24-66, peak 0.077 ln k per frame); push 2 44 f (f66-110, peak 0.082 ln k per frame); 7.2x in total over 88 f; typing from about f92 at 30 characters/s, each character at most 40 px wide on screen.
- Made with: sloosh-motion-director

### Cut in mid-sentence, pull back to the line

- Looks like: The film opens inside one giant word, its first letter cropped by the frame edge as if cutting into a thought mid-sentence; after a beat the camera pulls back to reveal the whole sentence at reading size.
- Use when: Copy-led launches built on one charged word, in calm-to-medium films.
- Avoid when: The key word is short or ordinary (the crop will not intrigue), or the film already opens on another zoom-out (icon card, macro number).
- Timing: Settle 12 f; hold 36 f; pull-back 56 f from 3.2x to 1x on dolly ease (peak about 0.032 ln k per frame).
- Made with: sloosh-motion-director

### Finished result first, then rewind

- Looks like: The film opens on the finished end state at its most impressive, holds for a beat, then visibly rewinds every element back to the empty start, where the story begins playing forward.
- Use when: Walkthroughs and feature films whose output is visually rich and readable at a glance.
- Avoid when: An end state that needs explaining, or more than about 30 state changes (the rewind turns to mush).
- Timing: Hold 40 f; rewind 36-48 f on smooth ease (peak about 8x real time, at most about 120 f of build); forward play from the next beat.
- Made with: sloosh-motion-director

### Mark builds, then is thrown into a macro of itself

- Looks like: On frame 1 a dot swells into the brand mark. The mark grows briefly, holds for a breath, then shrinks away faster and faster and hard-cuts at peak speed to a frame-filling macro of the same mark, which keeps pulling back.
- Use when: A brand-first logo sting where recognition must land in under half a second and the energy must pour into the next shot.
- Avoid when: The mark is unfamiliar and needs a longer hold to be learned, or the film already uses a scale-continuity cut elsewhere. Never use it to show the full lockup.
- Timing: Dot to mark 18 f on ease-out (edge about 49 px/f on its first frame); grow 32 f from f8; hold 8 f (f40-48); exit 20 f on ease-in (f48-68), cut at f68 (1.13 s); macro pull-back 24 f through a zoom handoff from about 2.2x.
- Made with: sloosh-motion-director

### Four live cells from frame 2

- Looks like: There is no title. The film opens on a flush 2x2 grid where every cell is already mid-action (a line assembling, a counter ticking, an object orbiting, a pin dropping), so from its first frames the frame reads as one living system.
- Use when: A hero or social loop that must show several features at once, or a launch whose first second has to prove breadth.
- Avoid when: The story needs one idea at a time, a single-message sting, or a 9:16 frame where the cells would shrink below about 540 px wide.
- Timing: First arrivals on f2, f2, f2 and f6 (no cell later than f8). Typical entrances: a type lockup settles in 18 f on ease-out, a counter finishes in 28 f. Loop periods 260 / 462 / 244 / 428 f. Something changes somewhere about every 20 f (longest gap about 62 f). Cells 960x540 at 1080p.
- Made with: sloosh-motion-director

### Macro number scramble, one-frame snap-out

- Looks like: Huge digits fill and overflow the frame, re-rolling every frame. On one frame the view cuts back to the whole figure, which rolls into the final metric and holds: the number is the hook before any brand appears.
- Use when: The strongest proof is one metric (users, hours saved, uptime) and the film earns attention with the outcome before the brand.
- Avoid when: There is no credible or impressive number, or the tone is calm and premium.
- Timing: Macro 29 f; snap 1 f at f29; settle 12 f; final string forced from f41 (0.68 s); hold 72 f with only the scale drift. Ticks at about 0.17, 0.23, 0.31, 0.36 and 0.40 s.
- Made with: sloosh-motion-director

### Oversize line flies through, restarts small

- Looks like: A huge fragment of the headline, about a quarter of frame height, brakes in from the right with its letters fading on as it slows, then dissolves; three frames later the same line restarts small and centred so it can be read.
- Use when: The headline has a thesis word worth previewing big, in a dark, energetic launch.
- Avoid when: Light stages where 65% white loses contrast, or headlines longer than about 5 words whose big fragment will not read. Also avoid it when the big fragment would sit still and cropped at both edges at any point: viewers read an oversized, cropped line that vanishes and then restarts small as a false start, not a preview. It has to travel every frame it is on screen.
- Timing: Big line visible from f0 (its clock t = f + 6) to f35: slide 39 f, about 35 px/f at t = 6 and 17 px/f at t = 12; letters 6 f each, 1.5 f stagger; fade over the last 7 f. No gap; small line from f36, 13 characters in 17 f, drift settled in about 40 f.
- Made with: sloosh-motion-director


## Transitions (22)

### Anchored overlay, background swap

- Looks like: A foreground element (a pin, a status pill, a modal, a big word) keeps its exact screen position while the world behind it hard-cuts, so a total change of scene reads as a change of zoom or context.
- Use when: Showing that one thing persists across contexts: a location going from 3D city to map, a request going from an empty void to the full app, a claim held over a run of photos.
- Avoid when: The overlay is text that must be reread after each swap, or the backgrounds are busy and bright enough to swallow it. Keep backgrounds near 5% mean luma under light overlays.
- Timing: Background holds of 10-22 f each in a montage (2-3 swaps), or a single swap. Overlay offset across the cut: 0 px ideally, 30 px at most. Overlay drift 0.5-1 px/f. Follow-up move 40 f on glide ease. Cuts on beats or 16ths.
- Made with: sloosh-motion-director

### Angle change on a shared drift

- Looks like: A hard cut jumps to a new angle or the next state of the same object (front to top-down, open to closed) while the slow zoom or pan carries on at exactly the same rate, so a calm shot changes viewpoint with no jolt and no speed ramp.
- Use when: Calm films and product beauty shots where a velocity ramp would be too loud: showing an object's second side or its next state within one continuous gesture.
- Avoid when: The two angles look alike (under about 30 deg it reads as a jump cut), the subject's size or position jumps, or one side is static. For a lift in energy, use a velocity handoff instead.
- Timing: Drift 96 f on soft ease-out from 1.10x (or a 2-4 px/f pan). Cut 8-16 f in, at −0.26 to −0.36% scale per frame (about 3 px/f at the frame edge); the drift settles 40-80 f after the cut. Angle change at least 30 deg, centre offset at most 40 px, size change at most 15%. Optional subject action 36-60 f on smooth ease, cut at 35-55% of it. Cut in 0 f.
- Made with: sloosh-motion-director

### Conveyor line swap

- Looks like: The current line floats up and fades, the stage is empty for an instant, and the next line rises from below into the same spot, so a run of statements reads as one upward feed.
- Use when: Sequences of short claims, lists of capabilities, a subject that changes while the predicate stays.
- Avoid when: Lines of very different length or alignment (the eye loses the slot), or more than 4-5 lines in a row without another seam type.
- Timing: Exit: 30 f on ease-in (last frame about 26 px/f, while fading). Gap 2 f. Entry: 30 f on ease-out (first frame about 37 px/f, while faded); colour over 16 f. Per-word stagger 3-4 f. One line per bar or half bar.
- Made with: sloosh-motion-director

### Motion-masked swap

- Looks like: Content changes on exactly the frame something else moves fastest (background rings whipping past, a card kicking into a tilt), so the change hides inside the motion and two states chain in one space with no visible cut.
- Use when: Changing copy inside a continuous environment; cycling examples (photos, prompts, results) in a loop.
- Avoid when: The masking motion is weak (under about 20 px/f at its peak), so the swap shows; or the content is a counter (roll the digits instead).
- Timing: Sweep: 20-24 f on smooth ease, centred on the swap. Kick: attack 2 f, decay tau 3 f, settled in about 8 f. Repeat no faster than every 48-54 f.
- Made with: sloosh-motion-director

### Path relay

- Looks like: A line and its lead dot carry the eye from one place to the next. The connector bends around a rounded corner with the camera following, or continues across a cut and enters the next shot from the same edge at the same angle.
- Use when: Money, data or messages travelling (send, route, sync), flowcharts and timelines, and films whose UI already uses lines and nodes.
- Avoid when: The film has no line language, or the path would cross readable text. A path that loops back reads as indecision.
- Timing: Dot at a constant 8-16 px/f. Corner radius 40 px. Camera lag 8-12 f. One run lasts 60-72 f. After a cut the dot lands 18 f later. Off-frame gap 12 f; re-entry at ≤ 60 px/f, slowing ×0.92 per frame.
- Made with: sloosh-motion-director

### Product surface cover wipe

- Looks like: A product surface (a UI panel, a window, a device) moves in front of the old shot and either passes straight through it with the scene changed behind it, or lands and becomes the new shot.
- Use when: Promise to product: the UI pushes the headline off. Scene changes that should show the product itself rather than a graphic.
- Avoid when: The surface is a plain coloured slab (then it is a preset wipe), or the pass-through would need more than 80 px/f; shorten the distance with a cut instead.
- Timing: Pass-through: about 2600 px at 64-72 px/f, or 36-40 f; the scene switches on the full-cover frame. Land: 940 px over 44 f on glide ease (peak about 64 px/f at 31% of the move); the title fades over 36 f, starting 16 f before. Occluder: covers for 2-4 f at the push's peak.
- Made with: sloosh-motion-director

### Reveal by subtraction

- Looks like: The clutter in front of the hero flies off toward the frame edges or shrinks away, uncovering a hero that was already sitting at its final size behind it.
- Use when: Ending a busy montage on the one stat, card or word. Walkthroughs that change app areas through the product's own window behaviour.
- Avoid when: The hero is not ready behind the clutter (it must never pop in), or the clutter is readable content the viewer has not finished.
- Timing: Scatter: 30 f on contact ease; items clear the frame by about frame 24; stagger 0-2 f; the hero stays static throughout. Window minimize: 40 f on contact ease in log scale (far corner ≤ 75 px/f), fading over the last 6 f; next entrance 4 f later. Staccato: one removal every 5-7 f, final hold 17 f.
- Made with: sloosh-motion-director

### Shape match cut

- Looks like: The hero shape leaves one shot at a known point and size, and the next shot opens on a matching shape (the mark, the flat UI, the real object) on the same point, so the object's identity carries across a change of world.
- Use when: Turning a problem shape into the answer, a device mockup into the bare UI, or a physical object into the mark.
- Avoid when: The silhouettes differ (round against tall), so the match cannot be seen. Use a dot relay or a container morph instead.
- Timing: Cut in 0 f. Centre offset ≤ 20 px. Scale ratio 0.57-1.3x. Incoming settle 18 f on ease-out, with half the change done in about 2 f. Outgoing pre-cut shrink 4 f on ease-in. Hold 12-30 f.
- Made with: morph-shapeshift

### Tip-back exit

- Looks like: The outgoing scene tips away from camera like a sheet laid onto a table, or flips up into a line, speeding up and fading into the next stage colour, and the next element lands on the clean field.
- Use when: Ending a UI section to hand over to a statement or an alert, when the next beat needs an empty stage for big type.
- Avoid when: The next act opens on the same pose (use a relay instead), or the dim would go to black and back up (a dip) instead of into the next stage colour.
- Timing: Tip-back: 30 f on smooth ease (rotateX 40 deg). Flip to a line: 20 f on contact ease. Crop collapse: 24 f on contact ease. Dim overlay 0 → 0.9 over the last 12 f. The next element starts 0-1 f after the exit clears.
- Made with: sloosh-motion-director

### Velocity handoff cut

- Looks like: The outgoing shot speeds up in one direction and is cut on its fastest frame. The next shot opens already moving the same way and brakes to rest, so momentum runs straight through the edit.
- Use when: Most cuts between moving shots: feature-to-feature edits, montages, chapter changes, and any film that must never stop. Velocity-matched cuts are exempt from the two-uses-per-type limit.
- Avoid when: One side has to be still (a held statement or a designed freeze), or the two shots would move in opposite directions. Carry a shape or an anchor across instead.
- Timing: Exit: last 16-24 f on exit ease (speed grows about ×1.1-1.2 per frame), ending at 25-40 px/f (never above 60) or −6 to −8% scale per frame. Entry: 30-55 px/f on frame 0, slowing about ×0.92-0.94 per frame (ease-out over 45-90 f; an entry distance of 40 to 60 px is about 400 px). A 1-3 px/f drift may run under the hold before the ramp. Text inside a moving shot must be under 20 px/f by the time it has to be read.
- Made with: sloosh-motion-director

### Band wipe

- Looks like: A band crosses a region (snapping up, lingering, then whipping off, or sweeping across a chart) and the content changes along its edge: the old state is erased under it and the new state draws in its wake.
- Use when: Swapping a data series, a filter result or a big-type card in place, when a control's tap should visibly cause the change.
- Avoid when: Applied to whole scenes again and again (it becomes a preset wipe), or when the band would cross text the viewer has not finished reading.
- Timing: Sweep: 368 px band at a constant 60-70 px/f (about 27 f across a 1400 px chart), starting 2 f after the cause. Hang-time: 6 f (ease-out) + 20 f (constant speed) + 16 f (contact ease) = 42 f. The new state draws in within 6-10 f after the band passes.
- Made with: animated-chart

### Defocus cut

- Looks like: The outgoing shot throws itself out of focus in a few frames, the film cuts to a shot that is still fully defocused with its content already moving, and the lens snaps sharp as that content settles.
- Use when: Joining two shots with nothing in common (no shared shape, direction or colour), or a deliberate 'look again' beat.
- Avoid when: As the default seam (it turns into a soft crossfade), on shots dominated by small text, or more than twice per film.
- Timing: Out: 6 f on ease-in to 16 px. Cut. Defocused hold 6-12 f at 24 px. Snap 8 f (ease-in) to t = 0.1. Settle 12-20 f (soft ease-out). Incoming card move 20 f on ease-out. About 30-45 f in all.
- Made with: sloosh-motion-director

### Envelope-matched type cut

- Looks like: A big line hard-cuts to a much smaller, longer line whose words start spread apart so it spans exactly the old line's width, then the gaps close while the sideways drift carries on, so the outer edges of the type survive the cut.
- Use when: A big two- or three-word claim hands over to its full sentence or call to action; any big-to-small type change where both lines share a centre or a left edge and the type already drifts sideways.
- Avoid when: B is naturally wider than A (use a blur-swap rescale instead), either line is a single word (there are no gaps, so collapse one word's tracking instead), or the alignment changes across the cut.
- Timing: Cut in 0 f, or 1 ghost frame at 0.6-0.7 incoming. The gaps close over 36 f on soft ease-out, half done by frame 5. The outermost words travel (W_A − W_B)/2: keep that at or under 160 px so their first frame stays under 20 px/f, or fly them at 0.6 opacity for the first 6 f. Shared drift 3-4 px/f, decaying in B over 60 f. Hold B at least 60 f.
- Made with: sloosh-motion-director

### Horizon rise

- Looks like: A huge disc rises from the bottom edge like a planet horizon, its rim washing over the frame, until its dark core swallows the screen and becomes the stage for the next line.
- Use when: A single colour event that divides the film into acts (UI section to brand moment), or a calm lift from a statement into the next card.
- Avoid when: More than once per film, or on a light film where the dark core would be the only dark frame.
- Timing: Rise: 56 f on dolly ease, about 2570 px of centre travel at 1080p (the rim's leading edge peaks near 70 px/f mid-move). Next text from about frame 46. Band version: 16 f on ease-in. The core fills the frame on a downbeat.
- Made with: sloosh-motion-director

### Iris from a glyph

- Looks like: A small dot appears on a word or icon in the current shot and balloons exponentially to swallow the frame, showing the next scene inside it, so the reveal starts from content rather than from nowhere.
- Use when: A word in the copy names what the next scene shows (a benchmark, a feature, a place); dark-to-light or light-to-dark act changes.
- Avoid when: A linear radius (it crawls, then snaps); the same iris more than twice per film; a seed glyph the viewer has not had 6 f to find.
- Timing: Seed in over 6 f, hold 6-10 f. Iris 20 f at a constant ratio (about ×1.25-1.29 per frame, radius in log space). Centre drift 20 f on smooth ease. Optional tonal ramp: 3 steps over 6 f. Funnel variant: 24 f at ×1.18 per frame. The disc fills the frame on the downbeat.
- Made with: sloosh-motion-director

### Polarity flip cut

- Looks like: A hard cut flips the stage between near-black and near-white on a downbeat, often with the same icon or pill held on the same spot in inverted colours, so the luminance jump itself is the accent.
- Use when: Act breaks: problem to answer, public to private, demo to claim. The strongest punctuation on a drop.
- Avoid when: A third time in one film; a flip from a static frame with nothing carried; or when the accent field would be the film's second full-frame accent flood.
- Timing: Cut in 0 f, or 2 ghost frames at 0.12 and 0.94. Anchor scale jump 1.0-2.5x. Post-cut drift 30 f on ease-out. After a flip to dark, wait 12-20 f before any small type. At most one flip per bar and two flip cuts per film.
- Made with: sloosh-motion-director

### Select and retype swap

- Looks like: A finished headline is selected like text in an editor, the highlight holds for a beat, and on one frame the selection is replaced by a caret that types the next line in the same place.
- Use when: Products where text is the medium (editors, prompts, writing and AI tools); correcting a claim, where the assumption is selected and overwritten by the answer; two or three headline swaps that should feel authored.
- Avoid when: The product has nothing to do with text, lines run past about 40 characters (the typing outlasts the read), or the swap repeats more than three times in a row and turns into a typing demo.
- Timing: Selection 2-3 f per word (or a 1 f select-all), hold 10-12 f, replace on 1 f. Line B types at 2 f per character on typing ease (a 20-character line in 40 f), and the caret blinks 30 f on, 30 f off once idle. About 60-75 f in all for a five-word, 20-character pair.
- Made with: sloosh-motion-director

### Stepped column fill

- Looks like: Columns rise from the bottom edge in a stepped pyramid centred under the hero, spreading outward until they close into one solid field that becomes the next stage behind it.
- Use when: Marks built from bars, steps or pixels; data and analytics products, where the columns read as a chart; stings and loop intros that change the stage colour behind a held hero.
- Avoid when: As a general scene change between unrelated shots (it reads as a preset blinds wipe), behind small readable type, or more than once per film.
- Timing: Each column rises over 40 f on smooth ease (tops peak at about 76 px/f at 1080p). Stagger 2 f per column outward from the centre (7 steps for 14-15 columns), about 54 f in all. The field closes on a downbeat and swaps to one flat plate on the same frame. Hero pulse: attack 2 f, tau 5 f.
- Made with: sloosh-motion-director

### Collapse to a dot relay

- Looks like: The hero collapses into one small dot, or the whole world shrinks into it. The dot, the only thing that survives, opens into the next object: a check ring, an avatar, the mark.
- Use when: Submit, send, process, receive: actions that mean 'this went in and came out as that'. Also the film's signature device when the mark contains a dot.
- Avoid when: The dot would blink out or change size or colour at the seam, or the film already has an implosion seam.
- Timing: Collapse: 4 f (ease-in, into a cut) or 16 f (ease-out, snap and hold). World shrink: 24 f on contact ease for a dot near centre (edges ≤ 66 px/f), or 40 f for a dot near a corner, starting 15 f after the collapse. Reopen over 8-12 f. Any device rotation that follows settles over 28 f on ease-out.
- Made with: sloosh-motion-director

### Giant word punch-out

- Looks like: A hard cut lands on an extreme close-up of an oversized word sliding fast and braking, its letters resolving one by one. A second cut jumps out to the whole word at reading size, arriving with wide tracking that slams together.
- Use when: A one-word claim or product name that deserves two beats: read it, then see it whole. Vertical cut-downs where one huge word fills the frame.
- Avoid when: Lines of more than two words, or words over about 10 letters (the close-up loses the word); or when the next shot needs the word small within a second.
- Timing: Close-up 18-22 f: starts at ≤ 70 px/f and slows ×0.92 per frame (about 18 px/f by frame 16); letters resolve over 12 f with a 2 f stagger from frame 4. Cut at 13-20 px/f residual speed. Wide entry 30 f on ease-out: scale 1.38 → 1, tracking 0.8 em → rest, horizontal blur of 18 px gone by 60% of the move, outer letters ≤ 60 px/f. Colour settles in 17 f. Hold 30-60 f. Exit 6-12 f on ease-in.
- Made with: sloosh-motion-director

### Portal zoom with aspect morph

- Looks like: A window opens in the middle of a solid tile. Tile and window grow faster and faster while the square stretches to 16:9, until the window's interior is the next scene and the tile's border has flown off the edges.
- Use when: The film's energy peak and act break, going inside the product, when the mark or app icon is a tile.
- Avoid when: The accent has already flooded the frame once (the tile border is a brief accent flood), or another zoom-through sits in the same act.
- Timing: Lead-in: converge 22 f, cube turn 12 f, blank hold 6 f. Portal: 39 f at ×1.084 per frame (border gone by about frame 30, inner window edges ≤ 78 px/f). Aspect 1 → 1.78 over the first 30 f. Next-scene labels start from about frame 30 on a 4-6 f stagger.
- Made with: morph-shapeshift

### Scale-through cut

- Looks like: An object shrinks faster and faster toward a fixed point, the film cuts, and a matching object appears much larger on the same point and keeps shrinking as it brakes, so one pull-back runs through two different worlds. The mirror version swells into the cut and opens on an undersized object that grows.
- Use when: Changing medium or world while keeping the subject: 3D to flat, device to UI, brand card to product, a mark coming back as a macro. Also hero pull-backs at act changes.
- Avoid when: The two objects cannot share a centre point, or both sides are calm; a scale jump without matched scale velocity reads as a jump cut. Use it at most twice per film.
- Timing: Exit: 16-24 f on ease-in to 0.70-0.80 (last frame −7 to −9% per frame). Cut on a downbeat. Entry: 1.7-2.0x → 1 over 30-40 f on ease-out (first frame −8 to −9%), or an 8-9x macro shrinking toward rest ×0.84 per frame and settled by about 30 f. Anchor drift ≤ 30 px. Push variant: +20-25% over 16-24 f, then 0.8 → 1 over 30 f.
- Made with: sloosh-motion-director


## Camera (22)

### Breathing zoom between interactions

- Looks like: After a reveal the camera slowly pulls back, coasts through a stop and turns smoothly into a slow push that lands on the next interaction, so the frame breathes across a whole act.
- Use when: Dashboard, analytics or table acts of 4-10 s with several interactions in one framing, where cutting would cost orientation.
- Avoid when: Shots shorter than about 90 f, acts that already move pose to pose with big pushes, or a scrolling feed (a zoom on a moving list reads as wobble).
- Timing: Pull after a reveal: -0.25%/f falling to 0 over 72 f (about -9% total). Push into the next interaction: 0 rising to +0.14%/f over 36 f, about +6% within 60 f of the zero crossing; table and list acts run +0.03 to +0.17%/f (about +6.6% total). Rate keyframes 36-90 f apart, linear. Exhale x0.94 over 60 f on ease-out.
- Made with: saas-product-video

### Detail first, then pull back

- Looks like: A shot opens tight on the one thing that matters (giant prompt words, a chart counting up, a status pill) with no chrome, then the camera pulls back to show it sitting in the full window.
- Use when: Result reveals, analytics, prompts and input moments where the value should land before the load of the full UI; breaking up a repeated card formula; re-establishing the whole product after a run of close details.
- Avoid when: The product hasn't been seen yet and the tight frame stays unrecognisable for long (keep the tight hold under 52 f), or the wider frame adds nothing new.
- Timing: Tight hold 24-52 f while the value animates. Pull k 1.6-1.7 -> 1.0 over 52 f on camera ease (peak about 4%/f at 27%), or a settle back over 56-80 f on ease-out (half done by f10-12). Edge tiles out over 16 f before the pull, context in over 30 f, 3D tip peaking mid-move. Re-establish k 2.2 -> 1.0 with focus over 60 f on camera ease (peak about 5.6%/f).
- Made with: animated-chart

### Fit-to-content follow

- Looks like: As a route, graph or plan builds, the camera widens just enough to keep every piece that matters in frame, so the shot opens close on the first node and ends on the whole structure.
- Use when: Pipelines, agent plans, org charts, dependency or network graphs and routes that build piece by piece, where the first node needs close-up legibility and the payoff is the whole shape.
- Avoid when: The finished structure already fits one comfortable framing, a single moving lead is the whole story ("follow the lead dot"), or the full structure cannot fit with 24 px labels (split it into chapters with cuts instead).
- Timing: Follow coefficient 0.06-0.08 per frame (time constant 12-16 f); zoom at most 1.2%/f, centre at most 12 px/f on screen (--blur if the corners ever pass 12 px/f). Margin 12% of the frame, 18% lead on the head's side. Nodes 20-40 f apart give a steady widening rather than steps. Closing punch-in 48-60 f on camera ease, or a hold with a -0.08%/f pull.
- Made with: saas-product-video

### Follow the lead dot

- Looks like: A small lead (a progress dot, a travelling packet, a drawing line's head) moves through the layout and the camera follows it with a soft lag, never quite stopping, so the viewer always knows where to look.
- Use when: Agent progress, pipelines, timelines and journeys across a map: any story told by one thing moving through a layout.
- Avoid when: The lead moves faster than about 20 px/f for long stretches (the lag lets it escape the frame), or the whole layout fits in one framing.
- Timing: Lag coefficient 0.08 per frame (time constant about 12 f). Peak 12.5 px/f, residual drift 2-2.5 px/f, never 0. Step rows reveal over 12 f as the lead passes. Bumps between steps about 40 f.
- Made with: saas-product-video

### Isolating push into one item

- Looks like: The camera pushes into one row, card or column while everything around it fades, dims or slides off the edges, picking a single thread out of a busy layout.
- Use when: Choosing one result from a list of parallel processes, moving from a typographic act into a UI close-up without a cut, or steering the eye to where the next action will happen.
- Avoid when: The item is still too small to read at 4x, or the surrounding layout carries information the viewer still needs.
- Timing: Dive 80 f, x4 on smooth ease (peak about 5%/f), sibling fades 20 f, swap on the last frame. Accelerate-through 60 f, x1.25 on ease-in, surround fade 16 f. Eject 30 f, x1.48 on smooth ease, then +4% over 60 f. Focus pull 18 f, x1.06, blur 8 px, opacity 0.6, running straight into the next move.
- Made with: saas-product-video

### Layered parallax truck

- Looks like: The camera trucks sideways across a scene split into two or three depth planes: the background barely moves, the subject moves with the camera and a near element slides past faster, so a flat layout reads as space.
- Use when: Hero product shots and feature cards that need depth without 3D, and slow establishing moves.
- Avoid when: Dense UI walkthroughs where the eye has to track one control, or any scene with more than three planes (it starts to look like a parallax demo).
- Timing: Truck 200-400 px over 90-120 f on camera ease (subject peak about 12 px/f for 300 px over 105 f), or a 1-3 px/f drift. Plane factors 0.3 / 1.0 / 1.6. Background overscan 5-8%.
- Made with: saas-product-video

### Living hold creep

- Looks like: Under every hold the frame keeps a barely visible push, pull or sideways drift, so no shot sits dead while the viewer reads.
- Use when: Any hold longer than about 30 f: reading a caption, watching a counter, a UI state sitting after an action, the end card.
- Avoid when: A designed freeze of at most 15 f on a silence, or a shot where a big camera move or a travelling cursor already supplies the life. Never stack a creep on top of a punch-in drift on the same axis.
- Timing: Scale creep 0.04-0.07%/f (+2.4 to +4.2%/s), at most 0.1%/f in a 40-60 f tail after a big push. Pulls about -0.08%/f. End card 0.0125%/f. Lateral drift 0.3-0.5 px/f for UI and cards, 1.5-3 px/f for big display type. linear once at speed, with a 20 f exponential ease-in from a seam. Released over the next move's own ease.
- Made with: saas-product-video

### Pull-back that lands an event

- Looks like: A long, gentle pull-back runs from a close-up to the full view, and as it decelerates the next UI event (a modal, labels, a caption) starts, so it lands together with the camera's settle.
- Use when: Walkthroughs and single-take films that move pose to pose, and any long move whose ending would otherwise be a dead beat.
- Avoid when: Short or fast moves under 50 f, where an event in the tail just competes with the motion, and the finale, where the lockup needs a clean frame.
- Timing: 108 f on smooth ease, zoom x0.56, peak about 1.5%/f (about 24 px/f) mid-move. Event starts at 72% of the move; the a firm spring modal settles within 4 f of the camera. Captions start in the last 25% of the move or up to 6 f after it.
- Made with: saas-product-video

### Punch-in insert on the same render

- Looks like: A hard cut jumps from the wide view to a 2-2.5x on-axis close-up, or to a 3-4.5x macro of the exact control being used, while every animation keeps running, then cuts back out.
- Use when: Small UI actions that need hero weight (send, picking a date, a chip), long walkthroughs that need their visual scale reset, and a wide/close rhythm that keeps both context and legibility.
- Avoid when: The UI doesn't hold up at 3-4.5x, or the close-up isn't obviously the same place (keep the cut on-axis or anchored to the cursor, or it reads as a jump).
- Timing: Wide holds 20-64 f before an on-axis punch (90-220 f when it establishes the scene). On-axis close-up about 60 f. Macro insert 46-74 f, up to 76-154 f when it carries an action. Scale 2.0-2.5 on-axis, 3-4.5 macro. Drift inside the insert 1-2 px/f linear (3-5 px/f for a 2.5x component slide). Cut on the click, keystroke or beat, with no transition frames. Chain 2-3 punches on consecutive beats for a staccato build.
- Made with: saas-product-video

### Reactive reframe

- Looks like: When something new appears (a popover, a result, the hero icon), the camera glides a few hundred pixels and pushes in slightly until it sits where the eye wants it.
- Use when: After any UI event that changes what matters on screen, or after a punch-in that left the hero off-centre.
- Avoid when: Every small UI change (keep it for the ones that matter), or an element that already appears near frame centre (a move under 40 px reads as a twitch).
- Timing: Popover reframe: starts 4 f after the pop, settles in 20-40 f on glide ease, k x1.05. Hero centring: 22 f on glide ease, 150-350 px of travel, peak about 22 px/f at 31% of the move, k 1.0 -> 1.23.
- Made with: saas-product-video

### Seamless loop drift

- Looks like: In a looping clip the camera drifts along a slow, closed figure-eight (a little sideways, a little up, breathing in and out) and returns exactly to its first frame, so the loop has no seam.
- Use when: Feature loops, background clips and vertical loops that replay endlessly.
- Avoid when: Linear films with cuts (use a living hold instead), or loops shorter than about 4 s, where the drift turns into a visible wobble.
- Timing: Loop L = 240-480 f. Amplitudes 24-40 px sideways and 10-16 px vertically (at twice the frequency), zoom +-3%, yaw +-3 deg. Peak speed about 0.5-0.8 px/f.
- Made with: saas-product-video

### Zoom-out hop between areas

- Looks like: To travel between two distant parts of one product, the camera eases back as it sets off, crosses at a wider framing that shows where it is going, and pushes back in as it arrives.
- Use when: Single-take and walkthrough films moving between two areas of one surface more than about a frame width apart (sidebar to board, one dashboard panel to another), where the viewer should see how they relate.
- Avoid when: Areas less than about a frame width apart ("reactive reframe"), a cursor that should lead the move ("cursor-led whip orbit"), or a wide view that is cluttered or unfinished, since the hop shows it.
- Timing: Pan on smooth ease over N = k x D / 34 f at depth 0.45, or k x D / 25 at 0.15-0.25: about 76 f for 2,600 px at k = 1, 106 f for 1,800 px at k = 2, 72 f for 1,800 px at k = 1. Dip on linear time, depth 0.15-0.45, its zoom rate peaking at 1-2.6%/f a quarter of the way in and out. Frame edge at most about 60 px/f. Beyond about 120 f, cut instead ("off-frame whip relay" or "punch-in insert on the same render").
- Made with: saas-product-video

### Crane down with a delayed push

- Looks like: The camera tilts down the page past the chart to the detail cards while a slow push-in builds behind it, as if the operator were leaning in to read.
- Use when: Moving down a long page or dashboard from the overview to the detail that matters.
- Avoid when: Pages too short to travel 500 px or more, or vertical formats where the push crops the column.
- Timing: Main tilt 64 f on smooth ease, about 240 px, peak about 10 px/f mid-move. Drift 300 px from a + 40 to a + 220 on settle ease (peaks near 5.8 px/f, under 0.5 px/f by the end). Push +22% from a + 40 to a + 240 on settle ease, peak about +0.35%/f near a + 98.
- Made with: animated-chart

### Cursor-led whip orbit

- Looks like: Following a cursor that leads the way to the next panel, the camera swings fast across the product, yawing to show the slab's thick edge and rolling slightly.
- Use when: Moving between two distant panels of one product in a single-take or walkthrough film, where a cut would lose the spatial relationship.
- Avoid when: There is no cursor or other lead to motivate it (an unmotivated whip reads as a flourish), or the act already uses yaw for something else.
- Timing: 74 f on whip ease, peak about 47 px/f at around 40% of the move. Yaw 0 -> 24 deg, roll 0 -> -10 deg, zoom x0.77. The cursor leads by 4-6 f.
- Made with: saas-product-video

### Directional impact kick

- Looks like: On a true impact (a card landing, a lock-in, a slam) the whole frame jolts a few pixels in the direction of the hit and pushes a hair closer, then settles within a fifth of a second.
- Use when: True landings and lock-ins: a heavy object slamming into a slot, or a statement locking together on a hit.
- Avoid when: Every beat or tick (that makes a shake, not a hit), soft UI arrivals, or mid camera move (it fights the move's ease).
- Timing: Jolt 6-10 px, attack 1 f, tau 4 f (gone in about 25 f). Push +1.5%, attack 2 f, tau 5 f. At most 2-3 per film.
- Made with: saas-product-video

### Extrude then crash in

- Looks like: An object grows toward camera (a disc extruding into a tall cylinder) and the camera slams into it, hard-cutting to its interior while still rushing forward.
- Use when: A violent spatial jump into the product at the energy peak of a launch film or sting.
- Avoid when: Calm films, any second use in the same film, and readable text on either side of the cut.
- Timing: Extrusion 12 f on ease-in. Camera push 24 f on a cubic ease-in, x1.9, reaching about 8%/f (about 77 px/f at the frame edge) on the cut frame. Interior entry x1.76 -> rest over 40 f on soft ease-out.
- Made with: saas-product-video

### Push-in with a roll swing

- Looks like: The camera dives into one corner of the UI, rolls a few degrees off level mid-dive like a hand-steered move, and rolls back to level as it lands.
- Use when: A push that would otherwise feel mechanical: diving into a settings corner, a sidebar or a detail panel.
- Avoid when: Next to another rolled or tilted move in the same act (one rotation axis per act), or on moves shorter than 40 f, where the roll reads as a wobble.
- Timing: 60 f; zoom 1 -> 2.09 on smooth ease in log space, peak about 3.5%/f mid-move. Roll 0 -> -4 deg by 57% of the move, back to -0.3 deg at the end, each segment smooth ease. Optional pitch 0 -> 8 deg over the last 24 f.
- Made with: saas-product-video

### Dolly surge with a foreground pass

- Looks like: The camera surges from a wide shot into a 3x medium close-up, with most of the travel in half a second, and at the fastest moment a near object rushes past the lens before a long, slow creep.
- Use when: Opening a launch film into a 3D or layered world, or a sting that dives from an overview into the hero object.
- Avoid when: Flat UI with no depth layers (nothing to pass the lens), or calm walkthroughs.
- Timing: Push 67 f on smooth ease, zoom 1 -> 3.1, 10-90% of the travel in about 28 f, peak about 4.8%/f near a + 33. Creep +4% over 60 f on linear from a + 47. Foreground exits on the peak at 60-80 px/f or less, smeared by the blur pass.
- Made with: saas-product-video

### Fly-through of a depth field

- Looks like: Dozens of flat screens or tokens float at different depths and the camera travels forward through them: near ones swell and slide off the frame edges, far ones barely drift, until the move lands square on one hero screen.
- Use when: Proving breadth (a whole platform, hundreds of templates, every integration) in 3-4 s without explaining any single screen; opening into a layered world; arriving on the one screen the next act is about.
- Avoid when: Items must be read in flight, there are fewer than about 15 of them (the field looks sparse), the film is flat with no depth language, or "swarm, cluster and burst reveal" already spends the film's breadth crescendo.
- Timing: Dive: 150-180 f on camera ease through 4,000 px of depth (Zh = 5200, F = 1200), landing the hero at scale 1 on the long settle. Drift: pull-back 40 f on ease-out, cruise 90-120 f, exit ramp 18-24 f. Speed gate between 50 and 70 px/f; far fade over 1,200 px of depth; about 12-16 items on screen at once. The hero's copy starts once it moves under 20 px/f.
- Made with: saas-product-video

### Hero push with a 3D turn

- Looks like: From a wide view of the whole app, one continuous move pushes 2.5x into a single panel while yawing, so the panel turns toward the viewer and an empty side of the frame opens for the caption.
- Use when: The film's energy peak: the one feature that needs both spatial orientation and close-up legibility, or a scene change inside a single-take film.
- Avoid when: More than once per film, or on a lone card with no surrounding app (the turn needs a world to orient against). Keep each act on its own rotation axis.
- Timing: 60 f on smooth ease, 10-90% of progress between 29% and 71% of the move, peak about 4.5%/f scale (around 47 px/f on screen) at 50%. Zoom 1 -> 2.56; yaw 0 -> 24-30 deg and pitch 0 -> 5 deg on the same curve. Caption starts at 75% of the move. Hold breath +2.5%.
- Made with: saas-product-video

### Off-frame whip relay

- Looks like: The cursor accelerates up and out of frame, the camera whips down the product while it's hidden, and the cursor re-enters from the top as a fast streak that brakes onto its target.
- Use when: A big spatial jump within one product (top bar to bottom bar, one page to another) that should feel like a match-on-action without a cut.
- Avoid when: Films without a cursor, or destinations less than about one frame height away (a plain reframe is enough).
- Timing: Cursor exit 24 f on ease-in (2.5 -> 15 px/f). Off screen 12 f. Camera 34-54 f on smooth ease centred on the hidden window, peak 60-75 px/f. Cursor re-enters at about 63 px/f and brakes over 36 f on ease-out (speed ratio about 0.92 per frame).
- Made with: saas-product-video

### Pull out from inside the object

- Looks like: The shot opens on what reads as a full-bleed colour field or a statement card, and one long pull reveals it was the face of a small object (an app icon, a card, a screen, the mark) sitting among its neighbours.
- Use when: Cold opens and hooks where a calm statement or a colour field should turn out to be part of the product (the question was printed on the app icon, the colour was one card in the grid); landing the mark into the final lockup; any reveal whose point is scale.
- Avoid when: The face is a photo or bitmap (it falls apart at 8-14x), the context it lands in is not recognisable at a glance, or a scale-through cut or detail-first pull-back has already used the same object. Once per film.
- Timing: Face hold 24-48 f for the read, with a 0.04-0.07%/f creep. Pull from k0 = 8-14 to 1 over N = 25.7 x ln(k0) frames on dolly ease (about 53 f from 8x, 66 f from 13.3x), log rate peaking near 6%/f mid-move and landing at rest. Copy scale tracks k ** 0.46 and fades over the 8-14 f in which the object's width passes 1.3x -> 1.0x the copy width. Anchor travel to the slot under 10 px/f. --blur for frames above 12 px/f.
- Made with: saas-product-video


## Typography in motion (25)

### Animated line re-break

- Looks like: A centred one-line statement re-breaks into a two-line stack, or back, with every word gliding from its old slot to its new one, so the layout changes without a cut or a jump.
- Use when: An inserted icon or a longer word makes a centred line too wide. A headline must stack to free half the frame for a product shot. Returning a stacked headline to a single line for the payoff.
- Avoid when: Lines over about 7 words. Re-breaks that carry the hero word far from where it was being read (keep it as the still anchor). More than one re-break per statement. Vertical formats, where a stack is already the default layout.
- Timing: Per word, D = 0.15 x travel, clamped to 30-48 f, on glide ease (peak about 20 px/f, near 30% of the move). y leads x by 4 f on soft ease-out through arrive. Stagger 2 f in the reading order of the new layout. Travel at most 320 px. Starts 6 f after a causing insert. Settled drift 0.3 px/f.
- Made with: kinetic-typography

### Blur-swap rescale

- Looks like: A big word blurs out and instantly re-forms smaller as the start of the full line, so the type changes scale without a rubbery size tween.
- Use when: Going from one or two giant words to the full readable sentence; right after "giant word punch-out"; any big-to-small type handoff inside one continuous take.
- Avoid when: As a default between unrelated lines (it is not a crossfade substitute); small-to-small swaps; overlaps longer than 10 f, which read as a dissolve.
- Timing: Old out 6 f (ease-in, blurOut 12 px); new in 14 f from +2 f (ease-out, blurIn 12 px, scale 1.25 -> 1, edges of a 1000 px line about 51 px/f on frame 1); 4 f overlap; typical cap-height change -35%; tracking collapse 16 f ease-out.
- Made with: kinetic-typography

### Blur-to-focus word rise

- Looks like: Words materialise one per beat out of a soft blur, rising a few pixels and darkening to full ink as they sharpen.
- Use when: Calm, premium statements that keep pace with a voice-over or a slow bed; the opening line of a quiet film; light grounds.
- Avoid when: High-energy acts or dense beats (the stagger is too slow); pale type on a pale ground (under 4.5:1); any blur left on readable text for more than 6 f.
- Timing: Per word 28 f ease-out; opacity 8 f; blur 8 -> 0 px, clear by frame 4; rise 13 px at 120 px type (peak about 3 px/f); stagger 20-22 f (one word per beat at 160-180 BPM); line drift 0.5 px/f.
- Made with: kinetic-typography

### Centre-out line unmask

- Looks like: A short line opens from its own centre outward behind a soft-edged mask while the letters stay perfectly still, so a result or status reads as unveiled rather than flown in.
- Use when: A result, status or confirmation line under a centred icon ('Published', 'Connected'). A hero word inside a pill that has just formed. A calm sub-line under a headline that has already landed.
- Avoid when: Lines over about 40 characters (the edges take too long to reach the ends). Left-aligned layouts (wipe from the left edge instead). Text that is also moving, where the mask fights the glyph motion. Headlines that need energy.
- Timing: Unmask over 18 f on ease-out (31% of each half-width opens on frame 1), with a 20 px feather. Opacity 0.6 -> 1 and tracking +0.04 em -> token over the same 18 f. Starts 4-6 f after the icon lands; a second line follows at +6 f. Hold at least 36 f + 6 f per word, drifting at most 0.3 px/f. Exit over 12 f on smooth ease.
- Made with: kinetic-typography

### In-place word light-up on beats

- Looks like: The finished line is laid out from the start and its words light up in place, chunk by chunk on the beat, with the last word held back.
- Use when: Titles and walkthrough captions over a moving camera; lines with an inline glyph or partner wordmark that must not shift; music-led films where each chunk can sit on a beat.
- Avoid when: High-energy acts that need motion in the type itself; lines over 6 words (it turns into a slide).
- Timing: Attack 5 f to 0.75, tail 40 f soft ease-out to 1; 6 f within a chunk, chunks on beats; last token +24-34 f; connectors 0.55 -> 1 over 12 f; title stagger 24 f shrinking to 5-6 f; exit all words together over 26 f smooth ease. If the camera is locked, add a 0.3 px/f line drift.
- Made with: kinetic-typography

### Masked baseline rise

- Looks like: Each word rises out of an invisible line at its own baseline, tops of the glyphs first, as if cut out of the layout.
- Use when: Editorial headlines and in-UI headings that must land fast (a 3-word line in under 0.5 s) without stealing focus; titles that build while the plane or camera is still moving.
- Avoid when: Tight leading where the mask would clip the line above; a calm voice-paced read (use "blur-to-focus word rise"); per-letter runs on anything but one short hero word.
- Timing: Per word 12 f ease-out (10-14 f), travel 110% of the line box (about 132 px at 120 px type): 57, 34, 18 px/f on frames 1-3; opacity 3 f; stagger 6 f (4-10); per letter 3 f stagger; letter drop 0.25 em over 8 f, 4 f apart; mask exit 10 f ease-in.
- Made with: kinetic-typography

### Re-centring line build

- Looks like: Words or typed glyphs join a centred line one at a time while the whole line glides sideways so it is centred on every frame.
- Use when: Speaking-pace builds, stat rows that widen as words arrive, centred typed headlines, any line whose final width is unknown while it builds.
- Avoid when: Shifts over about 280 px per word (split the line instead); left-aligned layouts; a line that must keep an anchored element still (use "in-place word light-up on beats").
- Timing: A new word every 26-36 f (0.43-0.6 s); a firm spring re-centre (peak about 7% of the shift per frame, 97% by 27 f), so shifts up to 280 px stay under 20 px/f; word drop 18 f ease-out; pre-solved: 1.3 f per character, 5 f fade, 90 px glide over 24 f ease-out; residual drift 0.3 px/f.
- Made with: kinetic-typography

### Reading-order word exit

- Looks like: Words leave one by one in reading order, each lifting a few pixels and vanishing, until only the hero element is left on screen.
- Use when: Isolating a hero word or object before a match cut or zoom; clearing a statement gently before a calmer UI moment; mirroring a word-by-word entry.
- Avoid when: Walkthrough captions just before a camera move: fade the whole caption at once over 26 f on smooth ease and finish 0-56 f before the move starts; exits that would hurry a payoff line.
- Timing: Per word 10 f, lift 0.12 em (about 14 px), stagger 4 f (2-6), a 5-word line clears in about 26 f; loosen variant 20 f per word, 6 f apart, about 32-44 f in all.
- Made with: kinetic-typography

### Staggered word roll

- Looks like: The words of a phrase roll up and away one after another while their replacements rise in from below, so one sentence mutates instead of cutting.
- Use when: Swapping one claim for the next in place; a URL replacing a tagline; a category word turning into the product name; a closing bookend that rolls the opening phrase into the brand line.
- Avoid when: Swaps where nothing persists (a cut or "blur-swap rescale" reads cleaner); more than two rolls in a row without a different move between them.
- Timing: Out 12 f ease-in, 0.2 em up; in 24 f ease-out from +0.25 em (peak about 7 px/f at 120 px type), 4 f overlap; stagger 6-11 f per word; a phrase swap takes about 50 f; a whole-line conveyor variant leaves exactly 1 empty frame between the lines.
- Made with: kinetic-typography

### Time-boxed eased type-on

- Looks like: Text types in with most of the line appearing in the first few frames, and every line, short or long, finishes in the same musical length.
- Use when: Prompts, search queries and names typed into the product; UI labels appearing while the camera trucks; keeping a run of typed beats on one musical length.
- Avoid when: Statements nobody would type; keystroke clicks on every glyph (let the music carry it); letter-by-letter reveals of a name whose prefixes spell another word.
- Timing: Box 68 f per line whatever its length (26-32 f for a headline under 22 characters, 84 f for giant type); ease-out count; mono labels linear 22-45 cps; caret blink 30/30 f after completion; caret-follow 8 f per character, head mask 25%; retype: 6 f accent, 1 f swap, 26 f retype. Hold at least 36 f + 6 f per word after the last glyph.
- Made with: kinetic-typography

### Vertical word stack

- Looks like: In a tall frame each new word lands on its own line under the last while the stack rises one line, so the newest word always sits on the optical centre.
- Use when: Vertical cut-downs where a horizontal line would be too small; speaking-pace statements on a phone-sized frame; one word per beat.
- Avoid when: 16:9 masters (use "re-centring line build"); statements over 6 words; stacking two separate statements.
- Timing: A word every 24-30 f; word rise 18 f ease-out; stack step a firm spring (97% in 27 f); at most 3 lines visible; final hold at least 36 f + 6 f per word with a 0.3 px/f drift.
- Made with: kinetic-typography

### Words spill out from behind a mark

- Looks like: A glyph or icon slides aside and the words shoot out from behind it, clipped at its edge, as if the mark were delivering the message.
- Use when: An icon-led claim mid-film, or an opening line pushed out by the mark already in motion; a feature icon that introduces its own line; a mark or number that says the sentence.
- Avoid when: The end lockup (it appears once and belongs to the end card); marks smaller than the cap height (nothing to hide behind); spills longer than about 360 px.
- Timing: Mark 260 px over 20 f ease-out (peak about 73 px/f, blurred master); words 320 px over 24 f ease-out (76 px/f on frame 1, under 20 by frame 6), 1 f after the mark; opacity 6 f; hold at least 54 f with a drift.
- Made with: kinetic-typography

### Hard-step edits that act out the copy

- Looks like: The headline does what it says with one-frame edits: broken words click straight one at a time, or words delete from the end faster and faster.
- Use when: Copy about fixing, undoing, cleaning up or simplifying; a deadpan joke beat; a problem line that should visibly go away.
- Avoid when: Copy the motion would contradict; calm films; more than one per film.
- Timing: Snap 1 f, no tween; fix intervals 20 then 14 f; delete intervals 10/5/5/2 f; broken-state drift 0.5 px/f; click within 1 f of each step; hold the fixed line at least 42 f.
- Made with: kinetic-typography

### Multi-direction slam assembly

- Looks like: Each word of a short sentence flies in from a different side, oversized and streaked, and the sentence assembles on one baseline almost at once.
- Use when: Re-spiking energy after a calm, read-paced card; a payoff line that needs a burst; 3-5 short words.
- Avoid when: Long words that would cross each other in flight; straight after another high-energy type move; calm films.
- Timing: Per word 20 f ease-out, 220 px travel (62, 47, 33, 23, 16 px/f on frames 1-5), scale 1.4 -> 1, opacity 5 f; delays 0/4/10/12/16 f; each word readable from about frame 5, the whole line resolved in about 36 f; then 1 -> 0.99 over 60 f.
- Made with: kinetic-typography

### Scaled-echo extrusion

- Looks like: A hero title carries two or three faint copies scaled out behind it, a short depth extrusion that compresses as the title lands and then holds.
- Use when: A product name or a hero title of one to three words that needs weight in a flat sans. A giant cropped word that needs physical depth. A title card between two energetic acts.
- Avoid when: Body copy or lines over 3 words (the copies tangle inside the counters). Low-contrast stages, where the copies turn to haze. Blur, glow, bevels or drop shadows on the copies. A film that already uses the motion-trail echo of the word slams: pick one echo device.
- Timing: Converge over 22 f on ease-out (step 0.03 -> 0.012; outer copy edges stay under 7 px/f on a 500 px title). Copy opacity 0.55 / 0.35 / 0.2. Hold the whole card (36-60 f) with a vanishing-point slide of about 40 px on linear and a line drift of 0.3 px/f. The solid-block variant uses 8-12 one-pixel steps that do not animate relative to the face; the card still drifts at 0.3 px/f.
- Made with: kinetic-typography

### Scramble decode

- Looks like: A string of random glyphs locks into the real text from left to right, or real letters roll through the alphabet into gibberish and back.
- Use when: Keys, codes, private or encrypted values, numbers resolving, a short technical name in a feature beat.
- Avoid when: Prose statements (it delays reading); the brand name in the end lockup; glints or sparkles on the glyphs.
- Timing: One lock every 5 f (about 48 f for a 10-character string); unlocked glyphs change every 2 f; accent decay 12 f ease-out; code roll 1 step per frame, 4-8 steps per letter.
- Made with: kinetic-typography

### Shared-letter morph

- Looks like: One word turns into another: the letters both words share stay and slide into place while the new letters tumble in and click upright.
- Use when: Two words that share letters and whose relationship is the point (before and after, problem and product); one memorable word turn per film.
- Avoid when: Fewer than 2 shared letters; words longer than about 8 letters; fast films where 60 f of letter flight is too slow.
- Timing: Space collapse 8 f; old glyph fade 6 f; each new glyph 24 f ease-out (about 45 px/f on frame 1), opacity 12 f; starts spread over 56 f; hold at least 36 f after the last glyph settles.
- Made with: morph-shapeshift

### Slice glitch into a speed streak

- Looks like: A word jolts into sideways-displaced horizontal slices for two frames, then stretches into a solid capsule that races off as a streak, and the next word lands in its wake.
- Use when: A speed or performance claim, where the word itself turns into motion. Handing a name off to a thread, packet or line that carries into the next scene. The 2 f slice alone on 'private', 'encrypted' or 'blocked'.
- Avoid when: Calm films. More than once per film. Words wider than about 450 px at the smear, where the edge would pass 80 px/f. Long lines. Coloured fringes or a tint shift along the trail.
- Timing: Slice: 2 f via fd, clean on frame 3. Smear: 18 f on contact ease, scaleX 1 -> 1.8; for a word up to 450 px wide the right edge ends near 70 px/f. Text-to-capsule crossfade over the last 10 f. The streak cruises at that speed and clears a 1920 frame in about 15 f, with a tail of at most 240 px. Next word: 320 px over 24 f on soft ease-out from e + 4 (58 px/f on frame 1, under 20 px/f from frame 7), opacity over 8 f. Hold it at least 54 f.
- Made with: glitch-fx

### Slice-band glyph assembly

- Looks like: Each letter builds up from thin horizontal slices that slide in from slightly different offsets at slightly different moments, faint and pale at first, until the word locks solid.
- Use when: A product or feature name that should feel assembled or digital. A name set beside a modular or pixel mark, including the one end-lockup build when the film bookends with it. A short title after a quiet beat.
- Avoid when: Lines over about 3 words, or type under 48 px (bands thinner than 3 px alias into noise). Prose. Delay spreads wide enough that the half-built word reads as broken for more than about 30 f. A film that already has a scramble decode.
- Timing: Each band takes 20 f on ease-out, with opacity over 8 f on linear and colour over the same 20 f. Band delays are 0-12 f from rand (plus 1 f per glyph if biased). The whole word is built in about 32 f (about 40 f with the bias). Offsets are 0.12 em sideways and 0.04 em vertical: about 4 px/f on frame 1 at 120 px type, so no blur. The swap to intact text takes 1 f, then the tracking tightens over 44 f on ease-out. Hold at least 60 f with a drift of 0.3 px/f.
- Made with: kinetic-typography

### Travelling front restyles a word

- Looks like: A front sweeps left to right across a settled word and restyles each glyph as it passes, in colour or weight, sometimes with a cursor riding under it.
- Use when: Turning a static big word into a moment of discovery; emphasising one or two promise words without a highlight shape; a change of voice mid-sentence.
- Avoid when: Text still moving; sweeps whose half-restyled frames read as another word; colour and weight sweeps in the same film.
- Timing: Sweep 32 f dolly ease (front peaks about 29 px/f across a 600 px word; stretch to 40 f for wider words); band 0.6 em; per-glyph weight morph about 4 f; a second word starts about 20 f after the first; begin at least 10 f after the word lands.
- Made with: kinetic-typography

### One-word slam sequence

- Looks like: A line is read one huge word at a time: each word hits oversized and blurred, settles, then is sucked away as the next word cuts in.
- Use when: A punchy 3-5 word line on a strong beat; a problem statement or rhythmic claim; vertical formats where one word fills the screen.
- Avoid when: More than one sequence per film; lines over 5 words; calm films; a card for a lone connector word (fold it into the next word).
- Timing: Entry 22 f soft ease-out from 1.35x (the edges of a 1120 px word start at about 43 px/f, faded and blurred, and are near 22 px/f by frame 4 when the blur clears), blur 12 -> 0 by about frame 4, drift 6 f, exit 14 f ease-in to 0.6x (last frame about 72 px/f, nearly transparent); 36-42 f per word (0.6-0.7 s), last word held at least 54 f under a 1-2% scale creep; every hit on a beat.
- Made with: kinetic-typography

### Oversize word slide-in

- Looks like: A huge word arrives streaked from beside the frame and brakes on a long tail, and a trailing word follows from further out and closes the gap so the phrase locks together.
- Use when: The energy peak of a type act; a two-word claim; a cold open whose first frame already moves.
- Avoid when: Long phrases; when screen direction must run the other way across the cut; small type.
- Timing: Brake 90 f ease-out (feels like a 33 f time constant); word 1 offset 0.4W (768 px), word 2 0.6W from +16 f; drift 0.5 px/f; opacity from 0.2, readable below 20 px/f from frame 16 (word 2 from frame 21); gap 1.7x -> 1x over 80 f.
- Made with: kinetic-typography

### Phrase clamp at a junction

- Looks like: Two halves of a phrase arrive from opposite directions and lock on one baseline at a fixed junction, like a clamp closing.
- Use when: A two-part claim whose halves mean more together (subject + promise, problem + fix); the payoff line; a junction that a slot roller will reuse.
- Avoid when: Lines over 5 words or halves of very unequal length; more than once per film; the end lockup.
- Timing: Vertical: 18 f ease-out, 64 px and 40 px travel (peak 19.7 and 12.3 px/f on frame 1), 2 f word stagger, 1 f pre-pose, opacity 3 f. Snap: 35 px per side over 10 f ease-out (about 20 px/f on frame 1) to 0.75 of the gap, back over 18 f soft ease-out. Calm close: 80 f soft ease-out. Hold the locked line at least 54 f with a 0.3 px/f drift.
- Made with: kinetic-typography

### Quiet type swells on the drop

- Looks like: A word appears small and low-contrast and waits through the build, then swells to hero size, with 90% of the growth landing exactly on the beat drop.
- Use when: A hero word or product name that should detonate on the drop after a quiet intro. The one appearance of the final wordmark when the music builds into the end. A single-word answer after a question beat.
- Avoid when: There is no real musical hit to land on. Words wide enough to swell past the safe area. Using it more than once per film. Stacking a separate scale punch or camera kick on the same hit.
- Timing: Letters 5-6 f apart at 9% of the frame height. Swell over 54 f on glide ease, starting at h - 32 so 90% lands on h: scale 1 -> 2.5 (2.9 at most) in log space, with the outer edges of a 420 px word peaking at about 16.5 px/f around frame 17. Contrast goes the muted tone -> ink over the 32 f before h. Hold at most 54 f after h, or 90-120 f if this is the final lockup's one appearance.
- Made with: kinetic-typography

### Slot roller beside a fixed phrase

- Looks like: A fixed phrase holds still while the word in its slot rolls through alternatives one line at a time, speeding up until the last one lands.
- Use when: One sentence frame that fits many subjects or capabilities; listing use-cases without spending screen time; a feature loop that cycles items.
- Avoid when: Items of very different widths in a centred layout (the fixed phrase would have to move); more than about 7 items; any mask loose enough that the neighbours read as a list.
- Timing: Step 20 f whip ease (0.18 x pitch frames above a 110 px pitch) every 29-34 f (0.48-0.57 s), 3 steps, then a 28 f hold before the cut. Accelerating run: 26/14/12/8/8/4/4 f (7 items in 76 f), last item on a detent spring (home in about 9 f), held at least 54 f under a 0.3 px/f line drift. Pitch 1.5x the font size; ticks at least 3 f apart.
- Made with: kinetic-typography


## UI choreography (19)

### Cards dealt or dropped into a grid

- Looks like: Cards land in a row or grid one after another, either dealt fast with a small tilt that squares up, or falling from just in front of the camera and shrinking into their slots.
- Use when: Revealing a set of options, results, features or integrations that should read as one set with a clear reading order.
- Avoid when: There is one hero object, or more than about 8 cards (use a row cascade or a scroll).
- Timing: Deal: 5 f stagger, 7 f settle (ease-out), rotate 4 deg, scale 0.95. Drop: 54 f (ease-out), stagger 0/4/10/14 f, 534 px, scale 1.38 to 1, peak ~62 px/f, content fades in from +8 to +16 f.
- Made with: saas-product-video

### Container morph into its next role

- Looks like: One element changes shape into what it becomes, a button unfolding into a panel, a card stretching into a detail view, a pill collapsing into an app tile, so there is no navigation cut to explain.
- Use when: A click that opens something (button to panel, card to detail), a status becoming an icon, an object docking into its slot.
- Avoid when: The size change comes from content or a drag (live reflow), or the two states have no visual relation.
- Timing: Morph 30-36 f (whip ease), edges <= 70 px/f. Old content out 12 f (smooth ease); title FLIP to 0.6 scale; new content +8 f after the peak, 2-4 f stagger; backdrop dim linear over the morph. Outline retract 15 f. Content swap: out 18 f (ease-in), resize 20 f (ease-out), in 18 f (ease-out).
- Made with: morph-shapeshift

### Container resizes, content reflows

- Looks like: A card or window changes size because its content or the user changes it, growing as typed text wraps or narrowing as an edge is dragged, while everything inside reflows to the new width.
- Use when: Typing into an input, responsive layouts, resizable panels: any moment where the point is that the UI adapts.
- Avoid when: The size change is a change of role, such as a button becoming a panel (use a container morph), or text must be read during the resize.
- Timing: Widen 67% to 77% FW over 24 f (soft ease-out); +1 line per wrap over 12 f (ease-out). Drag 300-400 px over 40 f (contact ease), ends near 40 px/f, hard stop; breakpoint FLIP 16-24 f (UI ease); then a 0.3 px/f push-out.
- Made with: saas-product-video

### Drag to reorder, siblings make way

- Looks like: An item lifts under the cursor, travels on a slight arc to a new position while its neighbours slide aside one slot at a time, and settles into place with a firm landing and no bounce.
- Use when: Prioritising, scheduling, kanban boards, playlists: any product whose smart part is ordering things.
- Avoid when: The reorder is automatic (animate the computed reorder on one curve, with no cursor), or more than 2-3 drags would fall in one shot.
- Timing: Lift 8 f (UI ease), scale 1.03. Drag T = max(36, 0.15 x distance) f (glide ease) on a 0.15 bow, <= 20 px/f, tilt <= 4 deg. Sibling shift 12 f (UI ease) per index change. Drop a firm spring, shadow back over 10 f, accent relax 24 f.
- Made with: saas-product-video

### Lens list scroll

- Looks like: A list scrolls with momentum past an invisible lens line, and each item's size, tint or tilt depends on its distance from that line, like a phone picker, a rolodex cylinder or a smile-shaped arc.
- Use when: Choosing among options, showing many screens as one continuous surface, or a playful list of choices that read one at a time.
- Avoid when: Items must be read while moving fast, or a plain scroll says it more simply.
- Timing: Picker: 120 f quartic momentum, D ~900 px, 30 px/f start, < 20 px/f from f15, ~2 px/f at the cut; focus scale 1.2 to 0.85 across 375 px; optional a detent spring landing. Cylinder: 90 f (ease-in-out), ~480 px, peak ~41 px/f, R = 1.4H, perspective 1600 px. Arc: R 1750 px.
- Made with: saas-product-video

### Progress spine leads the steps

- Looks like: A thin line grows down the side of a step list with a dot at its head. Each step appears as the head reaches it, works with a spinner and a typed detail line, then flips to done, and the list scrolls to keep the head in view until the line turns a rounded corner toward the result.
- Use when: An agent, build, deploy, import or onboarding process working through steps, where the point is visible progress toward one result.
- Avoid when: There are fewer than 3 steps (one status capsule says it), or the steps finish too fast to read (show the result with a count instead).
- Timing: Head travel 40 f per step (settle ease), about 10 px/f for a 120 px pitch; wait 24-60 f per step, taken from the data. Row reveal 12 f (smooth ease) with a 12 px rise. Spinner one turn per 48 f; detail line ~1.5 chars/f; check 8 f (ease-out); tag 8 f. Scroll lag 0.08 per frame plus a 2 px/f drift, peak about 12.5 px/f. Corner radius 40 px; horizontal run 10-14 px/f.
- Made with: saas-product-video

### Push-aside with bound layout

- Looks like: An incoming panel or card enters from the edge and the neighbouring content moves aside because it is bound to the panel's edge, so one motion moves two elements and nothing overlaps.
- Use when: Introducing a detail panel, a new card or a caption beside existing UI, or a joke where the layout itself does the gag.
- Avoid when: The incoming element should float above (modal, popover), or there is no room to move into.
- Timing: Shove: 72 f (whip ease), contact after 58% of the move, word <= 20 px/f. Side panel: 36% FW over 54 f (glide ease); neighbour 0.43x travel with a 28 f lead (smooth ease); exit ~50 f. Copy: 370 px + scale 0.83 over 48 f (glide ease); lines 6 f apart from +4-6 f.
- Made with: saas-product-video

### Row cascade

- Looks like: List rows or cards appear one after another from top to bottom, each rising a few pixels as it fades in, so the list reads as data streaming in.
- Use when: Populating any list, inbox, table, feed or a pair of mirrored input and output columns.
- Avoid when: Rows are added one at a time over a longer beat (top insert), or the list arrives by scrolling (flick scroll).
- Timing: Stagger 4 f (rows) to 6 f (cards); each row 12 f (ease-out), 6-12 px rise; ink-in 12 f at +40 f; overlap the previous move by ~20 f.
- Made with: saas-product-video

### Shell first, then contents, then the action

- Looks like: The empty container is on screen first, its contents arrive left to right, the card unfolds downward in stages, and the primary button fills last as the clear call to act.
- Use when: The first appearance of any real product screen, especially dashboards, headers and forms whose reading order matters.
- Avoid when: The screen should feel already alive on the cut (enter it moving with a rise-in), or the shot is shorter than about 40 f.
- Timing: Children 4 f stagger, 12 f each (ease-out), 6 px rise. Media fill 8 f, 8 f apart. Button fill 16 f (linear) from +20 f; label inverts at +28 f. Unfold 36 f then 24 f (smooth ease), content at 60% open. In-UI headline 6 f per word.
- Made with: saas-product-video

### Spawn from the anchor point

- Looks like: Menus, popovers, drop targets and detail cards scale out of the exact point that caused them, such as the cursor tip or a map pin, and collapse back into it.
- Use when: Any UI that opens from a click, or a drag target appearing: menus, popovers, dialogs, drop zones, cards from a map pin.
- Avoid when: The element enters from off-screen or is a full window (rise-in), or the trigger point is out of frame.
- Timing: Small: 12 f (lmix, ease-out) from 0.05, opacity 4 f, far edge ~63 px/f for a 300 px menu; camera reframe from +2 f over 20-40 f (camera ease). Large: 48 f (lmix, smooth ease) from 0.036, hint over the last 8 f, collapse 36 f (smooth ease).
- Made with: saas-product-video

### Top insert pushes the list down

- Looks like: New items arrive at the top of a list one at a time and every earlier item slides down one slot, on a steady metronome that reads as abundance or on a slower cadence where each row resolves as it is generated.
- Use when: Results, messages, subtasks or saved items accumulating: generated rows, imports landing, a feed or a stack filling up.
- Avoid when: The whole list should appear at once (row cascade), or there are so many inserts that the pushes blur into noise (scroll instead).
- Timing: Metronome: every 14 f, push 155 px over 20 f (UI ease), pill reveal 12 f (UI ease), label +4 f, camera drift 19 to 3 px/f (x0.97 per frame). Generation: every 36-40 f, resolve 12 f (ease-out) from scaleX 0.6 and 6 px blur, push 66 px over 10 f (UI ease).
- Made with: saas-product-video

### Clutter pile-up, then strip to one

- Looks like: Clicks spawn copies of a control until the frame is a messy pile, then elements vanish one per beat and the survivors snap to re-centre until a single tile remains.
- Use when: Showing overload (too many tools, buttons, tabs, notifications) and then focus: the product reduces chaos to the one thing that matters.
- Avoid when: Calm or premium films, or elements whose text must be read; the jumps are deliberately abrupt.
- Timing: Spawns every 4 f for ~60 f (12-15 clones), 8 f each (ease-out, 40-80 px), pile drift 1.5 px/f. Removals every 5-7 f with an instant re-centre; last survivor 17 f with a 0.5% drift.
- Made with: saas-product-video

### Genie launch from an icon

- Looks like: A dock or home-screen icon flares open at its top into a curved funnel that keeps widening until it fills the frame, and the app's first screen is already sitting inside it.
- Use when: Opening an app, a document or a tool from its icon in a dock, launcher or home screen, as a playful product-native scene change.
- Avoid when: The product is never launched from an icon, or the film already has a genie (once is a gag, twice reads as a template).
- Timing: Press, then funnel from +4 f: 44 f in log space (about x1.06-1.08 per frame, linear progress). Centre drift over the same 44 f (smooth ease). Waist and bottom edge open over the last 24 f (smooth ease). Fastest edge ~70-75 px/f at the end. Optional content settle 1.04 to 1 over 44 f (soft ease-out). Clip removed on full cover; the next UI event starts on that frame.
- Made with: saas-product-video

### Path fractures into a fan, then re-converges

- Looks like: A solid line draws out, breaks into dashes, splits into a fan of curves that end on obstacle pills, and later the curves funnel back into one point that becomes the next diagram.
- Use when: Explaining the friction of an old way (one simple path turning into many obstacles) before the turn to one clean path.
- Avoid when: The viewer needs real product UI on screen; this is diagram language, and a diagram act longer than about 4 s loses the thread.
- Timing: Trunk 12 f (linear); dashes at +12 f over 8 f to '24 12'; fan at +26 f: 6 curves x 24 f (glide ease), 2 f stagger, complete at +60 f; punch-in cut at ~+70 f (2.5x). Converge 24 f (smooth ease); camera landing 210 px over 60 f (ease-out), 22 px/f at its start.
- Made with: saas-product-video

### Stalled state by dimming

- Looks like: A token stops on its rail, the destination greys out, short status words appear one after another, and the frame goes briefly still so the blockage is felt.
- Use when: The problem beat: money, a message or a task stuck waiting (closed, pending, rejected) just before the product unblocks it.
- Avoid when: The film has no problem act, or the block would sit longer than about 1.5 s; stillness only works as a short contrast to the motion around it.
- Timing: Node dim 8 f (smooth ease) to 30%. Status words at +6/+28/+40 f, 8 f each (ease-out, 6 px rise); first word dims at +51 f. Freeze <= 15 f on a silence, then 0.3 px/f drift.
- Made with: saas-product-video

### Fanned stack resolves into slots

- Looks like: A tilted, overlapping stack of cards spreads into an even row, or each card flips to show its face and flies small into a slot of a list grid where its label resolves.
- Use when: Many options, offers, integrations or tools becoming an orderly set: the 'all in one place' or 'compare them all' beat.
- Avoid when: The cards must be read while they move, or there is only one card.
- Timing: Row: 2 f stagger, T = max(24, 0.09 x travel) f (ease-out), tilt +-6 deg. Flip: 6 f stagger, flip 6 f (8 f over 200 px wide, linear), drift 12 f (ease-out), FLIP to slot max(12, travel/20) f (settle ease), label 8 f; six cards in ~60 f.
- Made with: saas-product-video

### Orbit gather and merge

- Looks like: Tokens swing into orbit around a node, slow to a lazy spin, then accelerate one by one into a single exit point from which a line shoots out.
- Use when: Several inputs, funds or sources gather before one action (pooling, batching, syncing, sending) and the idea should be told by physics with no words.
- Avoid when: The tokens are UI cards carrying text (unreadable while orbiting), or the story has no single output point.
- Timing: omega = 13.25*exp(-f/10) + 2 deg/f, radius 95 px at 1080p. Spawns f10/f18/f28, 10 f each (ease-out). Merges 16 f each (contact ease), landing f72/f82/f86 at < 60 px/f; a hit pulse (2 f up, 5 f down) on the exit node. Exit line f92, 12 f (ease-out). About 105 f in all.
- Made with: saas-product-video

### Outline-led insert and spawn

- Looks like: A thin accent line or a heavy outline appears first and opens into a new row or a modal, then the stroke decays to a hairline so the content takes over.
- Use when: A click that creates something (a new account, row, record or dialog) that must read from a wide shot, or repeated creation shown as a rhythm.
- Avoid when: The accent already means something else in the film, or the shot is a calm monochrome close-up where a bright stroke would shout.
- Timing: Line 1 f; open 10 f (UI ease); border decay 24 f (linear); content in the last 4 f; inserts every 41 f. Modal 26 f (lmix on ease-out) from scale 0.07, far edge ~52 px/f; stroke 6/10/1 px; thin 12 f; opacity to 0.3.
- Made with: saas-product-video

### Toss into a bin with one rebound

- Looks like: Icons or chips are thrown into a container that rises in to catch them, drop through its mouth and peek back out once before settling.
- Use when: A comic or decisive 'throw the old way away' beat: replacing old tools, clearing clutter, deleting the problem.
- Avoid when: Serious, calm or enterprise tone, or the film has already used its two spring landings.
- Timing: Bin rise 160 px, 24 f (ease-out). Item rise ~260 px, 24 f (ease-out); hang 3 f; fall ~340 px, 22 f (contact ease), <= 70 px/f; tilt +-15 deg. Chain: 60 f per chip (contact ease along the path), 5 f lag. Rebound at +6 f, ~24 px, a landing spring, settled in 16 f.
- Made with: saas-product-video


## Data and numbers (17)

### Constant-speed bar sweep with lit caps

- Looks like: A row of bars grows in a wave that travels at constant speed; each bar eases up on its own and flashes a bright cap that relaxes to the resting tone.
- Use when: Volume, activity or histogram data streaming in; an opening equaliser or skyline that hints at growth.
- Avoid when: Bars that must be compared precisely, since the wave delays reading; fewer than 6 bars.
- Timing: 1.6 f per bar (~25 px/f wave). Each bar 12 f on ease-out (at least 0.09 x its height in px). Cap relaxes over 20 f.
- Made with: animated-chart

### Ease-out count-up from a near-final value

- Looks like: A proof figure counts up in place from a credible value just below its target and decelerates, so the last units tick in one at a time and it reads in about half a second.
- Use when: A single proof figure (countries, users, a price) must register in under a second, or a number inside a UI shot should feel live.
- Avoid when: The number is the film's hero reveal and deserves a reel or a snap-out; nothing on screen causes the count to start.
- Timing: Hero count 28 f on typing ease (quad-out: 2x the mean rate at the start, so the last unit lands in the final ~6 f). Prices and recounts 36-46 f; ambient UI KPIs 36-104 f. Start at 85-90% of the target. Hold the landed figure at least 36 f (plus 6 f per word of any label) under a 2-3% breath before anything covers it.
- Made with: animated-chart

### Flag cascade, then one chosen

- Looks like: Status marks appear on a set of cards one after another, then a single card switches to the accent state: many flagged, one picked.
- Use when: Triage, review, matching, anomaly detection: anything that narrows many down to one.
- Avoid when: The pick isn't what the product actually outputs; grids of more than ~12 cards, where the cascade reads as a queue.
- Timing: Flags 6 f apart, 6 f each. Selection ~28 f after the first flag, an 8 f change. Hold at most 48 f with a 2% push. The chosen card exits on ease-in.
- Made with: animated-chart

### Line chart draws with a tracking head

- Looks like: A line or stepped series draws left to right behind a solid dot at its head that the eye can follow, accelerating through the middle and creeping into its last point.
- Use when: Growth, price or usage over time; any chart where the trend is the message.
- Avoid when: Invented up-and-to-the-right data; charts under ~400 px wide, where the head reads as noise.
- Timing: Full draw 96 f on settle ease (peak near 29%, 3.5x the mean speed; the last 30 f creep at about 2-3 px/f on a 1,400 px path). Short form: 24 f on ease-out, with the area fill fading in from 8 f later over 16 f. Head peaks at 40-60 px/f at 1080p. Endpoint value rolls over 14 f.
- Made with: animated-chart

### Mechanical digit reel

- Looks like: Each digit sits in its own masked column and rolls vertically like an odometer: the low columns spin while the high ones step once, landing column by column.
- Use when: Counters with a tactile, product-like feel: totals, balances, counters that step on visible events.
- Avoid when: The film already counts with plain in-place digits (keep one counting style per film); fewer than 3 changes, where one roll is enough.
- Timing: Count 60 f on ease-out. Column roll 14 f (6-8 f for event counters). Detent landing ~16 f. Ticks at least 2 f apart.
- Made with: animated-chart

### Mini bar-chart answer card

- Looks like: Inside a chat or a panel, an answer arrives as a small card of labelled horizontal bars that grow in sequence, followed by a one-line insight that states the key figures.
- Use when: An AI or analytics product answers a question with data; a walkthrough needs one piece of quantitative proof.
- Avoid when: More than 6 rows, where the group outruns 30 f and the labels shrink; bars that carry no real meaning.
- Timing: Rows 20 f each on soft ease-out at a 5 f stagger (the group lands within 30 f). The insight types over ~40 f, starting 6 f after the last bar. Card visible ~180 f under a 2% breath. Optional 2.4x punch-in cut, then a pan from 20 px/f decaying 0.89 per frame (settled in about 30 f).
- Made with: animated-chart

### One control drives several live numbers

- Looks like: Dragging a slider visibly drives every dependent figure in lockstep, and the fill changes tint once it passes a marked threshold.
- Use when: Calculators, pricing, risk limits, utilisation: any feature whose logic is 'move this and those follow'.
- Avoid when: The dependent figures aren't computed consistently from one formula; more than 3 dependents.
- Timing: Drag 90 f on smooth ease (fastest change mid-drag). Cursor grabs 8 f before. Figures update every whole frame. Hold the end state at least 36 f under a breath.
- Made with: animated-chart

### Ring gauge filling with its centre number

- Looks like: A circular gauge sweeps to its value while the number at its centre counts on the same progress, and the ring's end cap leads the eye around.
- Use when: Percentages, scores, completion and utilisation; status pills and KPI tiles.
- Avoid when: Values that aren't parts of a whole; more than 3 concentric rings.
- Timing: Fill over N = max(48, 0.48 x radius x target) f on soft ease-out (48 f for most gauges, 77 f for a full 160 px ring). Centre count on the same progress. Accent relaxes over 20 f after landing. Nested rings 6 f apart.
- Made with: animated-chart

### Area-true ratio comparison

- Looks like: A multiplier claim ('10x smaller') plays as a block that shrinks in log space to the area the ratio implies, leaving an outline of its old size behind.
- Use when: Multiplier and reduction claims about size, cost, time or footprint.
- Avoid when: Ratios above ~25x, where the block shrinks to a dot (show the number alone); claims that aren't really proportional.
- Timing: Shrink 48 f on smooth ease via lmix. Fill mixes to the accent over the last 12 f. Ratio count 36 f on typing ease, landing with the block. Hold at least 36 f under a 2% breath.
- Made with: animated-chart

### Before-to-after with a delta chip

- Looks like: The old figure steps back to a small grey 'before', the new figure counts in at hero size, and a delta chip ('-38%') pops in the accent on the landing frame.
- Use when: Improvements such as cost down, speed up or errors falling from 412 to 3; before-and-after claims.
- Avoid when: The change is small or noisy; the story has no real 'before' state to show.
- Timing: Old figure exits over 12 f on ease-in. 'Before' MaskRise 30 f. New count 36 f on typing ease. Strike 10 f on ease-out. Chip on the landing frame (a small quick spring, no overshoot), fill relaxes over 20 f. Hold at least 36 f under a breath.
- Made with: animated-chart

### Companion glyph swaps mid-count

- Looks like: A small icon riding a counting number (a flag, an avatar, a status glyph) swaps to its destination state when the count crosses a threshold, then drops from superscript to the baseline.
- Use when: The count carries a from-to story (origin to destination, free to paid, pending to done) that one icon can tell.
- Avoid when: The glyph would only be decoration; counts shorter than 20 f, where the swap gets lost.
- Timing: Swap at ~60% of the count (frame 17 of a 28 f count). Drop 8-12 px at 1080p over 8 f on ease-out through arrive. The count lands 10-11 f after the swap.
- Made with: animated-chart

### Process-status pill with ring progress

- Looks like: A compact capsule shows where a process stands in one glance: a live dot, a mono step label, a ring filled to the current percentage, the step count and a grey date.
- Use when: Proving that a real, structured process exists (pipeline, build, delivery) as an overlay on process footage.
- Avoid when: The step and percentage aren't true to the story; frames that already carry a headline, which the pill would compete with.
- Timing: Arrival on a firm spring (~24 f to settle). Ring fill 30 f on ease-out. Step roll 14 f. Dot pulse: attack 2 f, tau 8 f. Visible 46-90 f.
- Made with: animated-chart

### Top-to-bottom row refresh

- Looks like: When a filter changes, a thin scan line crosses each table row in turn from top to bottom, and the row's icon, label and values change behind it.
- Use when: Tables, activity feeds or leaderboards that refresh on a filter or a new period.
- Avoid when: Only one cell changes, so a Roll on it is enough; more than 8 rows, where the cascade reads as a queue.
- Timing: Starts 2 f after the chip lands. 3 f row stagger. 20 f per row, linear (at most 60 px/f across a 1,250 px row). Six rows finish within ~35 f. Hairline fades over 6 f.
- Made with: glitch-fx

### Tucked unit under the last digits

- Looks like: A small lowercase unit word fades in right-aligned under a big number's last digits, its top overlapping the numeral's baseline, so number and unit read as one mark.
- Use when: A hero figure needs its unit (views, users, ms) without a second line pushing the layout down.
- Avoid when: The unit is longer than one short word; numbers ending in narrow digits (1, 7) that leave no room to tuck under.
- Timing: Starts at least 12 f after the number settles (36 f is a good default). Opacity over 19 f on smooth ease with a 4 px rise via arrive. Label at 0.35x the numeral size, overlapping its baseline by 30% of the label height.
- Made with: animated-chart

### Unit grid that fills to the count

- Looks like: A grid of small squares, each standing for a fixed number of units, fills in a diagonal wave while a counter beside it reaches the total, and one cell lands in the accent.
- Use when: Shares and proportions ('3 in 10 teams'), quotas, capacity; making a large count tangible without a chart.
- Avoid when: Exact values with many significant digits, which the grid can't show honestly; cells under 12 px on vertical phone formats.
- Timing: Diagonal wave over 30 f on stagger with ease-out. Each cell fades over 8 f, with an a small quick spring scale. Accent cell pulse: attack 2 f, tau 8 f. Hold at least 36 f with a 2% push.
- Made with: animated-chart

### Hero bar in close-up, then pull back

- Looks like: The winning bar (or the hero chart) grows across a tight frame, then the camera eases back to show the whole chart, with the grey comparison bars and their values.
- Use when: Benchmarks and comparisons the product wins; any chart whose hero value should be felt before it is compared.
- Avoid when: Narrow wins, which the close-up would oversell; more than ~6 bars, whose labels go unreadable after the pull-back.
- Timing: Bar fill 50 f on smooth ease (no overshoot) with a 4% push. Pull-back 52-80 f on camera ease to 0.65-0.75 of the close scale. Values count over 28 f on typing ease at a 4 f stagger. Hold the full chart at least 36 f under a breath.
- Made with: animated-chart

### Metric as the first statement

- Looks like: The film opens on its proof number already moving, with no title and no logo, and the brand waits for the end lockup.
- Use when: The product has one strong, true outcome number (users, views, savings) that should earn attention before the name does.
- Avoid when: The number is weak, generic or can't be verified; films where the mark itself must lead.
- Timing: First change by frame 2. Settled by frame 40. Readable for 72 f (about frames 41-113). Hand-off cut near frame 113. Optional freeze of at most 15 f on the landing silence.
- Made with: animated-chart


## Product demo (22)

### Agent status beat, then streamed answer

- Looks like: The product's tiny working status is shown at hero size, as a black capsule with a spinner and a typed label or as bare headline type, holds for a beat with a looping ellipsis or shimmer, then dissolves as the answer streams in.
- Use when: An AI or agent product needs its invisible work made visible, and a moment of anticipation before the payoff.
- Avoid when: The product is not autonomous; the hold would run past about 74 f; a second status beat in the same film.
- Timing: Label types in about 30 f (40 f at headline size); hold 60-74 f with the ellipsis stepping every 16 f and one shimmer sweep per 60 f (≈ 20 px/f); camera 1.62 → 1 over 56 f on soft ease-out; dissolve 12 f; stream ≈ 1 character per frame (41 characters in about 42 f); payoff variant: hold 30 f, dim 12 f.
- Made with: saas-product-video

### Change applied as a visible diff

- Looks like: A proposed edit lands in a code or document view as a diff: outgoing lines strike through and fold away, incoming lines open in place with a marker in the gutter, and the view steps hunk by hunk before the change is accepted.
- Use when: AI coding or writing assistants and review, versioning or migration tools, when the claim is 'it changes exactly the right lines and shows you which'.
- Avoid when: The code is unreadable at frame size (macro in first), or the change needs more than three hunks (show a summary instead); never give removals a second colour.
- Timing: Strike 8 f on UI ease; fold 12 f on UI ease starting 6 f later; slot open 12 f on UI ease with the text in at 70%; tint relax 36 f; hunks 60-90 f apart, camera hop 48 f on glide ease (≤ 300 px); accept fade 12 f; final hold 36-48 f under a 2% breath; at most three hunks.
- Made with: saas-product-video

### Command runs, output prints in bursts

- Looks like: A command is typed at human speed and entered; the terminal answers machine-fast, printing whole lines in uneven bursts with a stepping spinner and a progress bar, and ends on a single success line.
- Use when: Developer tools, CLIs, infrastructure and build products, where the contrast between a human-typed command and machine-fast output is the speed claim.
- Avoid when: The audience is not technical, or the output itself must be read line by line (show the result screen instead); never type the output.
- Timing: Command at 30 cps, caret hold 10 f; bursts of 2-6 lines 1-2 f apart with 10-24 f gaps (40-80 lines in 120-180 f reads machine-fast); line relax 24 f; burst scroll max(6, 0.14 × px) f on UI ease; spinner step 4 f; progress bar 60 f on smooth ease; success line held 48-60 f under the breath with the caret blinking 30/30.
- Made with: saas-product-video

### Device rises already moving

- Looks like: A phone or app window enters from below already travelling on the cut frame and decelerates into place near centre while the whole shot slowly scales down.
- Use when: The first product shot after a type card or a photo, when the previous shot's energy should carry straight into the product.
- Avoid when: The device is already on screen; a calm film where a 20 px/f arrival feels pushy; it would be the third rise in a row (vary with a tilt or a pull-back).
- Timing: On a cut: 140-160 px over 44 f on ease-out, first frame ≈ 6.2 × rise / 44 (about 20-23 px/f), 75% of the travel by f9, settled by f44; shot scale 1 → 0.9 over 48 f on soft ease-out. Over a title: ≈ 1,000 px in 48 f on glide ease, title fade 36 f starting 16 f early. Peek variant: 14 f peek, 4 f hover, 40 f launch on whip ease, 60 f scale drift.
- Made with: saas-product-video

### Edit with the product's own UI

- Looks like: Instead of cuts, the film moves between product areas the way the app does: a window recedes to a corner, a sheet slides up, a popover pops from its anchor, a button or card unfolds into a full panel.
- Use when: Walkthroughs across several product areas; any film where each transition can also demonstrate how the product navigates.
- Avoid when: A purely conceptual or type-led film; desktop chrome that is not part of the brand world; more than one native transition every 3 s (it starts to feel like a screen recording).
- Timing: Generic chain: exit on ease-in 22 f, gap 4 f, entrance on ease-out 52 f. Minimize 22 f; sheet 52 f (peak ≈ 50 px/f); popover 12 f plus a 20-40 f reframe; launch slide 96 f (peak ≈ 18 px/f); unfold 28 f on settle ease (at least edge travel / 20 f), content in 8 f after the peak, stage dim 24 f.
- Made with: saas-product-video

### Fast prompt at true scale

- Looks like: The real prompt bar fills with a long, honest instruction in about a second at full legible size, the card growing as lines wrap, then the text is sent up into a chat bubble.
- Use when: An AI, search or command product whose real input is the story; showing a real task without a dull typing wait.
- Avoid when: The prompt runs past about 100 characters (cut it); a human-paced beat is the point (use 30 cps with human rhythm); the product is not input-driven.
- Timing: Time box 68 f, or 50-72 cps (0.8-1.2 characters per frame); card width 24 f, +1 line per wrap in 12 f on ease-out; read hold after typing at least 36 f + 6 f per word, kept alive by the breath; send: 12 f out, bubble 16-18 f in with a 4 f offset.
- Made with: saas-product-video

### Flick scroll lands the target

- Looks like: A list or page scrolls like a trackpad flick, entering already fast or ramping up briefly, then glides on an exponential tail until the target row rests at its reading position.
- Use when: Showing volume (many results, a long page, a feed), or moving down a form to its next section with a human feel.
- Avoid when: The viewer must read during the move; the list is shorter than two screens; it would be the third scroll in a row.
- Timing: Cut entry: v0 54 px/f, decay 0.943 (tau 17 f), ≈ 76 f to rest. In-shot: ramp tp 28-40 f, vmax 35-60 px/f, tail decay 0.93 for a form section, up to 0.98 for a long volume reel (≈ 277 f for ≈ 2,600 px); readable below 3 px/f.
- Made with: saas-product-video

### Ghost suggestion accepted with a key

- Looks like: As someone types, the product proposes the rest of the line as pale ghost text after the caret; a small key chip appears, the key is pressed, and the ghost text inks in left to right as the caret jumps to its end.
- Use when: An assistant that completes text, code, email or form fields inline: the moment the product does the work is one key away, and the cause (the key) and the effect (the ink) share a frame.
- Avoid when: The product generates whole answers rather than inline completions (stream the answer instead), or the suggestion runs past about two lines at readable size; never show more than two accepts in a row.
- Timing: Prefix at 30 cps; ghost text 12 f after the last key, whole in 1 f (or 2 characters per frame); chip on a small quick spring with a 6 f fade; wait 30-40 f under a 2% breath; press 4 f down, 8 f recoil; recolour front 10 f per line (lines 3 f apart), accent relax 12 f; chip out over 8 f from ACCEPT + 4; read hold after acceptance 36-48 f.
- Made with: saas-product-video

### Hard swap on the cause frame

- Looks like: On a click or selection the product image, view or value changes in one frame with no crossfade, any price or count rolls up from just below its new value, and a physical card can hide the swap in a small 3D kick.
- Use when: A choice changes the product instantly: a variant picker, filter, plan selector, theme switch, a board that appears whole on launch.
- Avoid when: The change is a process the viewer should watch; two numbers would sit half-and-half in place; swaps faster than one per 30 f (the clicks read as a macro).
- Timing: Swap 1 f on the cause frame; hover 6 f before the press; recount 36-46 f on ease-out with 14 f digit rolls; punch attack 2 f, tau 5; kick peaks on the swap frame and settles in 6-8 f; at most one swap per 30 f, 54 f apart in a repeating sequence.
- Made with: saas-product-video

### List narrows with each keystroke

- Looks like: A shortcut opens a command palette or search field, and as the query types the list answers every key: non-matching rows fold away, survivors slide up, matched letters ink in, and the highlight rides the top result until Enter.
- Use when: Search, command menus, filters and pickers: any product whose speed claim is 'type a few letters and it is there', proving instant results without a spinner.
- Avoid when: The rows are illegible at frame size (punch in first), or the query is long (past about 12 characters it becomes a typing beat); do not FLIP more than about ten rows at once.
- Timing: Chips 4 f apart, press 4 f down + 8 f recoil; palette 10 f on soft ease-out, backdrop rack and veil 12 f; query 30-40 cps; row fold 10 f on UI ease (opacity 6 f); survivor FLIP max(12, 0.14 × px) f on UI ease; highlight 8 f on UI ease; 4-7 keys narrow 8-10 rows to 1-3; final list held 24-36 f under a 2% breath before Enter; close 8 f.
- Made with: saas-product-video

### One native control as the demo

- Looks like: Instead of a screenshot, the feature is shown as the single control that embodies it (a picker wheel, a toggle, a segmented switch) at large scale, centred, with no chrome, doing only its native interaction.
- Use when: A settings, targeting or compatibility claim in a type-led film, where one interaction says it is a real product faster than a full UI.
- Avoid when: The feature needs context to make sense; the control is generic (every app has a toggle) and says nothing about the claim.
- Timing: Shot ≈ 120 f; picker v0 20 px/f, decay 0.975 per frame, an item crossing focus about every 30 f early on and slowing after; detent settle ≈ 12 f; toggle knob 8 f; segment glide 18-24 f.
- Made with: saas-product-video

### Scrub a chart with a live readout

- Looks like: The cursor glides across a chart; a hairline and a dot ride the series beneath it and a small readout shows the date and value at that point, stepping from data point to data point until it lands on the one that makes the claim.
- Use when: Analytics, finance, health or monitoring products whose value is reading any point in history; a calm interaction beat after a fast one.
- Avoid when: The chart has no point worth landing on, or the readout is illegible at the framing (punch in to 1.6-2x first); never scrub faster than the readout can be read.
- Timing: Scrub 90-150 f on smooth ease at 6-10 px/f (the readout never moves faster than the cursor); hairline and readout in over 6 f; value roll 8 f per index change; landing pulse attack 2 f, tau 6; accent relax 24 f; hold on the landing point 36-48 f under a 2% breath.
- Made with: animated-chart

### Before/after drag divider

- Looks like: The cursor grabs a vertical divider on the product and drags it across, wiping away the old state to reveal the new one in the same layout.
- Use when: Redesigns, image or audio cleanup, performance gains, any this-got-better claim with a visible difference.
- Avoid when: The two states differ in layout (the wipe then reads as a glitch); the difference is invisible at frame size; the film has no human gesture anywhere else.
- Timing: Cursor approach 36-48 f on ease-out; press 4 f down, 8 f recoil; drag 60 f on smooth ease, or 36 f to the midpoint on glide ease (peak ≈ 46 px/f), a hold of ≤ 24 f, then 36 f on to the edge.
- Made with: saas-product-video

### Drag assets in, skeletons fill

- Looks like: The cursor drags a fanned stack of images into the input; after the drop they appear as grey skeleton thumbnails that fill with the real images one by one.
- Use when: The product takes real material as input (files, photos, documents) and the viewer should see that context going in.
- Avoid when: The input is text only; the drag path would cross text being read; more than six assets (show a count chip instead).
- Timing: Drag ≈ 72 f on smooth ease; thumbnails 8 f each at a 6-10 f stagger (≈ 36 f for four); attachment row opens over 18 f on UI ease.
- Made with: saas-product-video

### Generated view resolves from soft

- Looks like: A freshly generated window or row appears as a soft, out-of-focus shape over a flat placeholder plate and snaps into crisp UI in about a third of a second.
- Use when: An AI or build step produces a result and it should read as just arrived, without a spinner.
- Avoid when: The UI was already on screen (use a state change); more than two resolves in one sequence (it becomes a fog filter); type so small that 12 f of softness hurts legibility.
- Timing: Window: 20 f on ease-out (blur 20 → 0 px, opacity 0.6 → 1, scale 1.03 → 1), plate fade 20 f on smooth ease. Rows: 12 f each, push-down 10 f on UI ease, cadence 34-40 f. Card stats row: 12 f, starting once 60% of it is revealed.
- Made with: saas-product-video

### Long page flown like a runway

- Looks like: A whole long page lies on a steeply tilted plane that recedes to a horizon, and the view travels along it faster and faster, so the page reads as one landscape and is cut at full speed.
- Use when: Showing the length or completeness of a page, document, feed or site in about a second without asking anyone to read it; a fast connective beat between two readable product shots, or the carrier for a change made mid-move, such as a theme switch.
- Avoid when: The content must be read, the page is short (it reads as a tilted card instead), or the frame is vertical and leaves too little runway; use it once per film.
- Timing: Flight 80 f: plane speed 6 → 30 px/f over 54 f (closed form 6n + 0.225n², linear acceleration with no ease-out), then 36 px/f for 26 f into the cut, about 1,900 px of travel (page at least plane length + 2,000 px); near-edge screen speed ≈ 6 → 34 px/f, under the blur pass throughout; rotateX 55°, perspective 1200 px, plane 2x frame height; caption words 6 f apart, landed by f40 of the flight; cut on the final frame.
- Made with: saas-product-video

### Mark docks into the app

- Looks like: An integration mark or icon travels to an app tile or page and settles overlapping its face, rising in front of it at the moment of contact, so it reads as plugging in.
- Use when: An integration, plug-in or works-inside claim; handing off from a settings screen into the platform it acts on.
- Avoid when: The mark would pass over text being read; the mark is also the end lockup (it would appear early, so dock an integration icon instead).
- Timing: Approach 25 f on soft ease-out, overlap at f17, rest at f25; tile bump 2% (attack 2 f, tau 3, about 8 f). Variant: lift 27 f, colour invert 18 f, float 45 f, shrink 12 f on ease-in-out, page swing 50 f on ease-out, one-frame swap to the page logo on arrival.
- Made with: saas-product-video

### Pin field pull-back

- Looks like: A map pulls back from a close view to reveal a field of location pins that drop in as accent marks and relax to ink, then a card grows out of the pin the cursor picks.
- Use when: Location, coverage, store-finder or delivery features; any everywhere claim backed by real places.
- Avoid when: Fewer than about five locations; a map style busy enough to hide the pins; a route arc has already run on the same map.
- Timing: Pull 50 f on soft ease-out (first frame ≈ −7% scale per frame); pins ≈ 11 f each on a small quick spring, the group within 30 f (2-6 f apart); colour relax 24 f; card 12 f, leader 8 f, label 12 f.
- Made with: saas-product-video

### Several people at work at once

- Looks like: Two or three named cursors move and act on the same board at the same time, each in its own rhythm, while presence avatars stack in the corner, so collaboration reads without a word.
- Use when: Collaborative documents, whiteboards, design and planning tools: anything whose claim is 'together, live'.
- Avoid when: A single-user product, or a frame where the name flags would be too small to read; never more than three cursors, which turns into noise.
- Timing: Shot 180-240 f; travel 6-14 px/f on smooth ease, arrivals and presses at least 6 f apart; wander ≤ 6 px per 24 f; one action every 30-50 f across all cursors; note settle on a firm spring ≈ 16 f; accent outline 24 f; avatars on a small quick spring 6-10 f each; at most three cursors.
- Made with: saas-product-video

### Headline becomes the product input

- Looks like: Without a cut the headline turns into the product: a caret appears in the gap between two words, swells into a capsule and widens into the input bar that shoves the words aside, or the sentence inside a card dissolves while the card reshapes into the input.
- Use when: Bridging from message to demo in a type-led film; the product's core surface is an input, search or command bar.
- Avoid when: The product is not input-led; the headline has no natural gap; the bar would have to stay translucent over a busy backdrop (go straight to opaque).
- Timing: Caret 6 f, hold 8 f, capsule 14 f, widen 60 f on settle ease (a short bar: 23 f in all on ease-out); contents 12 f each at a 4 f stagger, button fill 16 f linear. Card variant: word exits 6 f apart, resize 30 f on ease-out, placeholder 16 f.
- Made with: saas-product-video

### Shared element survives the page change

- Looks like: The cursor clicks a row; the page drains away except the row's icon (or the clicked card), which stays exactly in place while the next page assembles around it with a short zoom-out.
- Use when: Navigating into a detail view, or carrying a piece of content between apps, where spatial continuity should make the product feel instant.
- Avoid when: Nothing exists in both states; the anchor is under about 40 px and cannot carry attention; it would need to travel more than a third of the frame (use a native transition).
- Timing: Hover 12 f, press (pressAt), page A out 6 f, anchor alone 2-4 f, page B 1.2 → 1 over 24 f on ease-out (≤ 50 px/f at 960 px from the anchor), block stagger 2 f over 10 f: about 48 f from click to settled. Cross-app: 36 f out, 20 f resize, 24 f in. Cut variant: anchor drag 40 f on whip ease.
- Made with: saas-product-video

### Tilted product plane flattens

- Looks like: A real product page lies tipped back in perspective, rises toward the camera and rotates flat to face the viewer, landing the product as a frontal screen.
- Use when: Introducing a real web page or app screen as the real thing while keeping the camera alive; the first frontal look at the product.
- Avoid when: The UI must be read during the move; the plane would need more than about 30° of tilt (text shears and aliases); the same flatten ran within the last 10 s.
- Timing: Rise 68 f on ease-out: top edge ≈ 35 px/f on the first frame, ≈ 12 px/f by f4, ≈ 5.5 px/f by f8, then ≈ 3.5 px/f drift and an exit at ≈ 5.5 px/f on ease-in; tilt follow-through 20 f, starting 6 f before the position lands; hero de-skew: hold ≤ 34 f, then 80 f on glide ease (peak edge speed ≈ 60-70 px/f at about 31%).
- Made with: saas-product-video


## Seams between acts (12)

A seam is the join between two acts of a film. These twelve seams hide the join in a move. Lengths are frames at 60 fps.

### Relay handoff

- Looks like: one story object, such as a dot or a cursor, crosses the join untouched while the world around it changes.
- Use when: one object carries the story from act to act.
- Timing: it has no length of its own. The object moves on one continuous path across both acts.
- Check: the object never blinks out, never changes style and never shows twice.
- Made with: sloosh-motion-director

### Shared-element container morph

- Looks like: the pieces of the logo grow into the containers of the product, such as the sidebar and the main panel.
- Use when: a brand opener hands over to the product.
- Timing: about 46 f on an ease-in-out. The pieces join without a gap. At the landing frame the live product takes over in the exact same place.
- Check: no double exposure, no thin line of background between pieces and no shimmer at the swap.
- Made with: morph-shapeshift or saas-product-video

### Iris or flood from the object

- Looks like: the story object grows to fill the frame, or the frame closes onto the object.
- Use when: a button press or a dot should open the next act.
- Timing: an iris that closes onto a dot lands by the first beat (about 30 f). A flood out reaches the farthest corner in about 18 f on an ease-out and is already moving on the drop frame.
- Check: the radius never crawls and then snaps. Do not use the same iris three times.
- Made with: sloosh-motion-director

### Implosion, silence, drop

- Looks like: the whole world shrinks and turns into the story object. One beat of true silence follows. Then the music drops.
- Use when: the film needs one big release into its main act.
- Timing: the world shrinks to nothing and turns about 14 degrees over about 19 f on an ease-in. The object grows a little. The silence lasts 15 f at most. The drop lands on the downbeat.
- Check: the object holds or grows while the world shrinks. The silence carries no sound tail.
- Made with: sloosh-motion-director

### Shutter collapse

- Looks like: a full-frame field closes to a thin line, and the line becomes the story object.
- Use when: an act ends on a hard beat.
- Timing: height first over about 16 f, then width over the next 13 f. It is already moving on the drop frame.
- Check: the two axes move one after the other. Both at once reads as a zoom out.
- Made with: sloosh-motion-director

### Split on a seam

- Looks like: the product opens along one of its own borders, such as a sidebar edge or a list divider. One side becomes a column of type and the other side fills the frame on a slight hinge.
- Use when: a feature needs a caption beside the live interface.
- Timing: about 42 f for the split. It closes so that it rests exactly on the first frame of the next act.
- Check: the split runs along a real border. A split along an invented line reads as a wipe.
- Made with: saas-product-video

### Velocity-matched cut

- Looks like: a hard cut between two moving shots. The motion continues in the same direction at the same speed.
- Use when: the edit should feel fast and unbroken.
- Timing: the exit speeds up over 10 to 24 f. The cut lands at peak speed. The entry slows over 48 to 84 f.
- Check: the direction never reverses and the speed never halves or doubles across the cut.
- Made with: sloosh-motion-director

### Zoom-through

- Looks like: the camera flies forward through shot A and comes out into shot B.
- Use when: one idea leads straight into the next, deeper idea.
- Timing: the exit grows to 1.2 times and blurs over about 12 f (0.2 s). The entry grows from 0.75 times to full size over about 30 f (0.5 s).
- Check: the entry does not start slow. Blur on text clears within 6 f.
- Made with: sloosh-motion-director

### Partial slide cut

- Looks like: both shots slide a short way in the same direction, and the cut hides inside the motion.
- Use when: two related screens or cards follow each other.
- Timing: both sides move the same short distance, about 230 px, for the same time, for example 24 f. The exit fades out early.
- Check: the distances and lengths match. The exit is gone before the entry arrives.
- Made with: saas-product-video

### Word waterfall

- Looks like: one line of text hands over to the next line word by word, so only one line is on screen at a time.
- Use when: a film says several short lines in a row.
- Timing: line A leaves at half its entry stagger, 3 to 4 f per word, over about 16 f. Line B starts on the beat once line A is half gone.
- Check: two full lines never show at once and the words do not collide.
- Made with: kinetic-typography

### An exit that reverses its entrance

- Looks like: an element leaves the way it came, along the same path, mirrored in time.
- Use when: an element must leave without a plain fade.
- Timing: the exit is shorter than the entrance, for example 14 f. If the element came from behind an edge, it tucks back behind that moving edge.
- Check: the mask moves with the element. A fixed mask lets the element poke out.
- Made with: kinetic-typography

### Words become the mark

- Looks like: each word of the payoff line gets an underline. The underline swells into a solid block that covers the word, and the blocks fly together into the pieces of the logo.
- Use when: the last line of the film should turn into the brand.
- Timing: the underline draws over about 16 f. It swells into a block over about 12 f while the letters fade under it. The blocks fly into the logo over about 20 f and land with a small squash.
- Check: underline the words. Never strike them through. The letters never poke out above the block.
- Made with: morph-shapeshift or kinetic-typography
