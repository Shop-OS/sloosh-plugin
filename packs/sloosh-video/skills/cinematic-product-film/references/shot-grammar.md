# Shot grammar for a cinematic product film

Use this file to write the storyboard, the keyframe prompts and the shot prompts. Model limits come from list_models. Prices come from the quote.

## Shot arc

A product film of 4 to 8 shots, 3 to 5 seconds each, often follows this arc. Change it to fit the brief.

| Shot | Picture | Camera |
|---|---|---|
| 1. Reveal | The product comes out of dark or haze. Light finds the edge first. | Slow push-in |
| 2. Macro detail | Texture, cap, label edge or material, very close. | Slow slide or rack focus |
| 3. In hand or in use | A hand lifts, sprays, pours or opens the product. | Locked or gentle handheld |
| 4. Product in its world | The product in a place that shows the mood: a vanity, a desk, a rock by the sea. | Slow orbit or dolly |
| 5. Hero float | The product alone, centred, with rim light and a slow turn. | Slow orbit |
| 6. End frame | The product still, with clear space for a logo or a line added in the edit. | Locked |

## Storyboard row

Write each shot as one row:

- Shot number and seconds.
- Picture: what the frame shows, in one sentence.
- Camera: one move only.
- Message: what the shot says to the viewer.
- Cut: how it meets the next shot (a cut on action, a match on shape, a light flare, a push through).

State the total length and the aspect ratio once, for the whole film.

## Continuity block

Write the block once. Paste it word for word into every keyframe and every shot prompt.

> Continuity: the same [product] as reference 1 in every frame, same label, same [colour] cap. Lighting family: [soft key from left, warm]. Grade: [warm neutral, soft grain]. Palette: [two colour names]. No text, no captions, no logos other than the label.

Keep the same reference images on every keyframe. This raises the chance that the product stays the same. It does not promise it.

## Keyframe prompt

> Shot [n] of [total]. [Subject and what it does]. [Place]. [Light]. [Lens, angle and distance]. [Composition, with space where the edit adds text]. [Continuity block].

From mood references take only the palette, grain, lens look and light. Leave their subject, logos and text. Write: "Match the palette, contrast and grain of references 2 to 4. Product, label and framing from reference 1."

## Shot prompt

The keyframe is the start frame, so describe only motion and change. Do not describe the still again.

> Shot [n] of [total]. Starts on the first frame[, ends on the last frame]. [One action in one clause]. Camera: [one move]. [Seconds] seconds. [Continuity block]. Sound: [named sounds, such as a soft spray or glass on stone], no music.

- Pass the shot's keyframe as the start frame. When the cut must flow and the model takes an end frame, pass the next keyframe as the end frame.
- Pass the product photo as a reference only if the model takes references with frames. Otherwise pass the frames alone.
- With an end frame, describe the change between the two frames.
- Say "no text" or give the exact words. Models invent captions otherwise.
- For a person, write "the same person as in reference 2, same hair, same top".

## Length by placement

| Placement | Good length | Notes |
|---|---|---|
| Reels, TikTok, Shorts ad | 9 to 15 s | 9:16. Show the product by second 3. Add captions in the edit for sound-off viewing. |
| Meta feed video | 6 to 15 s | 4:5 or 1:1. Most people watch muted. Add captions in the edit for sound-off viewing. |
| YouTube pre-roll | 15 to 20 s | 16:9. Show the brand in the first 5 seconds. |
| Website hero | 6 to 10 s | 16:9. Silent loop. |
| Brand film or launch spot | 30 to 60 s | 16:9. More shots, not longer shots. |

For 9:16 placements, keep the product and any text added in the edit out of the top 14%, the bottom 35% and 6% at each side of the frame.

## Test cut

Before the final round, offer a cheaper test cut: a lower resolution or a faster model that list_models lists. Quote it and get approval like any round.

## Check each clip

The agent cannot watch a video. Ask the user to watch each clip in the card or at its link and run these checks. The agent can compare only stills with view_asset.

| Check | Pass | Fix |
|---|---|---|
| Product | Shape, label and colour match the reference | Add a second angle, less motion, the same continuity block |
| Light and grade | Matches the shots before and after | Restate the lighting family and grade |
| Text | No invented words on screen | Add "no text" |
| Cut point | The last frame meets the next shot | Use the next keyframe as the end frame, or cut on action |
| Motion | Natural, no warping | Drop the end frame, ask for one slower move |

Every fix is a re-shoot: a fresh quote, a new approval and a new key.
