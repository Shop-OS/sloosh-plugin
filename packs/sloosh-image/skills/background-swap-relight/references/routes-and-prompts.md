# Routes and prompts

## Choose the route

| Situation | Route | Search for | Why |
|---|---|---|---|
| A real scene photo and a product | A product-in-scene or relight Space | product-in-scene or relight | It places the product into the photo instead of making a new scene. The product stays exact. |
| A described setting and a product | A background Space that takes a product photo and a setting description. If none fits, the direct path, with the product as reference 1 | background change for a product | A described setting needs new surroundings around the product. |
| A product, a scene photo and a person | Direct path, with a model that takes three references | No search. Go to the direct path. | Several references in one image. |
| A portrait and a described setting | A change-background Space | change-background | Made for people. It keeps the face. |
| Only the light should change | A relight-from-reference Space | relight-from-reference | It keeps the pose and the framing. |
| Several light moods for a portrait | A portrait lighting variations Space | portrait lighting variations | Several setups for one quote. |

If the user names no setting, suggest a seamless studio with a soft key light from the left.

Search for each Space with `list_spaces` and choose it by its description. Space names and ids change, so do not rely on a fixed one.

## Prompt template for the direct path

```
The product from reference 1, placed on [surface] in [setting in one line], at the scale of a real [object].
Light: [direction] [hard or soft] [colour], from [the window on the left / the light in reference 2]; shadows fall [direction]; soft contact shadow under the product.
Product, label, colours and proportions exactly as reference 1; only the surroundings and the light change.
[Lens] lens, [camera angle], product [share] of the frame, empty space on the [side]. No text, no extra products.
[One line from the brand kit about mood or palette, if there is one.]
```

## Example briefs

- "Put this candle on a marble bathroom counter with window light." Direct path, 4:5, the candle as reference 1. Check the shadows.
- "Place my bottle into this photo of our cafe and match the light." A product-in-scene Space with both photos. Check the contact shadow and the colour temperature.
- "Relight this portrait like the reference." A relight-from-reference Space. Compare the light direction and softness with the reference.

## Quality bar

- Shadow direction on the subject matches the scene.
- Colour temperature on the subject matches the scene.
- A contact shadow is present under a product.
- The scale is believable.
- The label, the logo and the face are unchanged.

## Craft rules

- Describe the light in three parts: the direction, the quality (hard or soft) and the colour.
- Name the light source in the scene, such as the window on the left. Say which way the shadows fall.
- Say that only the surroundings and the light change. Say that the subject stays exactly as in the reference.
- Give the scale in real terms, such as the size of a real candle on a counter.
- Ask for no text and no extra products.
- Draft at a low resolution to find the direction. Make the final at full resolution only for the approved direction.

## Fixes

Each fix needs a new quote, a new approval and a new key.

If a fix adds a reference photo that is not the user's own, ask the rights question again before the new quote. If the new photo shows a person, ask the consent question again too.

- The product floats: add "resting on the surface with a soft contact shadow and a slight reflection".
- The light fights the scene: use a Space with the scene photo, or add a light reference.
- The label is soft: add a close-up crop of the label as an extra reference.
- A face changed on a portrait: use a change-background Space. A direct model can redraw a face.
