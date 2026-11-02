# Film engine: the film folder, the toolchain and the fallback

Paths are relative to the sloosh-motion-director skill's folder. In commands, `<director>` means that folder. Commands that start with lib/ run inside the film folder, which holds its own copy of lib/.

## Requirements

- Python 3.9 or later with numpy, opencv-python (or opencv-python-headless) and scipy.
- ffmpeg.
- Playwright for Python with its Chromium browser.
- Some styles also use Pillow, or rembg for product cutouts.
- A voice-over needs Kokoro or Piper with a local voice, or a voice file from the user.

Ask the user before you install anything. The scripts download nothing and install nothing. The fonts come vendored in assets/fonts/, and new_film.sh copies them into the film.

## The film folder

```
1 study references --> 2 story on a beat grid (tl.py) --+--> 3 camera shots (Sloosh: still, then clip)
                                                         +--> 4 UI, logo and type as HTML, rendered to PNG frames
                                                         +--> 7 score, SFX and voice (audio.py)
                    5-6 compositor and grade (edit.py) <-- all three --> 8 QA by looking --> deliver
```

One timeline drives three parallel builds: the camera shots, the coded type and UI, and the synthesised audio. They meet in one compositor, and nothing ships until the contact sheets pass.

**Scaffold a film** with `scripts/new_film.sh`, from the user's project folder:

```bash
bash <director>/scripts/new_film.sh <product>_<style> 9x16      # or 16x9 | 1x1 | 4x5; optional fps (30 by default, 24 for some 16:9 films)
```

It creates:

- tl.py: the timeline, the copy and the cues
- edit.py: the compositor
- audio.py: the score, SFX, voice-over and master
- ui/type.html: the type layer
- lib/: filmkit.py (the compositor toolkit and effect tags), audiokit.py (the synth score, SFX, voice-over and master), render_html.py (HTML to PNG frames), sheets.py (contact sheets) and kit.js (easing, keyframes, lockups, cursors, measuring)
- fonts/: every vendored font and its licence text
- refs/, plates/, clips/, frames/, out/ and audio/

It prints any missing Python module and ffmpeg. Ask the user before you install them.

**Fonts.** All six families are under the SIL Open Font License 1.1. Their licence texts are in assets/fonts/ and are copied into the film's fonts/ folder. Never ship a font file without its licence text.

| Family | Files | Use |
|---|---|---|
| Archivo (variable: width 62-125 %, weight 100-900) | archivo-latin-wdth-normal.woff2, archivo-latin-wdth-italic.woff2 | heavy wide hype words |
| Inter Tight (variable: weight 100-900) | inter-tight-latin-wght-normal.woff2, inter-tight-latin-wght-italic.woff2 | UI text, end-card lines, captions |
| Instrument Serif (400) | instrument-serif-latin-400-normal.woff2, instrument-serif-latin-400-italic.woff2 | editorial serif headlines |
| Bodoni Moda (500 and 600) | bodoni-moda-latin-500-normal.woff2, bodoni-moda-latin-500-italic.woff2, bodoni-moda-latin-600-normal.woff2, bodoni-moda-latin-600-italic.woff2 | luxury serif |
| Fraunces (variable: weight 100-900) | fraunces-latin-full-normal.woff2, fraunces-latin-full-italic.woff2 | soft editorial serif |
| JetBrains Mono (500, and variable weight 100-800) | jetbrains-mono-latin-500-normal.woff2, jetbrains-mono-latin-wght-normal.woff2 | HUD, terminal and code text |

lib/render_html.py serves the film folder as the site root, so a page loads a font from /fonts/ with its exact file name:

```css
@font-face{font-family:'Archivo';src:url('/fonts/archivo-latin-wdth-italic.woff2') format('woff2');font-style:italic;font-weight:100 900;font-stretch:62% 125%;font-display:block}
@font-face{font-family:'Bodoni Moda';src:url('/fonts/bodoni-moda-latin-600-normal.woff2') format('woff2');font-style:normal;font-weight:600;font-display:block}
```

**Engineering habits that keep the quality high:**

- Each film is one editor script with a pure render(t): the same t always gives the same frame. Random effects (grain, glitch slices) are seeded by the frame number, so a re-render matches exactly.
- Every editor has a stills mode for fast checks, `python3 edit.py out/sheet.jpg 1.2,3.4,9.0`, and a video mode that pipes raw frames into ffmpeg.
- Before any spending, preview the cut on placeholders: `FILMKIT_PLACEHOLDERS=1 python3 edit.py out/sheet.jpg 0.5,2,6.4`. Each missing shot renders as a dark card with its file name.
- Source clips are decoded on demand and cached. In-between times blend two frames, so speed ramps stay smooth.
- Render UI at 2x when the edit pushes into it (render_html.py with --scale 2), so text stays sharp at a 2-2.8x zoom.
- Version, never overwrite: v1, v2, v3.

## If the helper files are missing

Never fall back to one-shot generation. Rebuild the minimum in the film folder:

- edit.py: decode the clips with OpenCV; a render(t) that picks the shot from a cut list, applies an eased zoom (cv2.warpAffine with a black border), the cut grammar, the tags you need and the contrast, vignette and grain finish, and composites PNG overlays by alpha; pipe raw frames to ffmpeg (rawvideo, bgr24, libx264, CRF 18).
- An HTML page with window.render(t), and a Playwright loop that calls render(i / fps) and takes screenshots with a transparent background.
- audio.py: NumPy oscillators, an envelope and a filter, kick, clap, hat and 808, a noise whoosh and impact, and a two-pass ffmpeg loudnorm to -14 LUFS.
