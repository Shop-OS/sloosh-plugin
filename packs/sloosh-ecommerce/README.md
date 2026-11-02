# Sloosh ecommerce

![Sloosh](assets/sloosh.png)

Sloosh ecommerce makes the images that marketplaces and online stores need. It adds ten skills to the core Sloosh plugin. Four skills make marketplace images: listing sets, white-background main images, multi-angle views and colourways. Three skills make apparel images: ghost mannequin shots, virtual try-on and lookbook sets. Three skills make store and category images: food photos, products in a room and collection banners. They use a published Sloosh Space when one fits, and make the images directly when none does. Claude shows you the quoted credits for each round of work and asks for your approval before it spends.

The pack never uploads to a marketplace, a store or a delivery app. Marketplace rules change often. Claude tells you which rules it applies, and you check the marketplace's current image spec before you upload. For one packshot or one lifestyle shot, use the core plugin's product imagery skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled. You set the daily allowance in Sloosh settings.
- The right to use every product, room, pose and reference photo that you give Claude. Claude asks you to confirm this before it quotes any work that uses them.
- The agreement of each real person in a photo that you give Claude. Claude does not use a photo of a child or of a public figure.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-ecommerce@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh ecommerce. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-ecommerce folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-ecommerce@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| amazon-listing-pack | A square listing image set for one product: a white main image, then lifestyle, scale, detail, feature callout and what's-in-the-box images. | Paid |
| white-background-compliance | A marketplace main image with the product alone on pure white, or a check of a main image you have against common white-background rules. | Paid |
| product-multi-angle | A matching set of views from one photo, such as front, three-quarter, side, back and top-down. | Paid |
| colourway-variants | One product in other colours or finishes, with the shape, hardware and framing kept the same. | Paid |
| ghost-mannequin | Garment photos with no model, hanger or dummy in view, shaped as if worn, on white or light grey. | Paid |
| virtual-try-on | A garment, glasses or jewellery shown on the person in your photo, with the face, pose and background kept. | Paid |
| fashion-lookbook-set | An on-model set that reads as one shoot, with the same model and light in each frame, and optional short clips. | Paid |
| food-photo-studio | Commercial food photos from a phone photo of a real dish, in menu, delivery app, feed and story sizes. | Paid |
| product-in-room | A home product placed in a room photo at true scale, with the room's light, perspective and shadows. | Paid |
| collection-banner | A wide store banner with two to four products on one set, an empty zone for your headline and a mobile version. | Paid |

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. The skills use its colours, photo style and product names. A brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace.

The pack reads only what you give it: product photos, room photos, person and pose photos, product facts and dish ingredients that you paste or upload. It does not read your store, your marketplace account or your sales data. It does not upload to a marketplace, a store or a delivery app. The images have no added text, so a store's own headline or a marketplace's rules stay in your control. Claude uses a customer's own photo only for the request that customer made, and never reuses it for other work.

Claude uses only the facts you give and the label on the product. It does not invent a feature, a size, a claim or a review. Generated colours are a guide, not a colour-matched sample. A room scene is a visual guide, not a measured plan. A view that your photo does not show, such as the back of a product, is inferred, and Claude tells you so.

## Spending

Planning costs nothing. This includes the image set plan, the shot list, the marketplace rules and a check of a main image you already have. The skills that make images use the credits and the daily spending allowance of the workspace you connect. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Make a full Amazon listing image set for this water bottle."
- "Put this serum on a pure white background for our Flipkart main image."
- "Check if this main image meets Amazon's white-background rules."
- "Show this tote in black, navy and sand."
- "Turn these model photos of our shirt into ghost mannequin shots."
- "Make a lookbook of our summer dresses on one model in a grey studio."
- "Make this phone photo of our biryani look good for the delivery app."
- "Show this sofa in my living room photo."
- "Make a homepage banner with our three candles, with space on the left for the headline."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
