# Sloosh brand

![Sloosh](assets/sloosh.png)

Sloosh brand helps you build a brand and keep it consistent. It adds nine skills to the core Sloosh plugin. Two skills work with the brand kit: one builds the kit from your website, brand guide or logo, and one checks finished images against it. These two cost nothing. Seven skills make brand work: logo concepts, brand boards, moodboards, icon sets, social profile kits, merch and packaging mockups and logo animations. They use a published Sloosh Space when one fits, and make the image or clip directly when none does. Claude shows you the quoted credits for each round of work and asks for your approval before it spends.

Sloosh makes PNG images and video clips, not vector files. A designer can trace an approved logo or icon to SVG. The pack never posts to social platforms and never changes your website or store. For on-brand product photos, use the core plugin's product imagery skill. For posts and ads, use the core plugin's ad variants skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled, for the skills that make images and clips. You set the daily allowance in Sloosh settings.
- The right to use every logo, artwork, photo, brand guide and style reference that you give Claude. Claude asks you to confirm this before it imports or quotes any work that uses them.
- The consent of any real person whose face appears in a logo, mascot photo or reference. Claude asks you to confirm this too.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-brand@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh brand. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-brand folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-brand@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| brand-kit-extract | A brand kit file, sloosh-brand.md, from your website, brand guide or logo: colours, fonts, voice, photo style and rules. | Free |
| brand-consistency-check | A keep, fix or drop scorecard for each finished image against the brand kit, with the skill that makes each fix. | Free |
| logo-from-brief | Original logo concepts from a brand name and a short brief, then mono, lockup and icon-only versions of the pick. | Paid |
| brand-board | Three to six brand board pages, such as palette, type, mood and logo lockup pages, or a one-page style tile. | Paid |
| moodboard-exploration | A moodboard of small draft images across three or four directions, and a short note on the direction you pick. | Paid |
| brand-icon-set | Matching icons in your logo's colours and stroke style, as grid sheets of up to nine icons. | Paid |
| social-profile-kit | A profile picture, highlight covers and a banner for each platform, with the export size of each image. | Paid |
| merch-packaging-mockups | Your logo or artwork on photoreal merch, packaging, stationery and poster mockups. | Paid |
| logo-animation | A short reveal clip of your existing logo, such as an intro sting or a brand bumper. | Paid |

## Where the brand kit lives

The brand-kit-extract skill writes the brand kit as a sloosh-brand.md file. It uses the same format as the brand kit from the Shopify pack. For a Shopify store, use the brand kit skill in the Shopify pack. Claude shows you the draft kit and saves it only after you approve it.

- In Claude Code, the skill writes sloosh-brand.md at the project root.
- In the Claude app, the skill gives you the file. Add it to the Project's knowledge, or paste it into later chats.

If you have a brand kit, such as a sloosh-brand.md file, Project knowledge or pasted text, every skill reads it first. The brand-consistency-check skill needs a brand kit. For the other skills, a brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace.

The pack reads only what you give it: logos, artwork, brand guides, brand text, product photos, finished images and the website pages you name. It does not post or upload to social platforms, and it does not change your website or store. It imports a logo, artwork or reference image into Sloosh only after you confirm you own it or have the right to use it. The brand-consistency-check skill adds an image to your Sloosh library only to look at it.

## Spending

The brand-kit-extract and brand-consistency-check skills cost nothing. The skills that make images and clips use the credits and the daily spending allowance of the workspace you connect. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. A changed brief or each new refine round needs a new quote and a new approval. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Pull our brand from tealeaf.com into a brand kit."
- "Give me three logo directions for Larkspur, a small-batch candle brand."
- "Make a brand board with our palette, type and mood for the agency."
- "Show me a moodboard of a few directions for our new skincare line."
- "Make a profile picture, highlight covers and banners for Instagram, LinkedIn and YouTube."
- "Are these twelve spring images on brand before we post them?"

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
