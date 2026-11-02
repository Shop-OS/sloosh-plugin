# Social profile sizes, safe zones and prompts

Sloosh makes images by aspect ratio, not by pixel size. The user sets the exact pixel size when they export or upload. Platforms change these sizes. Tell the user to check each platform's help page before the final export.

## Sizes and safe zones

| Platform | Asset | Make at | Export to (about) | Safe zone on the exported image |
|---|---|---|---|---|
| All | Profile image | 1:1 | 1080x1080 | The platform shows a circle. Keep the logo inside the middle 55% of the width, centred. |
| Instagram | Highlight cover | 9:16 | 1080x1920 | The platform shows a small circle from the centre. Keep the icon inside the middle 50% of the width, centred on both axes. |
| LinkedIn | Personal banner | widest ratio, crop to 4:1 | 1584x396 | The profile photo covers the lower left. Keep the logo and text in the right 65% of the width and the middle 60% of the height. |
| LinkedIn | Company page cover | widest ratio, crop to about 6:1 | 1128x191 | Keep the logo and text in the middle 40% of the height and out of the left 20%. |
| X | Header | widest ratio, crop to 3:1 | 1500x500 | The profile photo covers the lower left. Some screens crop the top and bottom. Keep the logo and text in the middle 60% of the height and out of the left 25%. |
| YouTube | Channel banner | 16:9 | 2560x1440 | Every device shows only the centre. Keep the logo and text in the middle 60% of the width and the middle 29% of the height. |
| Facebook | Page cover | widest ratio, crop to about 2.7:1 | 851x315 | Phones show a narrower centre. Keep the logo and text in the middle 70% of the width and the middle 60% of the height. |

"Widest ratio" means the widest ratio that `list_models` lists for the chosen model, such as 21:9. Fill the edges with a plain, continuous background, so a crop or an extension does not cut into the design.

The safe-zone column applies to the exported image after the crop. The profile image, the highlight covers and the YouTube banner are not cropped, so the column applies to them as made. For a cropped banner, use the band in the next section.

## How to crop a wide banner

A crop to a wider ratio keeps the full width and cuts the top and bottom. The width rules in the table stay the same. The height band changes. Put the logo and text in the height band below for the ratio you make. This band is the SAFE ZONE POSITION in the banner prompt.

| Target | From 21:9, keep | Logo and text in a 21:9 image | From 16:9, keep | Logo and text in a 16:9 image |
|---|---|---|---|---|
| X 3:1 | middle 78% of the height | middle 47% of the height | middle 59% of the height | middle 36% of the height |
| Facebook 2.7:1 | middle 86% of the height | middle 52% of the height | middle 66% of the height | middle 40% of the height |
| LinkedIn personal 4:1 | middle 58% of the height | middle 35% of the height | middle 44% of the height | middle 27% of the height |
| LinkedIn company 6:1 | middle 40% of the height | middle 16% of the height | middle 30% of the height | middle 12% of the height |

For the LinkedIn company cover, use 21:9 when the model lists it. From 16:9 the band is very thin.

## Prompt shapes

Replace each part in capitals with the brand's own words and hex codes. Keep the brand name, the tagline and every hex code in double quotes.

Profile image:

```
Square 1:1 profile image. Solid background "#PRIMARY".
The logo exactly as reference 1, no redraw, centred, about 55% of the width, so it survives a circular crop.
No text, no gradient, no border, no shadow.
```

Highlight cover, one per name, with the same style text each time:

```
Vertical 9:16 highlight cover. Solid background "#PRIMARY".
In the exact centre, a simple ICON FOR NAME in "#ACCENT", flat line style, about 40% of the width.
No text, no logo, nothing near the edges.
The icon matches the style of reference 1.
```

With no icon sheet, remove the reference line and describe the icon style in words. Keep that text the same for every cover.

Banner:

```
Wide RATIO banner. Background "#PRIMARY" with a subtle "#SECONDARY" shape on the right third.
The logo exactly as reference 1, no redraw, small, SAFE ZONE POSITION.
The tagline "EXACT WORDS" in a TYPE FEEL typeface, "#TEXT", spelled exactly, inside the same zone.
Plain, continuous background at every edge. Nothing else.
```

Write SAFE ZONE POSITION as the band for the ratio you make, with the width rule from the table. For example, a LinkedIn personal banner at 21:9: "in the right 65% of the width and the middle 35% of the height". For a banner with no tagline, remove the tagline line and write "No text".

## Checks for each image

- The logo is not redrawn, recoloured or cropped.
- The profile image still reads when cropped to a circle.
- Each highlight icon is readable at phone size inside a small circle.
- The tagline is spelled exactly. No other words appear.
- Nothing sits in the zones the platform covers or crops.
- All images use the same hex codes and the same style.
