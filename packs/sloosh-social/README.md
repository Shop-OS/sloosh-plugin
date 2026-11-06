# Sloosh social

![Sloosh](assets/sloosh.png)

Sloosh social helps you make posts for social feeds. It adds four skills to the core Sloosh plugin: swipe-through carousels, vertical clips for Reels, TikTok and Shorts, YouTube thumbnails and covers, and a preview skill that remixes a social post into a new video of your product. Each skill first writes a plan in the chat, such as the slides, the hooks or the headline. The plan costs nothing. Then the skill makes the content. It uses a published Sloosh Space when one fits, and makes the content directly when none does. Claude shows you the quoted credits for each round of work and asks for your approval before it spends.

The pack never posts to a social account and never reads your social accounts. For one ad in several sizes, use the core plugin's ad variants skill. For a product clip that is not for a vertical feed, use the core plugin's product video skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled. You set the daily allowance in Sloosh settings.
- The right to use every product photo, logo, review and style reference that you give Claude. Claude asks you to confirm this before it quotes any work that uses them.
- Consent from every person who appears. A person must agree to appear in AI-made content. Claude does not use a photo of a child or of a public figure.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-social@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh social. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-social folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-social@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| carousel-builder | A carousel of 4 to 10 slides in one look for Instagram or a LinkedIn document post, with a cover that works alone and copy for each slide. | Paid |
| reels-shorts-clip | One vertical clip of up to 15 seconds for Reels, TikTok or Shorts, built around a hook in the first 3 seconds. Captions and music come only from published Spaces that fit. | Paid |
| youtube-thumbnail | Truthful, high-contrast YouTube thumbnails and vertical Shorts or Reels covers with a 3 to 5 word headline, and variants that each test one change. | Paid |
| social-post-remix | Preview. A new video of your product or character in the structure and style of an Instagram or X post. It studies the post's hook, pacing and shots, makes new shots, and never reuses the post's footage or script. It needs the Calypso editor, which only some Sloosh connections have yet. | Paid |

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. A brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace.

The pack reads only what you give it: product photos, faces, logos, reviews, style references and the story or title you paste or upload. It does not read social accounts or analytics. It does not post, schedule or upload to a social account, even when a social connector is present. It does not mix audio, join or trim clips. For a LinkedIn document post, you join the slides into a PDF.

The social post remix skill is the one exception to "only what you give it": when you paste a public Instagram or X post link, Sloosh imports that post's video into your workspace as a reference. Sloosh's hosted Calypso editor studies it and assembles the new edit there. The result uses only new shots of your product or character. It never reuses the post's footage or script. TikTok and YouTube links are not supported.

## Spending

Every skill in this pack makes content, so each one uses the credits and the daily spending allowance of the workspace you connect. The plan in the chat costs nothing. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. A carousel makes the cover first, as a round of its own, so you approve the look before the other slides. A clip has a separate quote and approval for the clip, the captions and the music. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Make a 7-slide Instagram carousel on how to use our serum."
- "Turn these five packing tips into a LinkedIn carousel."
- "Make a 9-second Reel of our candle from this product photo."
- "Make this still postable as a TikTok with captions."
- "Make three YouTube thumbnails for my video on our trainer test."
- "Make a Shorts cover for this clip."
- "Remix this Instagram Reel into a new video for our candle."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
