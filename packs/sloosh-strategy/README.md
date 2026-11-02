# Sloosh strategy

![Sloosh](assets/sloosh.png)

Sloosh strategy helps you plan creative work before you spend. It adds four skills to the core Sloosh plugin. Three skills plan: a creative strategy from a brief, a teardown of competitor ads and a dated launch campaign plan. The fourth skill runs a campaign across rounds and sends each round to the skill that makes it. All four skills cost nothing. When a campaign runs, the producing skills show you the quoted credits for each round and ask for your approval before they spend.

The pack never posts ads, never reads your ad accounts and never changes a campaign. For one image, one ad or one video, use the skill that makes it, such as the core plugin's product imagery skill.

## What you need

- The core Sloosh plugin, installed and connected to your Sloosh workspace. This pack uses the Sloosh tools from the core plugin.
- A Sloosh workspace with spending enabled, for the rounds that make images and videos. You set the daily allowance in Sloosh settings.
- The right to use every image, review and reference that you give Claude. Claude asks you to confirm this before it quotes any work that uses them.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-strategy@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in the Claude app

1. In Claude, open Customize, then Plugins. Add the marketplace Shop-OS/sloosh-plugin and install Sloosh strategy. You can also select Add and Upload plugin, and choose a ZIP of the packs/sloosh-strategy folder.
2. Install the core Sloosh plugin too, if it is not installed yet.
3. Open the plugin's Connectors tab. Select Add if Sloosh is not added yet, then select Connect.
4. Sign in to Sloosh and authorize the workspace you want to use.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-strategy@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| creative-strategy | A confirmed brief and three to five creative territories, each with its visual world, hook family, proof, deliverables and main risk. | Free |
| competitor-creative-teardown | A teardown of the competitor ads you share: an inventory, a pattern table, the gaps and concept seeds that borrow structure, never assets. | Free |
| launch-campaign-plan | A dated plan for a launch, drop, sale or season: the assets each phase needs, the skill that makes each one, the approval rounds and a calendar. | Free |
| campaign-orchestrator | A campaign run in rounds, with one approval for each round. Each round goes to the skill that makes it, and only checked outputs feed the next round. | Free |

The campaign orchestrator itself costs nothing. The producing skills that it sends work to quote their own work and spend only after you approve.

## Where the brand kit lives

If you have a brand kit, such as a sloosh-brand.md file from the Shopify pack, Project knowledge or pasted text, every skill reads it first. A brand kit is optional.

## What the pack sends and reads

The pack runs no code on its own. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, images and choices you give it, using the access you grant when you connect. Sloosh stores the images and videos it makes in your workspace.

The pack reads only what you give it: briefs, product images, reviews, offers, dates and the competitor ads or public pages that you paste, upload or link. It does not search for, log in to or scrape ad accounts. It does not read analytics. It does not post or upload to ad accounts, even when an ads connector is present. It never sends a competitor ad to Sloosh. Competitor ads stay in the chat, and the teardown never copies a competitor's logo, copy, people or product shots.

## Spending

The planning skills cost nothing. When the campaign orchestrator runs a round, the producing skills use the credits and the daily spending allowance of the workspace you connect. Claude gets a quote before it makes anything. Claude groups the work into rounds of up to eight items. For each round, Claude shows the quoted credits and the round total, and asks for one approval. A Space run also shows the most it can hold. If the round total is more than the allowance left today, Claude proposes cuts or gives you the Sloosh settings link, and does not run the round. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Give me three creative directions for our autumn skincare launch."
- "Here are five ads from our two biggest rivals. What do they repeat and what can we learn?"
- "Plan the creative for our sneaker drop on 15 November across the store, Instagram and email."
- "Run the launch kit for the new sneaker: hero stills, feed and story ads, and a clip from the hero."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
