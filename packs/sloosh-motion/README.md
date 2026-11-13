# Sloosh motion films

![Sloosh](assets/sloosh.png)

Sloosh motion films makes stylised short films on your computer: product reveals, beat-synced edits, software walkthroughs and feature announcements, kinetic typography, glitch, dot-matrix and morph films. It also edits your own talking-to-camera footage into a finished cut. It adds sixteen skills to the core Sloosh plugin. One skill directs the film and picks the style. Seven skills make each style. One skill builds a film entirely in code, in Remotion or HTML pages. One skill edits a talking-head take: it cuts pauses and false starts and adds captions, camera moves and kinetic type. One skill cuts a long talking video, such as a podcast, into several vertical shorts, and edits each one with that skill. Five skills help around the film: animated charts, still plates, vertical exports, a style guide and shot list from a reference video, and a catalog of named motion effects. The style guide and the catalog cost nothing and work in any host. Claude plans the film on a beat grid, builds the type and interface layers as HTML, composites the frames in Python, adds synthesised sound and checks the result with ffmpeg. When a shot is missing, Claude can make stills and clips with Sloosh. Claude shows you the quoted credits for each round of Sloosh work and asks for your approval before it spends.

The pack never posts a film and never uploads to a social account. Every number in an animated chart stays exactly as you give it.

## What you need

- A coding agent that runs commands on your own computer, such as Claude Code. The films render locally. In the Claude app, only animated-chart and motion-plates work. For other video work there, use the core Sloosh plugin's video skills.
- Python 3.9 or later with numpy, OpenCV and SciPy, and ffmpeg.
- Playwright with its Chromium browser, to render the HTML type layers, charts and overlays.
- For auto-edit and long-video-to-shorts: macOS on Apple Silicon with the Xcode command line tools. Apple Vision makes the speaker matte and the face and hand tracks. On another system, auto-edit makes only the transcript and the cut, and long-video-to-shorts makes centre-cropped shorts without captions.
- For auto-edit and long-video-to-shorts: a local speech-to-text model on your computer, such as mlx-whisper or faster-whisper with its model folder. Claude asks you before it installs a transcriber or downloads a speech model.
- For a Remotion film only: Node.js. Claude asks you before it adds Remotion to the film project. Remotion needs a company license for companies with more than three employees.
- Optional: rembg for product cutouts, and Kokoro or Piper for a voice-over.
- For Sloosh shots: the core Sloosh plugin, installed and connected, and a Sloosh workspace with spending enabled.
- The right to use every photo, logo, video, track and reference that you give Claude. Claude asks you to confirm this before it quotes any work that uses them.

Claude asks you before it installs anything, and it suggests a virtual environment. The pack's scripts never download or install anything by themselves.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-motion@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh motion films. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-motion folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

