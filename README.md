# Sloosh plugins

![Sloosh](assets/sloosh.png)

Sloosh makes product images, ad variants and short product videos, and runs the published Sloosh Spaces in your workspace. This plugin connects Claude to your Sloosh workspace and adds eleven skills: product imagery, ad variants, published Spaces, product video, UGC storyboards, video remixes, launch films, creative iteration, batch runs, asset management and a skill router. Creative iteration takes the next round on a Sloosh result you have seen. Batch runs run one published Space over a list of items. The router picks the skill for a request that names none.

This marketplace also has nine packs. Each pack is a separate plugin that needs this core plugin:

- [Sloosh for Shopify stores](#sloosh-for-shopify-stores) (`sloosh-shopify`) makes catalog images, launch ads with copy and short product page videos for the products in a Shopify store.
- [Sloosh motion films](#sloosh-motion-films) (`sloosh-motion`) makes stylised short films on your computer, such as product reveals, beat-synced edits and software walkthroughs, with a style guide from a reference video and a catalog of named motion effects.
- [Sloosh performance ads](#sloosh-performance-ads) (`sloosh-ads`) plans, writes, makes and tests performance ads, such as hook grids, comparison ads, seasonal creatives and creative test plans.
- [Sloosh video](#more-packs) (`sloosh-video`) makes product films, product animations, morphs, motion copies, talking-head clips, captions, soundtracks and voiceovers, upscales and edits or extensions of your clips.
- [Sloosh image editing](#more-packs) (`sloosh-image`) retouches, swaps and relights backgrounds, reframes and outpaints, transfers a reference style and upscales your images.
- [Sloosh ecommerce](#more-packs) (`sloosh-ecommerce`) makes marketplace and storefront images, such as listing sets, white-background images, colourways, try-on and lookbooks.
- [Sloosh brand](#more-packs) (`sloosh-brand`) builds a brand kit, logos, icon sets, brand boards, moodboards, mockups and social profile kits, and checks work against the brand.
- [Sloosh social](#more-packs) (`sloosh-social`) makes carousels, Reels and Shorts clips, and YouTube thumbnails.
- [Sloosh strategy](#more-packs) (`sloosh-strategy`) plans creative work: a creative strategy, competitor teardowns, launch campaign plans and a campaign run in rounds.

Sloosh uses the credits and the daily spending allowance of the workspace you connect. Claude shows you the quoted credits and asks for your approval. Sloosh blocks paid calls above your "Ask before spending more than" amount until you approve. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Install in Claude Code

Run this in Claude Code:

```
/plugin install sloosh --marketplace Shop-OS/sloosh-plugin
```

On an older Claude Code, add the marketplace first:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. Download the Sloosh plugin ZIP from the Sloosh MCP page.
2. In Claude, open Customize, then Plugins, then select Add and Upload plugin. Choose the ZIP.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Use the connector without the plugin

You can also add Sloosh as a custom connector. In Claude, open Customize, then Connectors, and add a custom connector with this URL: https://mcp.sloosh.ai/mcp. Sign in to Sloosh and authorize your workspace. You get the Sloosh tools without the skills.

## Use the skills in other agents

Each skill is a folder with a SKILL.md file in the open Agent Skills format. Other coding agents can install some or all of the skills. The skills call the Sloosh tools. First connect the Sloosh server in that agent, then install the skills. In Claude Code, use the plugin. Do not also copy the skills into `~/.claude/skills`.

### Connect the Sloosh server

Add the Sloosh server with this URL: https://mcp.sloosh.ai/mcp. Then sign in to Sloosh and authorize your workspace.

- Codex: run `codex mcp add sloosh --url https://mcp.sloosh.ai/mcp`. Codex opens the Sloosh sign-in. If it does not, run `codex mcp login sloosh`.
- Cursor: add `{"mcpServers":{"sloosh":{"url":"https://mcp.sloosh.ai/mcp"}}}` to `~/.cursor/mcp.json`.
- Gemini CLI: run `gemini mcp add --transport http -s user sloosh https://mcp.sloosh.ai/mcp`. Start Gemini CLI in a folder that you trust, then run `/mcp auth sloosh`.
- Muse Code: add `"sloosh":{"transport":"streamable_http","url":"https://mcp.sloosh.ai/mcp","enabled":true,"mode":"optional"}` to the `mcp_servers` block in `~/.config/muse/settings.json`. A new file must also set `"schema_version": 1`. Then run `muse mcp login sloosh`.

### Install skills with the skills CLI

List the skills in this repository:

```
npx skills@1.7.2 add Shop-OS/sloosh-plugin --list
```

Install the skills you want for the agents you name. With `-g`, the CLI puts one copy in `~/.agents/skills`, which Codex, Cursor and Gemini CLI all read:

```
npx skills@1.7.2 add Shop-OS/sloosh-plugin --skill product-imagery product-video -a codex cursor gemini-cli -g -y
```

Always name the agents with `-a`. Without it, the CLI installs the skills into every agent it supports, Claude Code included. The skills CLI is a third-party tool. It sends this repository's name and the skill names to skills.sh. Set `DISABLE_TELEMETRY=1` to stop this.

Some skills hand work to other skills. Install them together:

- `product-video`, `ad-variants`, `ugc-storyboard`, `remix-video` and `launch-film` use `product-imagery`.
- `ugc-storyboard` and `launch-film` use `product-video`.
- `ad-variants` and `ugc-storyboard` can use `published-spaces`.
- `product-imagery`, `product-video`, `ad-variants` and `published-spaces` hand changes to a result you have seen to `creative-iteration`.
- `launch-film` needs its whole folder, with its scripts, assets and references folders. See the Launch films section below for what it needs on your computer.

### Install the plugin in Codex

Codex can install the whole plugin from this repository, with the eleven skills and the Sloosh server:

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex mcp login sloosh
```

## Video remixes

The remix skill runs the Shadow Clone Space on a short clip you give it. Your character takes the place of the person in the clip, with the same motion, camera and timing. The clip must be 4 to 30 seconds long and at most 64 MiB, as an .mp4 or .mov file. Upload the file or share a direct link to it. Links to Instagram, TikTok, X or YouTube post pages do not work yet: save the clip with the platform's own option first.

## Launch films

The launch film skill directs and renders a SaaS or product launch film with Remotion on your computer, cut to your voiceover. It runs in a coding agent that can run commands on your computer, such as Claude Code. It needs Node.js, ffmpeg, and Python 3 with numpy and Pillow. It transcribes the voiceover with whisper-cpp and a speech model. The agent asks you before it installs either. It can use Sloosh images and clips for missing shots after you approve each quote. Remotion is free for individuals, non-profits and for-profit companies with up to three employees. Larger for-profit companies need a Remotion company license.

## Sloosh for Shopify stores

Sloosh for Shopify stores turns the products in a Shopify store into catalog images, launch ads with copy and short product page videos, from a brand kit that it saves once. It reads products and basic shop information only and never changes the store. It needs this core plugin. Install it after the core plugin:

```
/plugin install sloosh-shopify@sloosh
```

In Codex, run `codex plugin add sloosh-shopify@sloosh`. See [packs/sloosh-shopify/README.md](packs/sloosh-shopify/README.md) for its skills and how it gets products.

## Sloosh motion films

Sloosh motion films makes stylised short films on your computer: product reveals, beat-synced edits, software walkthroughs and feature announcements, kinetic typography, glitch, dot-matrix and morph films. When a shot is missing, Claude can make stills and clips with Sloosh after you approve each round's quote. The films render locally, so the pack runs in a coding agent that can run commands on your computer, such as Claude Code. It needs Python 3.9 or later with numpy, OpenCV and SciPy, ffmpeg, and Playwright with its Chromium browser. The agent asks you before it installs anything. It needs this core plugin. Install it after the core plugin:

```
/plugin install sloosh-motion@sloosh
```

In Codex, run `codex plugin add sloosh-motion@sloosh`. See [packs/sloosh-motion/README.md](packs/sloosh-motion/README.md) for its skills and how a film is made.

## Sloosh performance ads

Sloosh performance ads plans, writes, makes and tests performance ads. Its planning skills write ad concepts, ad copy, creative test plans and results retros, and cost nothing. Its making skills make hook grids, sale banners, before and after ads, comparison ads, reference ad remixes, testimonial ads and creator-style video ads, after you approve each round's quote. It never posts ads and never reads your ad accounts. It needs this core plugin. Install it after the core plugin:

```
/plugin install sloosh-ads@sloosh
```

In Codex, run `codex plugin add sloosh-ads@sloosh`. See [packs/sloosh-ads/README.md](packs/sloosh-ads/README.md) for its skills.

## More packs

These packs each need this core plugin. Install the ones you want after the core plugin, for example:

```
/plugin install sloosh-video@sloosh
```

In Codex, run `codex plugin add <pack>@sloosh`. Each pack's README lists its skills:

- `sloosh-video`: [packs/sloosh-video/README.md](packs/sloosh-video/README.md)
- `sloosh-image`: [packs/sloosh-image/README.md](packs/sloosh-image/README.md)
- `sloosh-ecommerce`: [packs/sloosh-ecommerce/README.md](packs/sloosh-ecommerce/README.md)
- `sloosh-brand`: [packs/sloosh-brand/README.md](packs/sloosh-brand/README.md)
- `sloosh-social`: [packs/sloosh-social/README.md](packs/sloosh-social/README.md)
- `sloosh-strategy`: [packs/sloosh-strategy/README.md](packs/sloosh-strategy/README.md). Its skills plan work and cost nothing.

## What the plugin sends

The plugin runs no code on its own. The launch film skill includes scripts and a Remotion project template that run on your computer only when you ask for a film. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace. Each pack's README says what that pack sends and reads.

## Example prompts

- "Make a studio photo of my water bottle on a clean white background."
- "Create three 9:16 ad variants for my summer sale on this sneaker."
- "Find a Space in my workspace that makes product ad grids and tell me what a run costs."
- "Turn my latest product image into a short video clip."
- "Write a UGC storyboard for my face serum and make the shots."
- "Remix this 15-second dance clip with my brand character."
- "Make a 30-second launch film for our app from PART 1.mp3 and our website."
- "The label on that last image is wrong. Fix it and keep the rest."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
