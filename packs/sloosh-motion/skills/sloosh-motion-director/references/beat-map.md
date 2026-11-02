# Beat map: the idea, the beats and the grid (tl.py)

Write this before any spending and before any code. It goes into the treatment that the user approves. It costs nothing.

## 1. The format row

Pick one row. It sets the length, the cut pace and the word budget. The style skill's default wins when it has one.

| Format | Length | Grid | Notes |
|---|---|---|---|
| Launch teaser for one product | 10-20 s | 92-130 BPM | the whole product lands on the drop at 50-60 % of the film |
| Hype or aura edit | 12-25 s | 130-150 BPM | cuts on every beat after the drop |
| Software walkthrough | 20-30 s | 118-124 BPM | the UI sections run at their natural length, stretched to the grid |
| Feature announcement | 10-15 s | 118-128 BPM | one feature, one before and after |
| Feature loop | 6-15 s | whole bars | the last frame matches the first frame, so the loop has no seam |
| Logo sting or end card | 6-8 s | 100-128 BPM | the mark stays vector, built in code |
| Social vertical | 9-15 s | per style | the hook lands inside the first second |

The engine renders 30 fps by default (24 for some 16:9 films). A film over 30 s, or one led by a voice-over, is a job for the `launch-film` skill of the core plugin.

**Word budget:** at most 35 words per 30 s, at most 5 words per line and at most 2 lines on screen at once. Cut words before you shrink type.

## 2. The idea comes from specifics

1. **Specifics first.** Write down what the name evokes, the product's own objects (its card, its row, its bottle, its dropper), its verb, and the one behaviour that is not obvious ("unlike the obvious version, it..."). The idea comes from these, never from a style.
2. **Three ideas of different kinds.** (a) The product's verb made literal. (b) The viewer's pain made visible. (c) A formal device: a relay object, a bookend, one unbroken camera move, or a container that becomes the product.
3. **Two tests.** The cover-the-logo test: would the film be just as true of a competitor? If yes, it is not the idea yet. The deletion test: remove the demo beats. Does the value still read? Pick one idea and say why in one line. Write it in 15 words or fewer.
4. **The device.** One object or shape travels through every shot and never blinks out at a cut.
5. **The accent.** One accent colour with one meaning. It covers under about 8 % of the pixels and floods the frame at most once.

## 3. The beat map

Write the story as beats first: hook, build, breath, drop or key moment, payoff, end card. The hook starts inside the problem by 1 s. Show one or two capabilities as proof, then the promise, then the lockup. Nothing holds still for more than 1 s except the final hold (0.6-1.4 s). The drop lands on the key visual moment.

Show it to the user as a table:

| bar | time | picture | copy | sound | route |
|---|---|---|---|---|---|
| 1 | 0.0-1.0 | macro of the dropper, rim light | (none) | low riser | Sloosh still and clip |
| 2 | 1.0-2.6 | the device crosses the frame | "Meet Halcyra" | whoosh on the cut | code |

The route column uses the routes in `engine-choice.md`. The device appears in every row. Every on-screen fact has a source from the user or the product. Drop any metric, claim, review, price or offer that has no source from the user. A label does not make it allowed. Only sample interface data in a demo, such as fictional rows or names, may carry an "Illustrative" label.

## 4. Lock the beats in tl.py

| Variable | Meaning |
|---|---|
| BPM, B | the tempo and one beat |
| DROP | the key moment, on a bar line |
| T_BREATH | 3-4 frames of black and silence before the drop |
| T_PAY, T_END, LEN | the payoff, the end card and the film length |
| BEATS | every beat, aligned so that a bar line hits the drop |
| TYPE | the cue times of every lockup, slam and end card |
| COPY | the exact on-screen strings |
| HITS | whole-frame hits that also hit the type |
| VO | the voice lines |
| GENRE, KEY | the score's genre and key (any major or minor key, for example F#m, Bb or Ebm) |

Run `python3 tl.py` after each change. It writes tl.json for the HTML pages.

Rules that make the film feel edited, not assembled:

- Every section boundary after the drop is a whole number of beats from the drop.
- Render a UI or animation section at its natural length, then stretch it slightly (x0.97 to x0.99) to fit the grid. Never cut it short. Convert its SFX cue times with ui2t(u) = T_UI + u / UI_SP, so that every click sound lands on its click frame.
- Cut one frame before the beat. The flash or the impact peaks on the beat.
- Cut density has a shape: the intro holds, the build gets faster, the drop cuts on every beat, and one long hold resolves it. Never use one uniform pace.
- Place one to three hand-placed hits, each caused by something visible. Leave silence before the payoff.

## 5. The gate before the treatment goes out

- The idea is 15 words or fewer, and it passes the cover-the-logo test.
- The word count is inside the budget, and no line has more than 5 words.
- The device is in every beat row, and every shot has a route.
- Every on-screen fact has a source from the user. No unsourced metric, claim, review, price or offer is on screen, labelled or not.
- Nothing is spent yet.
