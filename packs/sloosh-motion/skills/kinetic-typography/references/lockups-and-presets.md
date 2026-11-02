# Presets, type system and lockups

## Presets for the intake

| Preset | One line for the user | Default length |
|---|---|---|
| Bold Poster (default) | Huge condensed caps, paper, ink and one loud colour, a new colour block every bar, a ticker | 15 s |
| Swiss Clean | Calm bone frame, crisp grotesk, words land with colour flashes, a split-flap board, a list finale | 16 s |
| Editorial Serif | Magazine serif with one italic phrase, strike and marker, optional photo with the subject in front of the headline | 12 s |
| Lyric / Beat | A word on every beat: caps slams with serif-italic breath words, the drop on a colour block | 10 s |
| Variable Stretch | One word at a time, squeezing, swelling and skewing with the font's own axes, then a fly-through a letter | 10 s |
| Scroll List | "We design ...": items glide through a fixed band, the last one lands in colour | 9 s |

## Presets in build

| Preset | Example folder | Signature and support moves | Fields | Music |
|---|---|---|---|---|
| Bold Poster (default) | bold-poster | stack, odometer, squeeze-to-fill, slam and inversion, type-as-camera, grid, stretch-to-frame, ticker | paper, orange and ink blocks every bar | house 120 |
| Swiss Clean | swiss-clean | word land and 4 accent flashes, split-flap board, word swap, grid wave, scroll list | bone with pink and lime hazes; an ink iris for the grid | house or ambient 120 |
| Editorial Serif | editorial-serif | masthead rise and axis swell, strike, marker, end track; optional subject in front of the masthead | warm paper (dark under a plate) | luxury 90 |
| Lyric / Beat | lyric-beat | lyric engine, per-word inversions, black breath, accent-block drop, echo walk, flap index | off-black to a red drop | trap 140 or the user's track |
| Variable Stretch | variable-stretch | width 62 to 125 squeeze, axis wave and skew snaps, stretch-to-frame, fly-through the O | black to acid | techno 124 |
| Scroll List | scroll-list | stem and band list, suspense beat, payoff in the accent, mono ticker | light neutral to a cobalt end | house 120 |
| Caption layer | caption-layer | lyric captions, Lockup A, slams over any base style | the base film's | the base film's |

Defaults: Bold Poster, 9:16 1080x1920, 30 fps, 15 s, 120 BPM house, 0 generations.

## Type system

Sizes are px for a 1080 short side. The engine scales by min(W, H) / 1080.

For 9:16 feed placements, keep readable copy out of the top 14%, the bottom 35% and 6% at each side, and left of the button rail. The "reels" safe zone in lib/ktkit.js does this: it runs from 14% to 65% of the height. Hero lines fit the safe width of each format; only 9:16 has the rail, and lines below 44% of the height end left of it.

| Preset | Display (.d) | Support (.s) and accent face | Case and tracking |
|---|---|---|---|
| Bold Poster | Archivo 900, width 62 to 125 | Archivo 700 width 100 kickers 32 px, +0.3 em | caps, -0.01 em |
| Swiss Clean | Inter Tight 800 | JetBrains Mono 500 labels 32 px; Instrument Serif italic accent word | sentence, -0.045 em |
| Editorial Serif | Fraunces optical size 144, weight 380 (swell to 760) | Fraunces italic accent phrase; Inter Tight 600 kickers +0.2 em | sentence, -0.025 em |
| Lyric / Beat | Archivo 900 width 62 | Instrument Serif italic breath words; JetBrains Mono board | caps and lowercase italic |
| Variable Stretch | Archivo, width 62 to 125, weight 100 to 900, skew snaps | JetBrains Mono | caps |
| Scroll List | Inter Tight 800 lowercase rows | JetBrains Mono kicker and ticker | lowercase with a full stop, -0.05 em |
| Caption layer | Archivo italic 900 width 125 | Instrument Serif italic | caps |

## Named lockups

| Lockup | 9:16 (1080 wide) | 16:9 (1920 wide) | In and out | Placement |
|---|---|---|---|---|
| A. Poster stack | lines fitted to the safe width (cap 400 to 420), kicker 32, leading -0.02 em | fitted to the safe width (cap 420) | masked rise on beats, wipe right 0.2 s | centred in the safe zone (y 0 to 1) |
| B. Echo | hero 260 to 320 fitted, 3 outline copies at 0.66 cap, small word 44 tracked 0.3 em | same px | hero 1.25 to 1 in 0.35 s, copies cascade at 60 ms | hero at 30 to 42% of the height |
| C. Slam fill | one word fitted to the safe width (cap 460) | fitted to the safe width | 1.35 to 1 with blur 12 to 0 in 4 frames | centre |
| D. Board | tiles 150 (stat) or 34 (index) | same | tiles flip in 0.12 s, lock left to right | centre, or an index top-left |
| E. End | title 96 to 120 at final tracking, rules 140 each side, URL 30 tracked | same | track 0.62 to 0.40 em in 1.2 s (track=[from, to]) | 42 to 46% of the height |
| Caption (layer) | caps 150, serif 1.0 em, at most 3 words per row, middle band 47% to 65% of the height, left of the rail | caps 150, band 62% to 90% of the height | per-word slam or rise, hard cut on the beat | CAPTION_BOX |

## Colours

- Each field is bg, ink and one accent. The four Swiss landing flashes are the only exception, and they last 4 frames.
- Every accent has at least 3:1 contrast on its field. A brand colour replaces the accent only.
- Outline rows and dim list rows are texture. Never put the message in them.
- With a plate, type goes behind the subject only where it stays readable. Over footage, the .over-footage soft shadow (18 px, 60%) is on.
