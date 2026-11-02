# Round plan, checks and handoff

The campaign-orchestrator skill uses these shapes. The producing skill always gives the real quote before any paid work.

## The plan table

Show the plan before any quote. One row for each step.

| Round | Skill | What it makes | Inputs | Cost tier |
|---|---|---|---|---|
| 1 | product-imagery | 3 hero stills, 4:5 | product photo, brand kit | low |
| 2 | ad-variants | feed and story ads on the chosen hero, 4:5 and 9:16 | round 1 hero, headline, offer | low |
| 2 | product-video | one 9:16 clip that starts from the hero | round 1 hero | medium |
| 3 | finishing skill from the image or video pack | upscale of the hero, captions on the clip | round 1 hero, round 2 clip | low |

Cost tiers: low for a round of stills, medium for short clips, high for a multi-clip film or a catalog batch, varies for a Space run.

No core skill makes upscales or captions. If the Sloosh image or video pack is not installed, leave those rows out and tell the user.

## The round quote list

Show one list for each round before the approval. In round 1, the allowance left comes from get_connection, divided by 1000. From round 2 on, it comes from the newest quote's budget, which is already in credits. If a quote does not fit the daily limit, add the settings link.

```text
Round 2 of 3
1. Feed ad 4:5 on hero v2 (ad-variants): [credits from its quote]
2. Story ad 9:16 on hero v2 (ad-variants): [credits from its quote]
3. Clip 9:16 from hero v2 (product-video): [credits from its quote]
Warnings: [each quote's warning, or none]
Round total: [sum] · Allowance left: [allowance in credits] · Kept back for fixes: about a fifth
Approve this round?
```

## The continuity lines

The producing skills write their own prompts. Pass these three lines to every step:

```text
Product: the [product] from reference 1, label and proportions exact.
Brand: [the brand kit's voice, palette and photo style]
Campaign: [the message]; tone [tone]; avoid [what the brand never does].
```

## The checks between rounds

Look at each still. Ask the user to watch each clip in its result card. If there is no card, call get_asset with the clip's kind and id and give the user its URL to watch.

| Check | Pass | Fix |
|---|---|---|
| Product | Label, logo, colour and proportions match the product photo | Send it to the creative-iteration skill with "keep the product exactly as reference 1" |
| Text | Every word is spelled right and readable at phone size | Use shorter words, or make the text version from a clean plate |
| Hands and faces | They look natural | Reframe to hide the hands, or try another variant |
| Layout | There is space where the copy goes, and the frame does not cut the subject | State the layout in the brief, or make a new ratio instead of a crop |
| Brand | Palette, light and mood fit the brand kit | Pass the brand line again |
| Clip | No product morphing, no text that appears from nowhere, no extra limbs, the camera follows the brief | Shorten the clip, or start it from a cleaner still |

Mark each item pass, fix or drop. Only passed items feed the next round. After three failed tries on the same check, show the best result and explain the limit.

## The handoff block

Write this block at the end of each round. The next round reads it.

```text
Handoff after round 1
Made by: product-imagery
Passed: hero 4:5 v2 (generated, [asset id], image, 4:5, key [its idempotency key]), packshot 1:1 v1 (generated, [asset id], image, 1:1, key [its idempotency key])
Dropped: hero 4:5 v1 (label blurred)
Next: ad-variants and product-video use hero 4:5 v2
Notes: label spelling checked on every still
```

Record each passed item's name, asset kind (workspace or generated), asset id, type (image or video), ratio and idempotency key. Before the next round, call get_asset with each item's kind and id. Pass the kind, id, type and returned URL to the next round's producing skill. Never pass a URL from a card message.

## The quality bar

- The user confirmed the plan before any quote and approved each round once.
- No step was quoted before its input existed.
- Every still was viewed and every clip was watched before it fed the next round.
- No invented reviews, stats, names or offers appear in any output.

## The delivery list

Close the campaign with one row for each file: its name, its ratio, its length and audio for a clip, what was checked, what was not checked, and the credits each producing skill reported as charged. Offer the next step in one line.
