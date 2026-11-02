# White-background rules and checks

These notes are guidance, not a promise of compliance. Each marketplace changes its image rules, and some categories have extra rules. Before the user uploads, tell them to check the marketplace's current main image spec for their category.

Never tell the user that an image is compliant. Say which rules you applied and which ones they must still check.

## Common main image rules

| Rule | Common guidance |
|---|---|
| Background | Pure white (RGB 255, 255, 255) to every edge. No grey, cream, gradient or vignette. |
| Fill | The product fills about 85% of the frame. Small margins on each side. |
| Position | The product is centred and shown whole. No part is cut off at an edge. |
| Content | Only the product for sale. No added text, logos, badges, watermarks, borders, frames or colour blocks. No props or accessories that are not included. |
| Shadow | Some marketplaces accept a faint natural contact shadow. For strict rules, use no shadow. |
| Ratio | Square 1:1 is the safe default. |
| Size | Many sellers aim for at least 1600 px on the longest side so zoom works. Check the current minimum. |
| Product truth | The true colour, shape, label and parts. No retouching that changes what the buyer gets. |

## Marketplace notes

| Marketplace | Main image guidance |
|---|---|
| Amazon | Pure white, product fills about 85%, only the product for sale. Check the current product image requirements in Seller Central for the category. Some apparel categories do not allow a mannequin on the main image. |
| Flipkart | Usually a white or very light background with the product only. Check the current listing image guidelines in the seller dashboard. |
| Walmart | Usually a white background with the product only, in a large square image. Check the current item image guidelines in Seller Center. |
| eBay | A plain white or light background is recommended. Check the current photo policy. |
| Google Shopping | A plain white or light background is recommended. No promotional overlays. Check the current image requirements in Merchant Center. |
| Etsy | No white-background rule. Check the current photo guidance. |
| Other | Ask the user for the marketplace's image rules or a link to them. If they have none, apply the Amazon guidance as a safe default and say so. |

## Finishes

- Cut-out: the product on plain white with no shadow. It suits strict rules. It needs a background-remover Space that puts the product on white. Such a Space keeps the source pixels. Some Spaces output a transparent background or keep the photo's framing. Then the result is not on white, not square or not at about 85% fill.
- White studio: the product on white with a faint contact shadow. It looks more natural, but its white can be near-white.
- On the direct path every finish is generated, so it is a new image of the product, not a cut-out. Check the label and shape as for any image.

## Choose the finish

| Need | Finish | Why |
|---|---|---|
| A strict marketplace main image | Cut-out on plain white, no shadow | A background-remover Space keeps the source pixels, so the label and shape stay true. On the direct path, check the label and shape. |
| A natural product page look | White studio with a faint contact shadow | The product looks grounded. The white can be near-white, not pure white. |
| A cluttered phone photo | White studio first, then a cut-out if the white fails the check | The studio route removes the background clutter and keeps the product unchanged. |
| A product with fine parts (straps, cords, hair, mesh, glass) | White studio | A cut-out can lose fine or clear parts. |
| Many products for one catalogue grid | The same Space and the same finish for each product | One look across the grid. |

## Direct path prompt

Use this shape when no Space fits. Pass the product photo as a reference asset.

```
The product from the reference image, exactly as shown, centred on a pure white seamless background, filling about 85% of a square frame.
Even soft studio light. [No shadow. | A very faint contact shadow directly under the product.] No reflections, no props, no text, no logo, no watermark, no border.
Keep the label, colours, shape and proportions identical to the reference.
```

## Visual check

Look at each image with `view_asset`. The preview is small, so it cannot measure pixel values or the exact pixel size.

| Check | Pass |
|---|---|
| White | The background reads as white to every edge and corner. No grey cast, gradient, vignette or seam line. No transparent or checkerboard background. |
| Edges | Clean outline. No halo, fringe, jagged edge or leftover old background. |
| Fine parts | Straps, cords, handles, hair, mesh and clear parts are all present. |
| Fill and position | The product fills about 85% of the frame, is centred and is not cut off. |
| Product truth | The label text is exact and spelled the same. The colour and shape match the source photo. |
| Content | No added text, logo, badge, watermark, border or prop. |
| Shadow | No shadow for the strict finish. Only a faint contact shadow for the studio finish. |

Tell the user to confirm pure white with an eyedropper in an image editor, or with the marketplace's own image check, and to confirm the pixel size before they upload.

## Fix a failed check

| Failure | Fix |
|---|---|
| Grey or off-white background | Run a background-remover Space that outputs white on the result, or on the source photo. Do not re-roll the same prompt. If none fits, suggest a background tool in an image editor. |
| Halo or rough edge | Run the cut-out on a sharper source photo, or use the white studio finish. |
| Fine parts lost in the cut-out | Use the white studio finish. |
| Product too small or off-centre (direct path) | Generate again with "centred, filling about 85% of a square frame" in the prompt. |
| Cut-out not square, not about 85% fill or transparent | Use the white studio Space or the direct path. Or tell the user to place the cut-out on white and square it in an image editor. |
| Label changed or misspelled | Use a background-remover Space, which keeps the source pixels. Ask for a sharper source photo if needed. |
| Image too small for the marketplace minimum | Search for an upscale Space with `list_spaces`. |
| Added text, prop or badge | Add "no text, no props, no badges" to the prompt, or use a background-remover Space. |
