# Engine choice: route each shot, pick the build, stack styles

The rule behind every row: words and marks are code; matter and light are Sloosh. Pick by what each shot needs, never by a model name. Model choice stays with list_models at quote time.

## 0. Pick the style

| Style skill | Pick it when the brief says | Default |
|---|---|---|
| the `product-reveal` skill | product reveal, packshot, launch teaser for one product, perfume, gadget, shoe, make my product look premium | 12-15 s, 9:16 |
| the `aura-farming-edit` skill | aura edit, hype edit, main character, velocity, phonk, a montage cut to a track, athlete or car edit | 15 s, 9:16 |
| the `saas-product-video` skill | software, app, dashboard, website, product demo, explainer; also a new feature, we shipped, update, changelog, launch post | walkthrough 20-30 s, 16:9; announcement 10-15 s, 1:1 or 9:16 |
| the `kinetic-typography` skill | words only, quote, offer, lyric video, typographic ad, manifesto | 10-20 s |
| the `glitch-fx` skill | glitch, cyber, VHS, datamosh, signal loss, glitchy transitions | a layer, or 6-15 s |
| the `morph-shapeshift` skill | morph, shapeshift, A turns into B, liquid, logo morph | 6-15 s |
| the `dot-matrix-particles` skill | dot matrix, halftone, LED, ASCII, particles, made of dots | a layer, or 6-15 s |

Feature announcements are part of the `saas-product-video` skill. When the brief names no style, pick the closest base style and offer one alternative in the intake. For example, a product launch with a track can be a product reveal or a hype edit. When a brief fits two styles, one is the base (the story and the pacing) and the other is an effect layer (section 3). "Recreate this reference" works with any style (`reference-study.md`).

## 1. Route each shot

Give every row of the beat map one route.

| Route | Use it for | Made by |
|---|---|---|
| code | type, UI, charts, counters, exact logos, anything that must be pixel-true | an HTML page with window.render(t), rendered to PNG frames (`code-layers.md`) |
| Sloosh still | a hero set, a background, a detail macro, a still that the edit moves with a handheld drift and a slow zoom | a quoted image round (`camera-shots.md`) |
| Sloosh clip | physics, liquid, cloth, light, a product that turns, a person who moves | a quoted video round, animated from an approved still |
| user footage | the user's own photos, screen recordings or clips | the user, imported or copied into the film folder |

Never route a logo, a UI, a caption or a title to a Sloosh clip. Video models drift letters and marks.

## 2. Pick the build

Most films are hybrid: a code film with Sloosh stills and clips as layers. The director's engine (tl.py, edit.py, audio.py) builds all of them. The style skill adds the look.

| The piece | Build | Why |
|---|---|---|
| A launch teaser or packshot film for one physical product | the director's engine with the `product-reveal` style | the real cutout keeps the label exact |
| A software walkthrough, app demo or feature announcement | the `saas-product-video` style, with real screenshots rebuilt as HTML | never invent screens |
| A hype, aura or montage edit cut to a track | the `aura-farming-edit` style | beat-locked cuts and ramps |
| Words as the whole picture, an offer, a quote, a lyric video | the `kinetic-typography` style, all code | glyph fidelity |
| A logo sting where the mark must stay crisp | code (the `morph-shapeshift` code route or a kinetic type end card); for a material moment, a texture from one Sloosh still with the real logo file masked onto it in code | a video model drifts logos |
| A to B with no cut, a liquid or shape change | the `morph-shapeshift` style | start and end frames from approved stills |
| Glitch, VHS or signal-loss hits | the `glitch-fx` style, as the base or as a layer | all damage is code, frame by frame |
| Dots, LED, halftone, ASCII or particles | the `dot-matrix-particles` style, as the base or as a layer | footage is clean; code makes the dots |
| Data, charts, numbers, KPIs | the `animated-chart` skill | values must not change |
| Backgrounds, textures and cut-outs for another editor | the `motion-plates` skill | matched plate sets by shot id |
| Raw talking-head or selfie footage the user shot, cut into a captioned edit | the `auto-edit` skill | it cuts on whole words and mattes the speaker |
| A finished wide film that needs a vertical version | the `reel-export` skill | safe-zone hook and a clean upload encode |
| A voice-over-led launch film over 30 s, or a Remotion project | the `launch-film` skill of the core plugin | it owns Remotion and match cuts |
| One generated clip of a product, with no edit | the `product-video` skill of the core plugin | no film needed |
| A published Space that already makes the whole piece, and exact type is not needed | the `published-spaces` skill of the core plugin | one run, no local build |

When the user has no shell on their computer, only the last two rows work. Say what is lost: no exact type, no beat-locked edit and no mastered score.

## 3. Stacking styles

One base style owns the story and the pacing: a product reveal, a hype edit, a software film or kinetic typography. Up to two effect layers may be added: glitch, morph, dot matrix, or kinetic type as the caption layer. A layer:

- fires on beats and transitions only (glitch hits of 6 frames or less, about 3-5 in 15 s)
- uses the base palette and the type system
- never covers the product or the key line while it is read

In code, a layer is extra tags in the cut list, an extra transition function, or an extra HTML overlay.

## 4. Sound route

- The default is an original score and SFX from audio.py (`sound-library.md`). It needs nothing from Sloosh.
- A voice-over comes from a local text-to-speech engine (Kokoro or Piper) with a local voice, or from the user's own voice file. The scripts never download a voice. If none is installed, ask the user before you install one. If the user says no, make the film without a voice-over.
- A track or SFX file from the user enters the film only with the user's confirmation of the rights.
- Place one to three hits, each caused by something visible. Leave silence before the payoff.