In the Claude app, animated-chart gives you an HTML page that plays the loop, and motion-plates makes still plates. The film skills need a coding agent on your computer.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-motion@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| sloosh-motion-director | The entry point. It picks a style, writes a treatment with a beat map, sets up the film folder and runs the shared engine. It can also match a reference video. | Paid |
| product-reveal | A launch film for one physical product: light sweeps, macro details, word slams and a packshot end card. | Paid |
| aura-farming-edit | A fast, beat-synced edit of one person, athlete, car or product, with speed ramps, flashes and bold type. | Paid |
| saas-product-video | A walkthrough or a short feature announcement, built from your real product screens. | Paid |
| kinetic-typography | A words-only film in six presets, such as offers, quotes, lyric videos and end cards, or a beat-synced caption layer for another film. A photo plate from Sloosh is optional. | Free |
| glitch-fx | A glitch film with signal loss, RGB splits, scan lines and HUD type, or glitch transitions for another film. | Paid |
| morph-shapeshift | A film where one subject becomes the next with no cut: outfit, product, shape, UI and logo morphs. | Paid |
| dot-matrix-particles | A dot-matrix, LED, halftone, ASCII or particle film, or one of these effects as a layer on another film. | Paid |
| animated-chart | A seamless loop of a bar chart, trend line, count-up or milestone, as an HTML page, an MP4 and a GIF. A Sloosh still or plate is optional. | Free |
| motion-plates | Matched still plates in 16:9, 9:16 and 1:1: backgrounds with room for type, textures, cut-outs and logos in a material. | Paid |
| motion-film-code | A motion film built entirely in code, with no voice-over: a type, UI or vector-logo sting, a seamless loop, or a scored 20 to 45 s film with exact UI and words. It renders in Remotion or HTML seek(t) pages on your computer, with optional Sloosh plates and clips. | Paid |
| auto-edit | A finished vertical or wide cut of your own talking-to-camera footage, edited on your computer: pauses and false starts cut, word-by-word captions, camera moves, depth of field, kinetic type and a mastered mix. A Sloosh world edit of the room and sound from a Space are optional. | Paid |
| long-video-to-shorts | Several vertical shorts cut from one long talking video you own, such as a podcast or a webinar, on your computer: Claude ranks the best moments, you choose, and each short gets a crop that follows the speaker's face and word-by-word captions. Paid steps happen only inside auto-edit, with their own approval. An optional voiceover comes from the soundtrack-and-voice skill in the sloosh-video pack, with its own quote and approval. | Free |
| reel-export | A 1080x1920 vertical version of a finished video, with a hook and logos in the safe zone. A vertical cover still from Sloosh is paid. | Free |
| reference-to-motion | A style guide and a shot list from a reference video you own or may study: pacing, cuts, camera, type, colour, sound and what not to copy. It hands the plan to motion-replicate or a film skill. | Free |
| motion-effects-library | A lookup catalog of over 400 named motion effects: what each one looks like, when to use it, its timing and the skill that makes it. | Free |

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. Claude uses its colours, fonts and logo. A brand kit is optional.

## How a film is made

1. Claude asks for the brief: the product, the words, the format (9:16, 16:9, 1:1 or 4:5), the length and any music you have.
2. Claude sets up a film folder in your project. It holds the timeline, the type layers, the fonts, the shots and the output.
3. Claude writes the treatment and the timeline on the beat grid and makes placeholder shots, so you can see the cut before any spending.
4. If shots are missing, Claude plans Sloosh stills or clips in rounds of up to eight, quotes each round and waits for your approval.
5. Claude renders, mixes the sound and checks every frame of the final file.

## What the pack sends and reads

The film work runs on your computer and stays in your project folder. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp only for Sloosh stills, clips and plates, with the prompts and images you approve, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace, and Claude downloads the ones the film uses into the film folder.

The pack reads only what you give it: photos, logos, screens, videos, tracks, numbers and references that you paste or upload. It does not post films or upload them to a social account.

## Spending

Sloosh uses the credits and the daily spending allowance of the workspace you connect. Claude gets a quote for each item before it makes anything. For each round, Claude shows each item with its quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. Claude cannot raise the allowance, buy credits or change your plan. A film made only from your own photos and footage costs nothing in Sloosh. Animated charts, kinetic type and vertical exports cost nothing unless you ask for a Sloosh still or plate.

## Fonts and third-party code

The pack ships six open font families under the SIL Open Font License 1.1: Archivo, Inter Tight, Instrument Serif, Bodoni Moda, Fraunces and JetBrains Mono. Each licence text is beside its fonts. The morph skill ships flubber under the MIT License, with a notices file for the code it bundles. The effects catalog is written from video-shotcraft (Apache License 2.0), motion-graphics-skills (MIT) and cinetic (MIT), with their licence texts in its notices file. It ships no code from them.

## Example prompts

- "Make a 12-second dark luxury product reveal of our perfume bottle, 9:16."
- "Cut a 20-second hype edit of our new trainer to this track."
- "Make a 30-second walkthrough video of our dashboard app, 16:9."
- "Make a feature announcement film for our new auto-resize feature."
- "Make a kinetic typography video with these four lines, on the beat."
- "Animate our quarterly orders as a bar chart loop for an Instagram post."
- "Make three background plates for our serum film in 16:9 and 9:16, with room for type."
- "Turn this 16:9 launch video into a Reel with the hook Hand-poured, small batch."
- "Break down the style of this reference clip I own into a shot list we can reuse."
- "Which motion effect should I use for a price reveal?"
- "Build a 6-second seamless feature loop for our landing page in code."
- "Auto-edit this selfie take I shot: cut the pauses and add word-by-word captions, 9:16."
- "Cut my 50-minute podcast episode into five vertical shorts with captions."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
