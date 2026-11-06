# Sloosh performance ads

![Sloosh](assets/sloosh.png)

Sloosh performance ads helps you plan, write, make and test performance ads. It adds thirteen skills to the core Sloosh plugin. Five skills plan and write: ad concepts, ad copy, short video scripts, creative test plans and results retros. These five cost nothing. Eight skills make ads: hook grids, sale banners, seasonal creatives, before and after ads, comparison ads, reference ad remixes, testimonial ads and creator-style video ads. They use a published Sloosh Space when one fits, and make the ad directly when none does. Claude shows you the quoted credits for each round of work and asks for your approval before it spends.

The pack never posts ads, never reads your ad accounts and never changes a campaign. For simple resized or restyled variants of one ad, use the core plugin's ad variants skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled, for the skills that make ads. You set the daily allowance in Sloosh settings.
- The right to use every image, review and reference ad that you give Claude. Claude asks you to confirm this before it quotes any work that uses them.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-ads@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh performance ads. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-ads folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-ads@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| ad-concepts | Ad concepts for a product: the angle, the format and the skill that makes each one. | Free |
| ad-copy-variations | Ad copy at volume: hooks, headlines, primary text and calls to action within each platform's limits. | Free |
| script-writer | A 15, 30 or 60 second video script: a hook for the first 2 seconds, timed beats with on-screen text and voiceover lines, a call to action and three alternative hooks, ready for the storyboard skill. | Free |
| creative-testing-plan | A test plan: one variable per test, the names, the ad sets, the metrics and what each result decides. | Free |
| creative-performance-retro | A retro of the results you paste: what won, how sure the data is and what to test next. | Free |
| ad-hook-matrix | A grid of hook images that change one thing at a time, ready for a test. | Paid |
| sale-banner-set | A set of sale or offer banners in the sizes your channels use, with your exact offer text and an email header when you need one. | Paid |
| seasonal-creatives | Festival, holiday and season versions of your product's ads, with the product and its label kept exact, plus a greeting image or a short clip on request. | Paid |
| before-after-ad | A before and after ad that shows the real problem and what the product does. | Paid |
| comparison-ad | A comparison ad with a table of true, sourced points. | Paid |
| reference-ad-remix | Your product in the layout of a reference ad that you own or have the right to use. | Paid |
| testimonial-ads | Review card ads that quote real reviews word for word. | Paid |
| ugc-video-ad | A creator-style video ad from a published Sloosh Space, such as a selfie ad with a voiceover. | Paid |

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. A brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace.

The pack reads only what you give it: product images, reviews, offers, reference ads and results that you paste or upload. It does not read ad accounts or analytics. It does not post or upload to ad accounts, even when an ads connector is present. It imports a reference ad into Sloosh only when you own it or have the right to use it.

## Spending

The planning skills cost nothing. The skills that make ads use the credits and the daily spending allowance of the workspace you connect. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude gives you the Sloosh settings link and does not run the round. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Give me ten ad concepts for our new protein bar."
- "Write twenty hooks and headlines for our serum for Meta and TikTok."
- "Write a 30 second TikTok script for our lunch bags, for parents, to drive sales."
- "Make a hook grid for our trainer launch so we can test the first line."
- "Make a sale banner set for 20% off everything this weekend."
- "Make Diwali feed and story images for our scented candle."
- "Plan a creative test for these three ad angles."
- "Here are last week's results. What won and what should we test next?"

## Open-source credits

The script writer adapts two MIT-licensed projects. It ships no code from them.

- Its virality checklist adapts the ranked virality criteria in [AI-Youtube-Shorts-Generator](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator) (MIT License).
- Its post-style rules adapt the post structure and content rules in the generate-post prompts of [social-media-agent](https://github.com/langchain-ai/social-media-agent) by LangChain (MIT License).

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
