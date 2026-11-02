# Brand board page prompts

Use these prompts on the direct path, one page per prompt. Replace each part in capitals, such as BRAND, with the brand's own words. Use only headline and body sample words the user approved. Keep the brand name and every hex code in double quotes so the model copies them exactly.

## Pages in a full board

| Page | What it shows | Ratio | What to check |
|---|---|---|---|
| Palette | Three to five large swatches, each with its name and hex code | 4:5 or 1:1 | Every hex is readable and matches the kit |
| Typography | A headline sample and a body sample in the type feel, with the type names as words | 4:5 | Words are spelled right; samples are legible |
| Mood | Four photographs in a 2x2 grid that show the brand's world | 4:5 or 1:1 | Light, palette bias and subjects follow the photo rules |
| Lockup | The logo on a light and a dark field, with clear space around it | 1:1 | The logo is the reference, not a redraw or a recolour |
| Overview | A one-page tile: logo, swatches, a type sample and two mood photos | 4:5 | All of the checks above |

Start with the palette page. The other pages use its confirmed hexes.

## Palette page

```
A clean brand board page for "BRAND", 4:5, white background.
Five large colour swatches in a row: NAME "#HEX", NAME "#HEX", NAME "#HEX", NAME "#HEX", NAME "#HEX".
Under each swatch, print its hex code exactly, in small grey text.
Top left: the logo exactly as reference 1, no redraw, small.
Top right: the word "Colour" in a TYPE FEEL typeface.
Flat layout, generous margins, no photos, no other text.
```

## Typography page

```
A clean brand board page for "BRAND", 4:5, off-white background.
A large headline sample that reads "HEADLINE WORDS" in a TYPE FEEL display typeface.
Below it, one short line of body text that reads "BODY SAMPLE" in a plain, readable TYPE FEEL text typeface.
A small label that reads "Type" at the top left. Accent colour "#HEX" for the label only.
Flat layout, generous margins, no photos, no logo, no other text.
```

## Mood page

```
Four photographs in a 2x2 grid that show the world of BRAND: SCENE 1, SCENE 2, SCENE 3, SCENE 4.
LIGHT FROM THE PHOTO RULES. PALETTE BIAS FROM THE PHOTO RULES, close to "#HEX" and "#HEX".
Thin white gutters between the photographs. No text, no logo, no recognisable people.
```

## Lockup page

```
A brand board page for "BRAND", 1:1.
Left half: a light field "#HEX" with the logo exactly as reference 1, no redraw, centred, with wide clear space.
Right half: a dark field "#HEX" with the light version of the logo exactly as reference 2, no redraw.
No other text, no shadows, no mockup.
```

Use this prompt only when the user supplies a light or reversed logo file. Pass it as reference 2. Without one, do not ask the model to recolour the logo. Put the logo exactly as reference 1 on a mid-tone field "#HEX" for the right half. Or leave the right half blank for a designer to place the real file.

## Overview page

```
A one-page brand style tile for "BRAND", 4:5, white background, in a clean grid.
Top: the logo exactly as reference 1, no redraw.
Middle: four colour swatches with their hex codes printed exactly: "#HEX", "#HEX", "#HEX", "#HEX".
Lower left: the word "BRAND" set as a headline in a TYPE FEEL typeface.
Lower right: two small photographs that show SCENE 1 and SCENE 2, LIGHT FROM THE PHOTO RULES.
Generous margins, no other text.
```

## Fixes for a page that misses

- Hex codes are garbled: use fewer swatches (five at most) and larger text. Put each hex in double quotes.
- The logo is redrawn: put "the logo exactly as reference 1, no redraw" first in the prompt. If it still changes, make the page without the logo and leave a blank area for it. Tell the user a designer can place the real file.
- Extra words appear: end the prompt with "no other text".
- The mood photos clash with the palette: name the two hexes the light and props must lean toward.
