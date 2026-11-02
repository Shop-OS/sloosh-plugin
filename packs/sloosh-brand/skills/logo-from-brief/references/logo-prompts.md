# Logo prompts

Use this file with the `logo-from-brief` skill. It holds the direction list, the prompt grammar, the refine and variation prompts and the fixes.

## Directions

Agree up to three directions per round. Each direction has one idea. Make them distinct from each other.

| Style | What it is | Good for |
|---|---|---|
| Wordmark | The full name set in custom type, no symbol. | Short names, fashion, beauty, editorial brands. |
| Lettermark | One to three initials as a compact mark. | Long names, app icons, monograms. |
| Symbol plus wordmark | One simple symbol beside or above the name. The default. | Most new brands. Splits into an icon later. |
| Emblem | The name inside a badge, seal or crest. | Craft, food, drink, heritage brands. |
| Mascot | A simple drawn character. | Playful, kids-adjacent or community brands. Not a real person. |

A direction line names the style and the one idea, such as "symbol plus wordmark: a single leaf folded into a drop".

## Concept prompt grammar

```
Logo design for "<BRAND NAME>" spelled exactly, <style>.
The symbol: <one idea>. Geometric, even stroke weight, no gradients, no shadow, no 3D.
Colours: <colour 1> on <background colour>; also readable in solid black.
Flat vector look, centred, generous margin, plain background, no mockup, no extra text, no tagline.
```

- Put the brand name first, in double quotes, followed by "spelled exactly".
- Name one idea for the symbol. Two ideas make a busy mark.
- Give colours as hex codes or plain names. For mono first, write "solid black on white".
- Do not name another brand, logo, mascot or designer. Describe the look in plain words, such as "rounded geometric sans, wide letter spacing".
- Use 1:1.

## Refine prompts

Change one thing per round. Pass the pick as the reference asset.

```
Change only <the one change, such as the letter weight to thinner strokes>.
Keep the spelling, layout, colours, spacing and symbol identical to the reference.
```

Examples of one change:

- "Change only the symbol: remove the leaf."
- "Change only the letter spacing: wider."
- "Change only the colour of the symbol to <hex>."

## Variation prompts

Make each variation from the approved PNG as the reference. Each one is its own quote.

| Variation | Prompt |
|---|---|
| Mono black | "The same logo exactly as the reference, in solid black on a plain white background. No other change." |
| Mono white | "The same logo exactly as the reference, in solid white on a plain <dark colour> background. No other change." |
| Horizontal lockup | "The same symbol and wordmark as the reference, set side by side on one line, symbol on the left. No other change." Use 16:9 or 3:1 if the model offers it. |
| Icon only | "Only the symbol from the reference, centred, no text, generous margin." Use 1:1. |

## Fixes

| Problem | Fix |
|---|---|
| The name is misspelled. | Pick a model whose description says it renders text well. Put the name first, in double quotes, with "spelled exactly". If it still fails, make the wordmark alone, then add the symbol in a refine round. |
| The mark drifts during a refine round. | Make a smaller change. Add "keep everything else identical to the reference". Pick a model that keeps unchanged areas. |
| The result is a mockup scene, not a flat logo. | Add "flat vector look, no mockup, plain background". |
| The mark is busy or hard to read small. | Remove one element. Ask for thicker strokes and fewer details. |
| The mark looks like a known brand's logo. | Drop that idea. Write a new one-line idea and quote again. |
| The Space asks for inputs the brief does not have. | Fill them with the brief's defaults and tell the user. |

## Delivery

- Files are raster PNG. A designer traces the approved PNG to make a vector file.
- Name each file by brand, direction and version, such as logo leaf v2.
- Remind the user to run a trademark search in each market before they use or register the mark.
