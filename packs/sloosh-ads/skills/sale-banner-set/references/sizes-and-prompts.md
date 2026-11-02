# Sizes and prompts

Read this file before you write the prompts on the direct path. It holds the size list, the email header rules, the alt text rule and the prompt shapes.

## Sizes

| Size | Ratio | Use | Layout |
|---|---|---|---|
| Square | 1:1 | Feed posts, chat and WhatsApp broadcasts, the master banner | Product and headline balanced, terms line below. |
| Portrait | 4:5 | Feed ads | Headline above the product, terms line below. |
| Story | 9:16 | Stories and reels | Keep the product and the text out of the top 14%, the bottom 35% and 6% at each side. |
| Landscape | 16:9 | Store homepage, web banners | Product to one side, text to the other, wide margins. |
| Email header | the widest ratio the model lists from 2:1 to 3:1, such as 21:9 or 3:1 | The top of a campaign email or newsletter | Headline and code in the centre, product beside them. |

Use only ratios that the model's `list_models` entry lists. If the model lists no ratio wider than 16:9, use 16:9 for the email header and tell the user.

## Email header

- Most email layouts show the header at about 600 px wide. On a phone it shows smaller still. Write one short headline in large, bold type that is easy to read at that width.
- Keep the headline, the code and the product inside the central 80% of the width. Some email templates crop or pad the edges.
- Keep the terms line short. If it does not read well at email width, ask the user to move it into the email text below the header.
- Keep the body copy out of the image. The email itself carries it as live text.
- Check that the type contrasts with the background and reads at about 600 px wide.
- Use a size of about 2K or the model's default. Ask the user before you choose a larger size, because it can cost more.

## Alt text

- Many email clients block images until the reader allows them. Give the user one alt text line for each email header.
- Put the full offer in the alt text: the headline, the code and the end date, with the same words as the locked offer.
- Keep it to one short sentence. Do not start it with "image of".
- Suggest that the user also puts the code and the end date in the email text, so a reader without images still sees them.

## Prompt shapes

### Round 1: the square master

Name the product from reference 1 and where it sits. Give the headline and the terms line in quotes, with the words "exactly" and "no other text". Give the colours and a clean, bold sans-serif type with wide margins. If there is a logo, place the logo from reference 2 small in a corner, inside the safe area. Keep the product label and colours exactly as reference 1.

Example: "Square sale banner. The candle from reference 1 sits on the right, on a warm cream background. Headline exactly: "25% OFF ALL CANDLES". Terms line exactly: "Code GLOW25. Ends Sunday." Bold sans-serif type in deep brown, wide margins, no other text. The logo from reference 2 small in the top left corner. Keep the label and colours exactly as reference 1."

### Round 2: the other sizes

Start each prompt with: "Reference 1 is the approved square banner. Recompose the same elements, colours and type for this ratio." Then give the headline and the terms line again in quotes, with "exactly" and "no other text". Add the layout line for the size from the table above.

For the email header, add: "Wide email header. Headline and code large and centred, inside the central 80% of the width. The product beside the text, also inside that area. Nothing important near the edges."

### If the text or product is wrong

- Use shorter words or all caps. Short words spell better.
- If the product is lost in the layout, put its position first in the prompt, such as "product occupies the right third".
