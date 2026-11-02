# Effects and the Spaces to search for

Published Spaces change on the server. Search for them each time with list_spaces. Choose by the description that list_spaces or get_space returns, not by a name in this file. The ratio and length columns are typical. The Space's description and input schema are the truth.

## Effect map

| The user wants | Search terms | Typical ratio and length | Works best for | Inputs to expect |
|---|---|---|---|---|
| Features labelled while the camera orbits | feature callout, orbit | 9:16, about 8 s | any product with three selling points | up to three features of four words or fewer |
| Parts fly apart and come back | exploded view | widescreen, about 5 s | tech, gadgets, shoes, anything with internals | a clean packshot on white |
| A smooth turn on its axis | 360 orbit, product spin | 16:9, about 5 s | hero banners, product pages | one clear front photo |
| A weightless float with ingredients around it | zero gravity, float | 9:16, 4 to 10 s | beauty, food, drink | what floats around the product |
| A paper wall tears to reveal the product, with sound | tear-away reveal | 9:16 | launches, offers | a brand colour |
| A plunge and a splash, with sound | splash, pour | 9:16 | cans, bottles | the liquid or medium |
| A box opens and the product steps out in stop motion | stop motion, unpack, unboxing | about 8 s | packaged goods | the pack photo |
| A press, a squish and a bounce back | crush, squish | 9:16 | soft goods, sneakers | what presses |
| A knife cuts the product to show it is cake | cake reveal | 9:16 | sneakers, bags, bottles | a cake flavour |
| A pop-up cardboard world around the product | cardboard world | 9:16, about 6 s | playful brands | a backdrop idea |
| Any other product effect | no Space; use the direct path | the model's limits | any product | the effect in one sentence |

If two rows fit, offer both in plain words and let the user choose.

These requests belong to other skills:

- A product placed in a scene with a camera move and no product effect belongs to the core product video skill.
- A plain product page loop with no product effect belongs to the core product video skill.
- Several clips of one product for an edit belong to the cinematic product film skill of this pack.

A seamless loop is an option only for a named effect in this map.

## Prompt template for the direct path

Write the motion only. The start frame already shows the product.

```
The [product] exactly as the first frame, label readable throughout. [One move: a slow 90 degree orbit / a pedestal rise / a macro push-in on the cap / the parts drift apart and settle back]. [Physics, if any: condensation forms, fabric settles]. [Light: direction and quality]. Background [plain / described]. No text, no hands, no extra objects. [Sound: one soft foley sound, or none].
```

- Say "exactly as the first frame" first.
- Use one move per clip.
- For a loop of a named effect, end on the start pose and pass the same photo as the end frame.

## Fixes for common faults

| Fault | Fix |
|---|---|
| The label drifts or warps | Use a cleaner photo: plain background, higher resolution. Make a clean packshot first if needed. |
| A callout is misspelled | Shorten it to four words or fewer. |
| Parts do not go back in place | Use a packshot on white, and ask for fewer parts. |
| The Space is missing or changed | Search again. Offer the direct path. |
| The hold is more than the allowance left | Give the user the settings link. Offer a shorter length or another Space. |
