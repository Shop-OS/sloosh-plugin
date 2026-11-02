# Motion recipes

Each recipe sets values in the CONFIG block of `assets/chart.html`. Every value on screen comes from CONFIG.data, typed once at the top. Nothing in the drawing code holds a number.

## The four states

Every loop has the same four states. Plan them in one line each before you edit CONFIG.

1. Start: the empty or "before" state. Title, labels and the base line are already in place.
2. Change: about 2 s. Bars grow, a count runs, or points gather. Nothing fades out and gets replaced.
3. Hold: about 4 s. The final values show, and the headline value is labelled in the accent colour.
4. Return: about 1.5 s back to the start state, then a short rest on it. The last frame equals the first.

CONFIG.timing sets the start delay, change, hold and return in seconds. Keep their sum below CONFIG.duration so the loop rests on the start state. The title, category labels and axis never move.

## Choose the motion

| The user wants | motion | data |
|---|---|---|
| Compare 2 to 8 values, such as quarters or channels | bars | one entry per bar, with a label, text and value |
| Show a trend over time | bars-to-line | 3 to 8 entries in time order |
| One big number | count-up | one entry: text is the number, label is what it counts |
| A before and after, such as a conversion rate | before-after | two entries, the "before" first |
| A milestone, such as a follower count | milestone | one entry; set duration to 12 |

More than 8 values, a pie chart, a map or a dual axis is out of scope for this template. Offer the closest motion, or ask the user to cut the data down to what the post must say.

## Numbers

- text is the exact string the user gave, such as "44,000", "44k", "1.2M" or "4.8%". It is drawn as typed.
- value is only for bar height and line position. Leave it out when text is a plain number. For "44k" or "1.2M", set value to the number itself (44, or 1.2).
- A count runs from 0 (or from the "before" value) to the final number in the same format: same prefix, suffix, decimals and separators. The hold always shows the exact text.
- If a text has no number in it, it does not count. It shows as typed.
- Never round, reformat, add "+" or add a number the user did not give. A wrong digit is a failed chart.
- Real numbers: set sample to false. Sample data, only after the user agrees: set sample to true. "Illustrative data" then shows on every frame. Set source when the user names one.

## Sizes and safe zones

| Placement | width x height |
|---|---|
| LinkedIn and Instagram feed (default) | 1080 x 1350 |
| Square post | 1080 x 1080 |
| Reels, Stories, TikTok, Shorts | 1080 x 1920 |
| Slides, YouTube, a website | 1920 x 1080 |

At 9:16 the template keeps text and bars out of the top 14%, the bottom 35% and 6% at each side. Other sizes keep a 7% margin.

## Look

- One accent colour for the headline value. Other bars use the muted bar colour. Take the accent and the background from the brand kit when there is one, and check the contrast of text on the background.
- No gradients, glow, shadows, 3D or bounce. Motion eases in and out. Bars may grow one after another; they return together.
- No axis tick numbers and no grid. The value labels carry the numbers.
- Font: the system sans by default. For a brand font, embed it in the page with @font-face and a base64 data URL, and only when the user has the font file and may use it. Put its family name first in CONFIG.font.

## Milestone

- About 3,200 seeded points drift like a night sky. About 84% of them gather onto the number, sampled from an offscreen bold render of the text. Raise points to about 5,000 for a 1920-wide frame.
- Timing on a 12 s loop: 0 to 2 s drift, 2 to 6.5 s gather with a staggered ease, 6.5 to 7.5 s the accent line draws, 7.5 to 8.5 s the label fades in and rises, 8.5 to 10.5 s hold with a soft shimmer, 10.5 to 12 s the points return.
- Every random value comes from the seeded generator, so each seek gives the same pixels. Change milestone.seed for a different scatter.
- The number must come from a real source the user names, or the chart is marked "Illustrative data". Never round it up.

## Optional Sloosh still or plate

These are image prompts for the optional Sloosh round in SKILL.md.

Infographic still (one static image of the chart):

    A clean flat infographic, 4:5. Title "Orders per quarter". Four vertical bars labelled Q1, Q2, Q3, Q4 with the values "12k", "18k", "31k", "44k" printed above them, exactly as written. The Q4 bar in green, the others in dark grey, on a near-black background. Flat colours, no gradients, no 3D, no extra numbers, no other text.

Quote every number exactly as the user wrote it, in quotes. Ask for no other text. Read every digit back with `view_asset` before you show it.

Background plate (an image behind the coded chart):

    A soft, out-of-focus photo of a desk with a laptop in warm morning light, 4:5. The centre 70% of the frame is calm and dark enough for white text. No text, no numbers, no logos, no screens with content.

Save the plate as plate.png in the work folder and set CONFIG.plate to "plate.png". Darken it in an image editor if the chart text is hard to read. The plate never carries a number.
