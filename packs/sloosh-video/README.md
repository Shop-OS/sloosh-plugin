# Sloosh video

![Sloosh](assets/sloosh.png)

Sloosh video helps you make and change product videos in the chat. It adds nine skills to the core Sloosh plugin. Three skills make new video: multi-shot product films, product effect clips and transitions from one frame to another. Six skills work from a clip or a person you already have: motion copies, talking-head clips, captions and subtitles, clip extends, edits and restyles, soundtracks and voiceovers, and upscales. They use a published Sloosh Space when one fits, and make the clip directly when none does. Captions, soundtracks and upscales use a published Space only. Claude shows you the quoted credits for each round of work and asks for your approval before it spends.

Everything runs in Sloosh, so nothing renders on your computer. The pack never posts videos and never joins clips. It adds audio to a clip only through a published Space. You cut the clips together in your own editor. For one plain clip from a prompt or a product image, use the core plugin's product video skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled. You set the daily allowance in Sloosh settings.
- The right to use every photo, clip and reference video that you give Claude. Claude asks you to confirm this before it quotes any work that uses them.
- The consent of every real person who appears in your photos or clips. Claude asks you to confirm it before any quote. The pack does not use a child or a public figure.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-video@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh video. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-video folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-video@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| cinematic-product-film | A product film of 4 to 8 shots: a storyboard, one keyframe per shot, then one clip per shot with one look, delivered in shot order. | Paid |
| product-animation | One product effect clip from one product photo, such as an exploded view, a 360 spin, a float, a splash or a seamless loop. | Paid |
| transitions-and-morphs | One clip that moves from a start frame to an end frame, such as a colourway change, a before and after or a match-cut bridge. | Paid |
| motion-replicate | The moves, timing and camera of a reference clip, given to your own character, creator, mascot or product. | Paid |
| talking-head-video | A person on camera who says your script: a lip-synced clip, a dub into another language, new camera angles or a talking clip from one photo. | Paid |
| captions-subtitles | Word-timed captions or styled subtitles burned into a clip with speech, so it reads on mute. | Paid |
| video-extend-edit | Your existing clip, made longer, fixed in one place or restyled into a new setting or look. | Paid |
| soundtrack-and-voice | A music bed, an original soundtrack or a voiceover added to a clip you already have, through a published Space. | Paid |
| video-upscale-master | A sharper, larger version of an existing clip, such as 1080p, 2K or 4K, from a published upscale Space, with the same length, framing and timing. | Paid |

The storyboard of a product film costs nothing. Claude asks you to approve it before it quotes the keyframes. Captions and subtitles need a published captions Space in your workspace. When none exists, Claude tells you and makes nothing. Soundtracks, voiceovers and upscales work the same way.

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. A brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images, clips and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace.

The pack reads only what you give it: product photos, clips, scripts, frames and reference videos that you paste or upload. It does not post or upload to any social or ad account. It imports a reference clip into Sloosh only when you own it or have the right to use it. It drops the logo, on-screen text, watermark and voice of a reference clip. It never removes a watermark or a rights mark from your clip.

Claude cannot watch a video. It checks stills and asks you to watch each clip and check it against a short list.

## Spending

Every skill in this pack uses the credits and the daily spending allowance of the workspace you connect. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. A re-shoot or a fix is new work with a new quote and a new approval. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Make a 30 second cinematic film for our new perfume from these product photos."
- "Make an exploded view of our earbuds from this packshot."
- "Morph our bottle from black to sand in one clip."
- "Make our mascot do the dance in this clip. I own the clip."
- "Make our founder say this script from her headshot. She agreed to it."
- "Add karaoke-style captions to this talking clip for Reels."
- "Make this clip three seconds longer and change the background to a beach."
- "Add a calm music bed and a voiceover with this script to our product clip."
- "Upscale this clip to 4K."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
