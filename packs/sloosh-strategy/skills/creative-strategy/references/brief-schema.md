# The creative brief

The creative-strategy skill writes this brief in Part 1. Keep it in the conversation as a short block the user can correct. When you hand off, paste the brief and the chosen card into the producing skill's request. Never invent a field the user did not give or confirm. Mark it unknown.

## The brief block

```yaml
brief:
  brand: name as the user writes it
  product: one product per brief; several products need several briefs
  product_assets:                     # Sloosh assets, by kind and id
    - {kind: workspace, id: <id>, role: product, note: front packshot, rights: confirmed, person_consent: confirmed | no person}
  brand_kit: sloosh-brand.md | pasted text | unknown
  audience: who buys it, in plain words
  objective: conversions | awareness | retention | catalogue
  offer: "Buy 2 get 1" | none
  message: the one thing the viewer should take away
  proof: review quote, stat, ingredient or award, verbatim, with its source
  tone: three words at most
  placements: [ig-feed-4x5, ig-story-9x16, meta-feed-1x1]
  deliverables:                        # what the user gets
    - {type: image, count: 3, ratio: "4:5"}
    - {type: video, count: 1, ratio: "9:16", seconds: 10, audio: true}
  references: [{kind: workspace, id: <id>, role: style | competitor | mood, rights: confirmed}]
  must_keep: [label text, cap colour, bottle shape]
  must_avoid: [neon, clutter, medical claims]
  copy_on_image: none | "exact text"
  language: en
  budget_comfort: unknown | the budget the user states
  allowance_left: unknown | budget.remainingUnits from get_connection / 1000, in credits
  deadline: unknown
```

Write the prompt fields tight, so you can paste them into a prompt as they are:

```yaml
message: "Scalp-first care that shows in four weeks"
tone: calm, clinical, warm
must_keep: [label text, matte green cap, bottle proportions]
must_avoid: [neon, clutter, before and after skin claims, text over the label]
```

## Defaults

Apply these only when the user says "just make it" or does not answer. State each one you apply.

- Placements: feed 4:5 and story 9:16.
- Count: three variations of each.
- Copy on image: none.
- Quality: draft first. The producing skill finishes the approved direction at full quality.

## Placement to ratio

| Placement | Ratio | Notes |
|---|---|---|
| Instagram or Facebook feed | 4:5 | 1:1 is the fallback. |
| Stories, Reels, TikTok, Shorts | 9:16 | Keep the product and the text out of the top 14%, the bottom 35% and 6% at each side. |
| Facebook, LinkedIn or X feed | 1:1 | The universal fallback. |
| YouTube, landscape display, website hero | 16:9 | |
| Pinterest pin | 2:3 | Vertical, little text, lifestyle. |
| Email or messaging header | 3:1 | Short copy. Product on the left or in the centre. |
| Marketplace main image | 1:1 | Pure white background, product fills most of the frame, no text, no props. |
| Store product gallery | 1:1 or 4:5 | Use the same crop across products. |

The producing skill picks the resolution and checks the model limits.

## Video length by placement

| Placement | Sweet spot | Sound |
|---|---|---|
| TikTok, Reels or Shorts ad | 9 to 15 s | Design for sound on. Add captions for sound off. |
| Meta feed video | 6 to 15 s | Most people watch muted. Add captions. |
| YouTube bumper | 6 s | |
| YouTube pre-roll | 15 to 20 s | Show the brand in the first 5 s. |
| Product page loop | 5 to 8 s | Silent loop. |
| Website hero | 6 to 10 s | Silent loop. |

One generation makes one short clip. A longer piece is several clips, a Space run or a film edit on the user's computer.

## Hook and text rules

- The first one to three seconds carry the visual action, the spoken line and the caption. They must not repeat each other.
- Show the product by the third second on paid placements.
- Feed static: a headline of six words or fewer, one supporting line and one call to action.
- Story or Reel cover: four words or fewer.
- End on the offer and the call to action.
- Platforms change their limits. Check them before a large spend.

## The hand-off

When you hand off, paste the confirmed brief and the chosen card into the producing skill's request. Name produced assets by kind and id. The next skill reads each one again with get_asset. Never pass a card URL as an asset.
