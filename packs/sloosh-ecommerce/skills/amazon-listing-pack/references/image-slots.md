# Listing image slots

Each slot is one square 1:1 image. Pass the product photo as reference image 1 in every prompt. Replace each part in square brackets. Use only the user's facts, word for word.

| Slot | Purpose | Text in the image | Needs |
|---|---|---|---|
| Main | Shows exactly what the buyer gets. | None. | The product photo. |
| Lifestyle | Shows the product in use, in a real place. | None. | The product photo. A setting from the brand kit. |
| In-hand scale | Shows the true size. | None. | The product photo. |
| Macro detail | Shows texture, material or a key part. | None. | The product photo. A detail the user names. |
| Feature callouts | Shows up to three facts next to the product. | Up to three short callouts. | The product photo. Three facts in the user's words. |
| What's in the box | Shows each item the buyer gets. | None, or one short label per item. | The product photo. Photos of each item, or the box contents from the facts. |

## Prompt shapes

Main:

```
Square 1:1 product photo. The product from reference 1, exactly as shown, centred on a pure white background. The product fills most of the frame. Even, soft studio light. The label reads exactly as in the reference. No text, no props, no shadow, no badges, no logos besides the product's own.
```

Lifestyle:

```
Square 1:1 lifestyle photo. The product from reference 1, exactly as shown, in use in [a setting from the brand kit]. Natural light. The product is the clear subject and the label faces the camera. No added text, no badges.
```

In-hand scale:

```
Square 1:1 photo. The product from reference 1 held in an adult hand at its natural size, on a plain light background. Soft daylight. The label faces the camera. No text.
```

Macro detail:

```
Square 1:1 close-up photo of [the detail the user names] on the product from reference 1. Shallow depth of field. True colour and texture. No text.
```

Feature callouts:

```
Square 1:1 listing image. The product from reference 1, exactly as shown, large on the left, on a [brand secondary colour or light grey] background. On the right, three short callouts with thin leader lines to the product: "[fact 1]", "[fact 2]", "[fact 3]". Spell each callout exactly. Dark text, simple sans type. No other text, no badges, no awards, no claims, no logos besides the product's own.
```

What's in the box:

```
Square 1:1 top-down flat lay on a plain light background. The product from reference 1 and [each item in the box], laid out neatly with even space between them. Soft, even light. No other items. No text.
```

## Checks for each slot

- Main image: pure white to each edge, the product fills most of the frame, the label is exact, and no added text, prop, badge or watermark.
- Secondary images: each callout matches the user's facts word for word, spelled exactly. No invented icons, seals, awards or rank claims.
- The product matches the reference in colour, shape and label.
- No word appears that the user did not give.
- No item appears in the box image that the user did not list.
- No marketplace logo, badge or award seal appears.

## Craft rules

- One product per image.
- Use the same light and the same brand colour in every secondary image, so the set looks like one shoot.
- Put at most three callouts in one image, with at most four words each. Use plain dark sans text on a light background.
- In the scale image, show the product in an adult hand at its natural size, with the label to the camera.
- Do not put a marketplace logo, a marketplace badge, a "best seller" label or an award seal in any image.
- Pick the largest output size the model lists. If the long side is below the marketplace's minimum, tell the user.
