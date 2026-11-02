# Logo reveal recipes

Use these recipes with the direct path of the logo-animation skill. Pick the model with `list_models` first. Check its prompt length, start frame and end frame support, duration and ratios. Replace each part in square brackets.

## Routes

| Mark | Route | Risk |
|---|---|---|
| Bold icon, chrome or 3D look | A published Space found with `list_spaces` | The Space decides the motion and the length. |
| Clean icon or short wordmark, light sweep | Direct: the logo as the start frame | Low, if the camera is locked and the clip is short. |
| Icon in a material, such as brass, wood or glass | A material still first (a Space or an image), then the direct path with that still as the start frame | The still can redraw the mark. Check it before you animate it. |
| Icon that grows into the full lockup | Direct: start frame A (icon) and end frame B (lockup), only on a model that takes both | Letters can blur in the middle of the move. |
| Thin type, small text, exact kerning, transparent background | A code build, not a generated clip | None for the mark. Sloosh makes only the background plate. |

## Start frame rules

- The start frame is the logo in the centre on the brand background, at the ratio of the placement, with clear space around the logo so the camera can push in.
- Use the ratio of the placement: 16:9 for a video intro or outro, 9:16 for Reels and Stories, 1:1 for a feed post.
- No tool can pad, place or recolour an image. If the logo file is already a frame at the clip ratio with clear space around the mark, use it as the start frame. If not, make the start frame first with mode `image_gen` at the clip ratio, with the logo as reference 1 and the no-redraw wording below. That still has its own quote and approval.
- For 9:16, keep the mark out of the top 14%, the bottom 35% and 6% at each side.
- Use the largest logo file the user has. A small or soft logo gives a soft clip.

## Reveal clip prompt (start frame)

```
The logo stays exactly as the first frame: same shape, colours and proportions. A single soft light sweeps across it from left to right once over 2 seconds, revealing a subtle [material] surface. Camera locked, slight slow push-in. Background [colour] untouched. No text, no particles, no extra shapes. The logo holds still for the last second.
```

Other moves to try. These are untested suggestions. Quote and check them like any other clip:

- Light-up: the frame starts dark and the logo lights from the edges in, then holds.
- Focus pull: the logo starts soft and comes into sharp focus, then holds.
- Slow orbit: a small camera arc, for a 3D or material mark only.

Avoid these moves on a generated clip: letters that fly in one by one, a mark that breaks into particles, a fast spin and a morph between two different shapes.

## Start frame and material still prompt (image, logo as reference 1)

```
The logo exactly as reference 1, no redraw, made of [material: brushed brass, frosted glass, oiled walnut]. Same shape, same proportions, same letterforms. Centred on a plain [colour] background, soft studio light from the top left, a gentle reflection below. No added text, no extra shapes.
```

For a plain start frame, leave out the material and keep the logo flat. Ask for the clip ratio and clear space around the logo.

Check the still before you animate it: same outline, same letters, no new text, colours true to the brand.

## Lockup stills (frame A and frame B)

- Frame A: the icon alone, centred, on the brand background.
- Frame B: the full lockup, icon and wordmark, on the same background, with the icon in its lockup place.
- Make both at the same ratio and resolution. Use the logo as reference 1 for both. Write "the logo exactly as reference 1, no redraw".

## Lockup clip prompt (start frame A, end frame B)

```
Start exactly on the first frame, end exactly on the last frame. The icon slides to its place as the wordmark fades up from the icon's edge. Smooth, weighted ease, no bounce. No camera move. No new elements. The lockup holds still for the last second.
```

## Length and timing

- 3 to 5 seconds for a sting or a bumper. Up to 8 seconds for a slow material reveal.
- Hold the finished mark for the last second.
- A shorter clip keeps the letterforms more stable.

## Checks

You cannot watch a video. Ask the user to watch the clip in the result card and confirm these points. Check stills yourself with `view_asset`.

- The letterforms, shapes and colours match the logo at the start and at the end.
- No extra text, letters, particles or shapes.
- The background stays the brand colour.
- The final second is still.
- Name the clip by brand, route, ratio and version, such as tealeaf logo sweep 16x9 v1.
