# Ghost mannequin prompts

Use these prompts on the direct path. Write one prompt per view. Keep the light words, framing, ratio and background the same for every view and every garment in a range.

## Front view

```
Ghost mannequin product photo of the garment in reference 1, as if an invisible body wears it: shoulders and chest filled out naturally, neckline open so the inside back of the collar shows, sleeves hanging with a natural drape.
Front view, straight on, centred, <ratio>, <pure white | light grey> seamless background, even soft studio light, a faint shadow under the hem only.
Keep the fabric colour, print placement, buttons, stitching, label and proportions exactly as in reference 1. No person, no skin, no hands, no hanger, no mannequin parts, no text.
```

## Other views

Add one of these lines to the front prompt. Pass the approved front result as reference 2.

| View | Line to add |
|---|---|
| Back | Seen from directly behind. Use the back photo in reference 1. Match the scale, framing and light of the front view in reference 2. |
| Inside-neck | Close view into the open neckline from the front, showing the inside back of the collar and the label from reference 1. Match the colour and light of reference 2. With no label photo, add: blank label, no readable label text. |
| Detail | Close view of the <print, embroidery, button or zip> from reference 1, filling the frame, the same light as reference 2. |

If the user has no back photo and still wants a back view, say in the prompt that the back is plain unless the user describes it. Label the result as generated, not photographed.

## Fixes

| Problem | Fix |
|---|---|
| A hand, a shoulder or skin stays in view | Put "no person, no skin, no hands" first in the prompt. Ask for a photo cropped closer to the garment. |
| A hanger, clip or dummy stand stays in view | Add "no hanger, no clips, no stand, nothing above the collar". |
| The print moves, repeats or changes | Add a detail photo as another reference. Add "print placement exactly as in reference 1". Try another model from `list_models` that takes more reference images. |
| The collar is closed, not open | Add "neckline open, inside back of the collar visible". |
| The garment looks flat, like a flat lay | Add "three-dimensional shape, chest and shoulders filled out, slight depth at the side seams". |
| A white or pale garment loses its edges | Use a light grey background. Tell the user that a marketplace main image may need pure white. |
| The colour shifts | Name the true colour in plain words, such as deep olive green. Add "colour exactly as in reference 1". |
| The back view does not match the front | Pass the approved front result as reference 2. Use the same model and the same light words. |
