# The Remotion route

Read this file when the engine choice is Remotion. The film folder from the director's new_film.sh stays the home of the film. The Remotion project is one subfolder in it. tl.py stays the one timeline.

## Before you add Remotion

- Tell the user the Remotion license rule from SKILL.md once, before you scaffold the project.
- Ask the user before you add Remotion to the project. Say which packages you will add: remotion and the Remotion CLI package, at one exact version, plus react and react-dom. Add nothing else without a new question.
- Use the package manager that the user already uses. Look for its lock file in the film folder or its parent. If there is none, ask the user which one to use.
- Take packages only from the public npm registry. Do not add a package globally. Do not run a package's own setup wizard.
- If the user says no, use the HTML route. Tell the user that the film keeps the same timeline, gates and master.
- Node.js must already be on the user's computer. If it is missing, tell the user and use the HTML route.

## Layout

```
<film>/
  tl.py, tl.json        the one timeline (python3 tl.py writes tl.json)
  audio.py, edit.py     the director's score and compositor
  fonts/ plates/ clips/ the director's fonts; Sloosh or user stills and clips
  out/                  every render, versioned
  remotion/
    package.json        the Remotion packages at exact versions
    remotion.config.ts  the render defaults (codec, pixel format)
    public/             copies of fonts/, plates/ and clips/ (copy again after a change)
    src/index.ts        registerRoot(Root)
    src/Root.tsx        one Composition, id Film, sized from tl.json
    src/timeline.ts     reads tl.json; the only place that turns seconds into frames
    src/fonts.ts        loads the fonts before the first frame
    src/scenes/*.tsx    one component per section of the beat map
```

Copy the folders into public/ rather than linking them. A render bundles public/, so never put frames/ or out/ in it.

## The one timeline in Remotion

src/timeline.ts imports tl.json and exports frame numbers. No other file holds a number of seconds or frames.

```ts
import tl from "../../tl.json";

export const FPS = tl.FPS;
export const f = (seconds: number) => Math.round(seconds * tl.FPS);
export const LEN = f(tl.LEN);
export const DROP = f(tl.DROP);
export const T_PAY = f(tl.T_PAY);
export const T_END = f(tl.T_END);
export const BEATS = tl.BEATS.map(f);
export const TYPE = Object.fromEntries(
    Object.entries(tl.TYPE).map(([k, v]) => [k, (v as number[]).map(f)]),
);
export const COPY = tl.COPY;
export const SIZE = { width: tl.W, height: tl.H };
```

- Set resolveJsonModule to true in the project's tsconfig.json, so the import type-checks.
- Root.tsx gives the Composition durationInFrames LEN, fps FPS, and the width and height from SIZE.
- Each scene is a Sequence with from and durationInFrames taken from timeline.ts.
- After you change tl.py, run python3 tl.py again before the next render.

## Rules for every frame

- Every value comes from useCurrentFrame() and the timeline. Use interpolate with extrapolateLeft and extrapolateRight set to clamp, and spring with the composition's fps.
- No CSS animations or transitions, no timers and no requestAnimationFrame. They run on the clock, not on the frame.
- No Math.random(). Use random() from remotion with a fixed seed string.
- Show images with Img and clips with OffthreadVideo, with staticFile() paths into public/.
- Load fonts in src/fonts.ts: call delayRender, load each .woff2 from public/fonts with the FontFace API, add it to document.fonts, then call continueRender. Use only the fonts in the film's fonts/ folder or fonts the user owns.
- Measure text before you place it. Fit each line to the safe width of the format.
- Build exact UI as components from the user's real screens. Never invent UI, numbers, reviews or claims.
- Put no audio in the composition. audio.py makes and muxes the score afterwards.

## Stills, drafts and renders

Run the Remotion CLI through the project's own package runner, from the remotion/ folder. Never run it with a package runner that downloads a package on the fly.

- **Style stills:** use the CLI's still command with the entry point src/index.ts, the composition id Film, a frame number from timeline.ts (for example the hook, DROP, T_PAY and T_END) and an output path in out/stills/. Make a sheet of them with the director's sheets.py, or look at each file.
- **Draft:** use the CLI's render command with the entry point, the composition id Film, the scale option at 0.5 and the output out/<name>_draft_vN.mp4. Render only a range of frames with the frames option when you work on one section.
- **Full render:** the render command at scale 1 with the H.264 codec, the yuv420p pixel format and, if the installed version has the option, the bt709 colour space. Write it to out/<name>_vN.mp4.
- Then mux the score: python3 audio.py out/<name>_vN.mp4. It writes out/<name>_vN_final.mp4.
- Then run the gates and the master checks in `references/gates.md`.

## When a render fails

- A timeout on the first frame is often a font or an image that never loads. Check each delayRender has its continueRender.
- A blank frame at a cut is often a Sequence whose from or durationInFrames is off by one. Take both from timeline.ts, never by hand.
- If the CLI is missing, the packages are not in the project. Ask the user again before you add them.
