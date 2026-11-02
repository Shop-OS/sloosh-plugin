# Brand icon set prompts and checks

Use these on the direct path, one prompt per sheet. Replace each part in capitals, such as BACKGROUND HEX, with the brand's own values. Keep every hex code in double quotes so the model copies it exactly.

## Make each name drawable

An icon shows one object or one simple sign. Rewrite an abstract name into an object before you write the prompt. Confirm the rewritten list with the user in one message.

| The user writes | Draw instead |
|---|---|
| Quality | A rosette or a check in a shield |
| Fast shipping | A delivery van with motion lines |
| Easy returns | A box with a curved return arrow |
| Vegan | A leaf in a circle |
| Cruelty-free | A rabbit outline |
| Dermatologist tested | A dropper over a small shield |
| 30-day guarantee | A calendar page with a check |
| Recyclable | Three arrows in a loop |
| Secure payment | A padlock on a card |

Do not put numbers or words inside an icon unless the user asks. A model often misspells them.

## Write the style spec

Look at the logo with `view_asset`. Write one line that a model can follow. Name the stroke, the joins and corners, the fill and the colours.

- Line logo: "2 px even stroke, rounded joins and ends, no fill, ink "#1F3A2E" on "#E8DCC8", no gradients".
- Solid logo: "solid filled shapes, soft 4 px corner radius, one colour "#C2410C" on "#FFFFFF", no outlines".
- Two-colour logo: "outline in "#1E293B" with one flat accent fill in "#38BDF8", same stroke weight everywhere".

If the user picks a style that differs from the logo, write the spec for that style and keep the logo's colours.

## Sheet prompt

```
A 3x3 grid of nine icons on a plain "BACKGROUND HEX" background, nine equal square cells, generous padding in each cell.
Draw every icon in the style of the logo in reference 1: STYLE SPEC.
No text, no labels, no numbers, no shadows, no gradients.
Icons, left to right, top to bottom: 1 NAME, 2 NAME, 3 NAME, 4 NAME, 5 NAME, 6 NAME, 7 NAME, 8 NAME, 9 NAME.
One icon per cell. Each icon is one clear object with the same visual weight, centred in its cell.
```

For fewer than nine icons, change the grid size, the icon count and the cell count in the first line to match. Keep the sheet square, so keep the cells square. Use 2x2 for up to four icons and 3x3 for five to eight. Leave the last cells empty. Say which cells stay empty, such as "the bottom right cell stays empty".

## Fix one tile

```
Keep this icon sheet exactly as reference 1.
Change only the icon in the CELL POSITION cell to NEW OBJECT, drawn in the same style: STYLE SPEC.
Keep the other icons, the grid, the background and the colours identical.
No text, no labels.
```

On a 3x3 sheet, name the cell as top left, top centre, top right, middle left, centre, middle right, bottom left, bottom centre or bottom right. On a 2x2 sheet, name it as top left, top right, bottom left or bottom right.

## Quality checks

- Each icon reads as its name at a small size. Squint at the sheet to test it.
- The icons are in the order of the list, one per cell.
- The stroke weight, corner radius and colours are the same on every icon.
- The colours match the logo or the brand kit hex codes.
- No stray text, labels or numbers appear.
- The grid is even. No icon touches the edge of its cell.
- The sheet is a PNG image, not a vector file. Tell the user that a designer can trace it to SVG.

## Fixes for a sheet that misses

- Icons are out of order or merged: number them in the prompt and keep "One icon per cell". Use fewer icons per sheet.
- Labels appear under the icons: put "No text, no labels" first in the prompt.
- The style drifts from the logo: pass the logo as reference 1 and give the stroke weight in px. If the model takes no reference images, pick another model from `list_models`.
- One icon is weak or wrong: fix that tile with the fix prompt above. Do not remake the whole sheet.
- The colours shift: quote every hex code in double quotes and remove other colour words.
