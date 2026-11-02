# Plate prompts, checks and fixes

Use this file with the motion-plates skill. Pick each model from list_models. Do not pick a model from this file or from memory.

## Plate kinds

| Plate kind | What to look for in the model list | Size | Notes |
|---|---|---|---|
| Studio background, flat design surface | A model that makes clean, even graphic surfaces | 2K | Flat and even. Ask for "no gradient banding, subtle grain". |
| Photoreal surface (slate, linen, water, concrete) | A model strong at photoreal detail that offers 4K | 4K | State one light direction. |
| Texture tile | A model that takes a seed | 1K to 2K | Ask for "seamless, tileable, uniform lighting". |
| Product cut-out | A background remover Space on a clean product still | Native | Leave the shadow off. The code adds it. |
| Hero render with a 3D look | A model that takes two or three product reference images and offers 4K | 4K | "Studio CGI look, soft HDRI light, product exactly as the reference." |
| Logo in a material | A logo or material Space, with the logo file and a material photo (metal, wood, stone, fabric) | Native | The vector logo stays in the code layer. Use it for a hero moment only. |
| User interface | Do not generate it | | Capture real screens. |

## Prompt grammar for a background or surface

```text
[Kind] for a motion graphics background. [Surface and material], [light: one direction, quality, colour], camera [straight on / 15 degrees top-down], [ratio].
Composition: [left / right / top] [third / half] completely empty and plain for typography. No text, no letters, no logo, no objects other than [list]. Flat, even exposure, no vignette, subtle film grain, no gradient banding.
[Brand line from the brand kit]
```

## Cut-out source still

```text
The [product] from reference 1 on a flat mid-grey background, even light, no shadow, no reflection, full product in frame with a 10% margin, label facing the camera, keep the label and the shape exactly.
```

Then run the background remover Space on that still, or on the user's own product photo when it already has a plain ground.

## Set consistency

- Write the first plate's light and material sentence once. Copy it word for word into every later plate.
- Change only the composition between plates.
- Keep the same model, the same reference set and, where the model takes one, the same seed.
- For a 9:16 version, pass the approved 16:9 plate as a reference and ask for "the same scene, taller framing".

## Checks for every plate

- No text, no letters and no logo unless the plate asks for one.
- The empty zone is really empty.
- The light direction and the horizon match across the set.
- The 16:9 and 9:16 versions sit side by side with no clash.
- The product shape, label and colours match the real photo.
- 4K exists for every plate that the camera pushes into, crops or match-cuts.
- Say which plates are illustrative and do not show the real product.

## Fixes

| Problem | Fix |
|---|---|
| The model adds text or logos | Put "no text, no letters, no logos" first in the prompt. Try a model that makes clean graphic surfaces. |
| Banding in a gradient | Ask for grain and even light. Or dither the gradient later in the code layer. |
| A halo on the cut-out edge | Run the remover again on a source with more contrast against the ground. Or use a mask or segment Space from list_spaces on the named object. |
| Only one named part is needed, such as the cap or the shoes | Search list_spaces for a mask or segment Space and name the part. |
| 9:16 does not match 16:9 | Make 9:16 from the 16:9 plate as a reference, "same scene, taller framing". Or use an aspect ratio Space. |
| The model has no 4K | Make the plate at 2K, then use an upscaler Space. |
| The product changed | Add a second reference angle. Say "keep the label and the shape exactly". Reject the plate. |

## Handoff block

For each plate, list: shot id, kind, ratio, size, file name (shot id, ratio and size, such as bg01_16x9_4k.png), model, seed if used, and whether it is illustrative.
