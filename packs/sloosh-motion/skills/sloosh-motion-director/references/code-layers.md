# Code layers: UI, type and the compositor

## UI, logos and product animation, built as code

UI walkthroughs, toggles, logo morphs, cursors, chips, counters and cards are one HTML page per piece, rendered frame by frame. No model touches them, so the text is sharp, the logo is correct and every click is exact.

- **The page:** ui/<piece>.html holds every element as a layer and defines window.render(t), which sets every transform, opacity, blur and colour for time t. No CSS animations, no timers, no real time.
    - Load the helpers with a script tag for /lib/kit.js: K.E.out, K.E.inOut, K.E.back and K.E.spring easing, K.kf keyframes, K.set, K.mblur directional motion blur, K.cursor, K.typeOn, K.shine, K.counter and K.measure.
    - Set window.READY = true after the images and fonts have loaded.
- **Render it** from the film folder:

```bash
python3 lib/render_html.py ui/type.html --dur <LEN> --out frames/type
python3 lib/render_html.py ui/ui.html --dur 11 --scale 2 --out frames/ui
```

  The output is a transparent PNG sequence (or an opaque MP4 with --opaque --mp4). The page server listens only on 127.0.0.1. In edit.py, fk.Overlay("frames/ui", start=T_UI, speed=UI_SP) places it on the film timeline (UI_SP = natural length / section length).
- **Place cursors by measuring the target element** (getBoundingClientRect, after the scene's camera transform). Typed coordinates put the cursor on the wrong row.
- **Brand assets:** use the user's real logo file and real colours. Vectorise a raster logo (upscale it, split it into colour masks, trace the contours with OpenCV into an SVG), so it stays sharp at any size. Rebuild icons as SVG shapes measured from the logo, so parts can move. Never redraw a logo by hand when the file exists, and never ask a model to draw it.
- **UI motion grammar** (use what the style asks for): a 3D window entrance from a tilt with a spring; a macro zoom onto a chip and a click that squashes it; a menu pop with overshoot; a pan down a sidebar with vertical motion blur; a connect button that sparkles and then shows a check mark; a photo that flies in large and lands as a thumbnail; typing with the newest letters in the accent colour; a toggle that switches the footage on the frame of its click.

## The type system

One family, two lockups, strict placement. A different font per slam and overlapping words look amateur. The fix is a system.

- **Default family:** Archivo, italic, width 125 %, weight 900, for every hype word (font-stretch:125%; font-weight:900; font-style:italic). Inter Tight for UI text and end-card lines. A style skill may swap the family (Bodoni Moda for a luxury fragrance, Instrument Serif for editorial, JetBrains Mono for a HUD) but keeps the discipline.
- **Colours:** white plus one accent. A second colour is only for the logo and the end-card rules.
- **Lockup A, the two-line stack** (K.lockupA): bottom-left of the safe zone, never centred over the subject. Line 1 in white at 118 px; line 2 in the accent at 168 px, tucked up into line 1 (-0.13 em). In: a left-to-right mask wipe over 0.16 s (line 2 starts 0.07 s later) and a 36-50 px slide with a quartic ease-out. Out: a wipe and slide to the right over 0.2 s. A soft dark shadow keeps it readable on bright footage.
- **Lockup B, the echo stack** (K.echo): a huge accent hero word (about 260 px on a 1080-wide frame) at 42 % of the height, scaling from 1.25 to 1.0 as it lands. Three outlined white copies cascade below it with falling opacity. A small word sits above it, widely tracked.
- **Slam** (K.slam): one word on a beat, scale 1.35 to 1 with blur 12 to 0 in 4 frames.
- **End card** (K.track): the title tracks in from 0.62 to 0.40 em, and accent rules grow out from the centre. A small line of spaced capitals sits below.
- **Measure, never guess.** Load the fonts first (document.fonts.load), measure each word's rendered width, and place it from that measurement. Shrink any line that is wider than the safe zone. Guessed positions draw words on top of each other and clip lines at the frame edge.
- **Safe zones:** on 9:16, keep the product and text out of the top 14 %, the bottom 35 % and at least 6 % at each side (the lockups sit about 11 % in from the left), plus a right column about 17 % wide from 44 % of the height down (feed buttons sit there). On 16:9, keep 5.4 % clear on each side, 8 % at the top and 9 % at the bottom. On 1:1 and 4:5, keep 7 % clear on each side, 8 % at the top and 12 % at the bottom. No text under 28 px. Words never cover the subject's face or another word, and every wipe finishes on screen.
- **Type and picture together:** whole-frame hits (HITS in tl.py: negative, red duotone, smear) are applied after the type, so they hit the text too. Voice lines land on the slams.

ui/type.html is a working example of this system. It reads the copy, the cue times and the colours from tl.json.

## The compositor and the edit grammar (edit.py)

One script computes every frame from the timeline and pipes raw frames into ffmpeg (libx264, CRF 18). Every effect is code, so it is exact and repeatable. lib/filmkit.py documents every tag and transition at its top.

- **Footage:** fk.CutList(SHOTS, beats=tl.BEATS, fx_from=DROP, fx_to=T_END). Every row is (start, end, source, in_point, speed, zoom_from, zoom_to, focus_x, focus_y, tags). The source is a video, an image or "black". A vertical clip goes into a horizontal frame with the tag vert_full (cover-crop, slightly high) or vert_blurbg (centred over a blurred, darkened copy).
- **Stills feel like footage:** every still used as a shot gets a handheld micro-rotation and the slow zoom, so nothing reads as a photo.
- **Per-frame order:** the shot and its source time (speed ramps), the camera (an eased zoom around a focus point, shake or punch), the look tags, the cut grammar, light leaks, then in edit.py the type overlay, the whole-frame hits, the finish (contrast, vignette, bloom, grain) and the flash frames.
- **Cut grammar on every cut:** the outgoing shot's last 2 frames zoom x1.06 with a radial zoom blur; the incoming shot's first 3 frames zoom from 1.12 to 1.0 with a decaying zoom blur and a 14 px shake; a 2-frame brightness flash. The tag hard skips it (the breath and deliberate smash cuts).
- **Hyper effects on the beat** (from the drop, while the payoff runs): a zoom punch on every beat, a colour split on every downbeat, single red-monochrome or inverted frames on some beats (the style sets the budget), grain on everything and a vignette on everything except UI.
- **Effect tags:** punch, ramp, red, pink, teal, warm, duo, bwflick, smear, glitch, zblur, shake, negative, leak, whiteout, flat, flash, freeze, reverse, stutter, hard, locked, pushin. The recipes are in lib/filmkit.py.
- **Transitions:** a rush into a screen (zoom 1 to 1.9 with zoom blur, fade to white); a white flash; fk.whip (a horizontal blur over 3 frames); an inverted frame with a settling colour split (fk.rgb_split); a psych strobe; fk.shockwave on a logo slam; fk.mosaic_wipe between worlds.
- **Figure lock:** measure a figure's centre and height in every clip, smooth them, and scale and move each frame so that the figure sits at the same spot and size in every world.
- **Before and after:** the before is flat (the tag flat, normal speed, a small BEFORE tag). The after has every beat effect on. The contrast sells it.
