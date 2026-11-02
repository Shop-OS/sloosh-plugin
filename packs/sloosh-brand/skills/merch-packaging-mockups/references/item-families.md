# Item families, prompts and fixes

Use this file with the `merch-packaging-mockups` skill. Space names change, so search with `list_spaces` and choose by each Space's description. Never pick a Space from memory.

## Item families

| Family | Examples | Search terms for `list_spaces` | What the user must give |
|---|---|---|---|
| Merch | caps, tees, totes, hoodies, mugs | merch mockup | The logo, ideally a PNG with a transparent background. The item colours. |
| Packaging | pouches, bottles, jars, cartons, tins | packaging mockup | Flat label or box art. The pack type. |
| Box from a dieline | a folding carton | dieline, box from dieline | One flat printed dieline image with clear fold lines. |
| Label concepts | a first label design around the existing logo, when no label art exists yet | label design | The logo. The exact brand name, product name, size and any facts the label must show. |
| Print and cover | a magazine cover, a box and a print ad | magazine cover, print packaging | A product photo the user may use and the product name. |
| Stationery | business cards, letterhead, envelopes | business card, stationery | The exact name, title, phone, email and address for each card. |
| Out of home and screens | billboards, bus stops, posters in frames, phones | poster mockup, billboard | The finished design at full size. |
| Material logo | the logo in metal, wood, glass or stone | textured logo, material logo | The logo and, if the Space asks, a photo of the material. |
| Anything else | a water bottle, a neon sign, a van wrap, a shop sign | none | The artwork and a short scene. Use the direct path. |

For a magazine cover, a billboard, a bus stop or a shop sign, use a made-up or blank masthead. Do not name a real magazine, publisher, store or media owner.

Default "merch" to three items: a cap, a tote and a tee. Ask before you add more.

## Direct path prompt

Write one prompt per item. Fill each slot. Pass the artwork as reference 1.

```
Photoreal product mockup: <item, such as a matte black steel water bottle> on <surface> in <light, such as soft daylight from the left>.
The artwork from reference 1 printed on the <face or panel>, exactly as reference 1, no redraw, correct perspective, following the surface curve, <finish, such as matte screen print>.
<brand kit line: background colour as a hex code, props, mood>
No other text, no other logos. 50 mm lens, eye level, product fills about 70% of the frame.
```

- Put every word the item must show in double quotes and add "spelled exactly".
- For apparel, name the fabric and the print method, such as "heather grey cotton tee, white screen print".
- For packaging, name the material and finish, such as "kraft paper pouch, matte label, gold foil logo".
- For a scene with people, show hands or a cropped figure. Do not show a recognisable face.
- Use 1:1 or 4:5 for a presentation. Use 16:9 for a billboard scene.

## Quality checks

- The artwork is not redrawn. Letterforms, colours and proportions match the original.
- The print sits on the surface. It follows curves, folds and seams with believable perspective.
- The material looks real: fabric weave, paper grain, glass reflections, metal highlights.
- The scene has no invented text, no extra logos and no watermark.
- Text on a label or card matches the user's text letter by letter.
- On a dieline box, the panels meet at the right edges and nothing is upside down.
- No real magazine, publisher, store or media owner name appears. Mastheads are made up or blank.
- The ratio fits the use: 1:1 or 4:5 for a presentation, 16:9 for a billboard scene.

## Fixes for a near miss

- Logo redrawn or letters shifted: quote again with the output as reference 1 and the artwork as reference 2. For a Space output, use the asset from `import_asset` as reference 1. Write "Keep the scene. Replace the printed artwork with reference 2 exactly, no redraw." If it still drifts, offer the user one more quote at a flat front-facing angle, where the print wraps less.
- Card or label text wrong: on the direct path, pick a model whose description says it renders text well. Put the text in double quotes with "spelled exactly". Use fewer words per card.
- Dieline box misfolds: check that the dieline is one flat image with clear fold lines and no crop marks in the art. Ask the user for a clean export. Then quote it again, ask for a new approval and use a new key.
- Colours drift from the kit: put the exact hex codes in the Space's colour field, or in the prompt on the direct path.

## Hand-off notes

- Say that these are presentation images, not print-ready files.
- Say that print needs the original vector artwork and the printer's own template.
