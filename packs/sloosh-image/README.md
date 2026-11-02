# Sloosh image editing

![Sloosh](assets/sloosh.png)

Sloosh image editing helps you edit and finish images you already have. It adds five skills to the core Sloosh plugin. They retouch one thing in a photo, swap and relight a background, reframe a picture to a new shape, shoot your product in the look of a style reference and upscale a finished image for print or hero use. They use a published Sloosh Space when one fits, and make the edit directly when none does. Claude shows you the quoted credits for each round of work and asks for your approval before it spends.

Each skill keeps what you did not ask to change. The pack never posts images and never changes a store or an ad account. For a brand-new product photo, use the core plugin's product imagery skill. For more rounds on an image Sloosh just made, use the core plugin's creative iteration skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled. You set the daily allowance in Sloosh settings.
- The right to use and edit every image that you give Claude, including scene photos, logos and style references. Claude asks you to confirm this before it quotes any work that uses them.
- The consent of each person shown in a photo to an AI edit of that photo. Claude asks you to confirm this before it quotes. The skills do not edit photos of children or public figures.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-image@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh image editing. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-image folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-image@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| image-edit-retouch | One change to a photo you have, such as a removed object, a cut-out, fixed label text, a new colour or a skin retouch. The rest stays the same. | Paid |
| background-swap-relight | Your product or portrait placed in a new scene photo or a new background, relit so it looks shot there. | Paid |
| reframe-outpaint | The same picture in a new aspect ratio or a larger frame, such as a landscape photo outpainted to a 9:16 story. | Paid |
| style-reference-transfer | Your product shot in the look of one to four style references, such as a mood board or an editorial still. | Paid |
| upscale-and-finish | A finished image upscaled from 2x to 6x for print or a hero banner, delivered at a stated pixel size and file format. | Paid |

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. A brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images it makes in your workspace.

The pack reads only what you give it: the photos, scene photos, light references, style references and logos that you paste, upload or link. It does not read your store, ad accounts or analytics. It does not post or upload images anywhere outside your Sloosh workspace. It imports an image into Sloosh only when you own it or have the right to use it. It does not copy another brand's logo, mascot or campaign from a style reference.

## Spending

Every skill in this pack uses the credits and the daily spending allowance of the workspace you connect. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. Each fix after a result needs a new quote and a new approval. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Remove the price tag from this product photo and keep everything else the same."
- "Cut out our serum bottle on a transparent background."
- "Put this candle into my bathroom photo and match the light."
- "Make this landscape photo a 9:16 story and extend the table."
- "Shoot our sneaker in the style of these three mood images."
- "Upscale this hero image to 4x for an A3 print."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
