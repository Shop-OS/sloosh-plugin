# Edit prompts

Each edit prompt has three parts in this order: the one change, the keep-list and the guard line. Write the change first and in one sentence. Name the exact place in the image.

## Skeleton

```
Change only [the price tag on the left side of the table: remove it and fill the space with the same wooden table surface].
Keep everything else identical: the product, the label, the lighting, the shadows, the background, the framing and the colours.
Do not add objects or text.
```

## Patterns by change

| Change | The change sentence | Notes |
|---|---|---|
| Remove an object | Remove [the object] from [place] and fill the space with [the surface around it]. | Name the surface, such as "the same white marble". The fill must continue its texture and light. |
| Fix or replace text | Change the text on [the front label] to read "[EXACT TEXT]". Keep the font, size, colour and position. | Copy case and spelling exactly. Use as few words as you can. Check it letter by letter after. |
| Change one colour | Change the colour of [the cap] to [plain colour name]. Keep its material, shine and shadows. | Name only the one item. Use a brand colour from the brand kit when one exists. |
| Insert a logo or object | Add [the logo] from reference 2 onto [the front of the box] in reference 1, flat, following the box's perspective and lighting. | Pass the source first and the insert second. |
| Add a prop | Add [one small sprig of rosemary] beside [the bottle, on the right], in the same light and shadow direction. | One prop per pass. Keep it smaller than the product. |
| Clean a surface | Remove the dust, fingerprints and small scratches on [the glass]. Keep its reflections and edges. | Do not remove real design marks or embossing. |
| Skin retouch | Remove only temporary marks on the skin, such as spots and stray hairs. Keep pores, freckles, moles, scars and natural lines. | Never slim, reshape a body or change the face. Needs the person's consent first. |
| Cut out the subject | Remove the background and keep [the product] on a plain white background with clean edges. | A direct edit may not return a transparent background. For transparency, use a background remover Space. Hair, fur, glass and straps are soft spots. |
| Clean a cut-out edge | Clean the edge of [the product]. Remove any halo. Keep the plain white background. | Run this on a solid-backdrop result, not on the source. For a transparent cut-out, run the background remover Space again. |
| Tone only | Make the whole image [slightly warmer / brighter / less saturated]. Change nothing else. | Keep the change small. Name one direction. |

## When the edit drifts

- If more changed than you asked for, cut the prompt to the change sentence, the keep-list and the guard line. Remove any style words.
- If text is still wrong, use fewer words in the new text. Match the case of the original label. If the model has a quality field in `list_models`, quote again with its highest choice.
- Chain small edits on the latest output, not on the source. Each pass is a new quote and a new key.
