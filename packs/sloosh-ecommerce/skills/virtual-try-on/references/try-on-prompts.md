# Try-on prompts and checks

Use this file for the direct path and for the result check. Write each prompt in three parts in this order: the identity line, the product line and the guard line. Pass the person photo as reference 1 and the product photo as reference 2. For a new pose, pass the pose photo as the last reference: reference 2 with no product photo, or reference 3 with one.

## Routes by product

| Product | What to search for with `list_spaces` | Direct path when no Space fits |
|---|---|---|
| Top, dress, kurta, shirt, outerwear | virtual try-on | Yes |
| Glasses or sunglasses | glasses try-on | Yes, but a Space keeps the frame scale better |
| Necklace, earrings, ring, bracelet | jewellery on model | Yes |
| The same person in a new pose | pose transfer | Yes, with the pose photo as the last reference |
| A full outfit from a flat lay | flat lay on model | Use the `fashion-lookbook-set` skill for several poses |
| Two garments at once, a bag or a hat | none | Yes |

## Garment skeleton

```
The person in reference 1, with the same face, hair, skin tone, pose, framing and background, now wears the [garment] from reference 2.
Keep the garment's exact colour, print placement, texture and fit. The sleeves and the hem fall naturally for this pose. Keep the original light direction.
Nothing else changes. No text, no extra accessories.
```

## Eyewear and jewellery skeleton

```
The person in reference 1, with the same face, hair, expression, pose, framing and background, now wears the [frames / necklace / earrings / ring] from reference 2.
Fitted at natural scale with correct contact points: [the nose bridge and the ears / the collarbone / the ear lobes / the finger]. Realistic reflections on the metal and the lenses. One of each item, no duplication.
Nothing else changes. No text.
```

## Pose skeleton

```
The person in reference 1, with the same face, hair, clothes and background, now stands in the pose of the figure in the last reference.
Copy only the pose. Do not copy the face, the body or the clothes of the last reference.
Nothing else changes. No text.
```

## Fixes for the next round

| Problem | Change |
|---|---|
| The garment colour shifts | Add the flat lay or a ghost mannequin photo as a second product reference. Name the colour in plain words. |
| The face changes | Put "the same face exactly as reference 1" first. Use fewer scene words. Try another model from `list_models`. |
| The frames float or look too big | Use a glasses Space if one fits. Add "frames at natural scale, resting on the nose bridge, arms to the ears". |
| The jewellery doubles | Add "one necklace only" or "one earring in each ear". |
| The print moves | Add "the print sits in the same place as on reference 2". |

## Result check

- Identity: the same face, hair, skin tone and expression as the person photo.
- Scene: the same pose, framing, background and light direction, unless the user asked for a new pose.
- Product: the exact colour, print placement, texture, logo and trims.
- Fit: plausible at the shoulders, the waist, the sleeves and the hem. Fabric folds follow the pose.
- Anatomy: five fingers on each hand, natural arms and neck, no merged hair and fabric.
- Eyewear: the frames rest on the nose bridge, the arms reach the ears and the scale matches the face.
- Jewellery: one of each item, at natural scale, with the correct contact point and no floating chain.

## Craft rules

- Do not crop or reframe the person photo unless the user asks.
- Name the garment type plainly, such as a linen kurta or a wool overcoat.
- For a garment, the person's body must be visible. For eyewear or jewellery, the face, the ears or the neck must be visible.
- For eyewear and jewellery, name the contact points: the nose bridge and the ears, the collarbone, the ear lobes or the finger.
- For a first look, use a lower resolution if the model offers one. Use the full resolution only for the approved look.
