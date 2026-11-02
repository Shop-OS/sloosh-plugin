# Shot list and AI shots (saas-product-video)

The shot list is the plan of every shot in the film. It is part of the free treatment. The user approves it before any paid round. This file also holds the prompts for the three AI shots. The Sloosh rounds and the spending rules are in SKILL.md.

## 1. The shot list

**Real screens only.** Every UI shot rebuilds a real screen of the user's product: a screenshot, a screen recording or a capture of the user's own URL (`references/ui-rebuild.md`). Never invent a screen, a feature, a button, a menu item, an integration or a number. A model never draws UI. If a beat needs a screen that you do not have, ask the user for it once. If the user cannot give it, cut the beat.

**Screen inventory (before the shot list).** List each screen you have: its file name, recording time or URL, what it shows, and light or dark. For each feature, collect the exact flow: the start screen, the screen of the action and the result. Capture light and dark only if the product has both and the film uses both. Show at most 4 features. Use the product's own labels.

**One row per shot, in film order:**

| Column | What to write |
|---|---|
| Time | the start and end on the beat grid (tl.py) |
| Beat | the job of the shot: hook, intro, UI entrance, interaction, camera move, result, before, after, outro |
| Source | an AI shot (desk, phone, world; c1, c2, c3), or a page in code (intro, ui, build, toggle, type). A UI row also names the real screen it rebuilds |
| Move | the camera or page move |
| Type | the exact words on screen, at most about 6 words per line |
| SFX | the sound on the shot's events |

**The grammar of a walkthrough** (the scenes are in section 6 of `references/walkthrough.md`):

| Slot | What it shows | Default |
|---|---|---|
| Opening | the pain over the realistic opener, then the product name | desk and phone clips with hype stacks, then intro.html |
| UI entrance | the product appears: the window springs in, or the camera whips to a new screen | S1 Window, S3 Settings |
| Interaction | one real action with the cursor: a click, a menu, typing, a toggle | S2 Menu, S4 Connect, S7 Typing |
| Camera move | a move inside the page: a sidebar pan, a macro zoom, a push-in | S3 pan, S6 push-in |
| Result | the outcome; unverified numbers carry Example data or Example output | build.html |
| Before and after | the same moment, flat and OFF, then switched on | toggle.html over the world clip |
| Outro | the logo lockup and the call to action | S8 logo, then the D End Card |

Give each feature one UI entrance and one interaction. Drop a slot the product does not have.

**Example rows (fictional product):**

| Time | Beat | Source | Move | Type | SFX |
|---|---|---|---|---|---|
| 0.00-1.25 | Hook | c1 desk, window 0.4-1.65 | slow push 1.00 to 1.05 | "40 INVOICES. / BY FRIDAY." | whoosh into the cut |
| 7.00-8.30 | UI entrance | ui.html S1, rebuilt from screen_main.png | the window springs in, dive to the account chip | none | whoosh, pop |
| 9.45-10.60 | Interaction | ui.html S3 and S4, rebuilt from integrations.png | pan down the sidebar, zoom to Status, click Connect | UI labels only | click, sparkle |

**Readable text.** UI text that must be read is at least 28 px on the film frame. Check it at phone width, not only on a large screen.

**The source note.** Deliver a short note with the film. List the source of each screen, each element that you simplified in the rebuild, and every number marked Example data or Example output.

## 2. The AI shots and their prompts

Three AI shots, each a still and then one clip. Make all the stills in one round and build the pages while they run.

### Stills (realistic, positive phrasing, aspect ratio = the film's)

The edit chain: desk (from scratch, or from the user's face photo), then phone (edited from the approved desk still: the same room, light and sleeve), then world (from the user's product photo if they have a physical product; otherwise the customer's world).

1. **desk** (the person at a laptop):
   - *Identity:* "Image 1 is the exact real person: keep the exact face, hairline, skin tone and texture, build and age." Or, for a fictional person: "a {{ROLE, e.g. founder in her 30s}}".
   - *Shot:* "three-quarter view from behind the left shoulder, seated at a desk, leaning toward a laptop whose screen faces away from camera, the person on the left third, room on the right for type."
   - *World and light:* "a lived-in {{ROOM, e.g. small studio office at night}}; the laptop screen is the key light, cool on the face; one warm practical lamp far right; {{BRAND_HINT, e.g. a terracotta mug}}."
   - *Camera:* "a cinema camera, 35 mm, f/2, ISO 3200."
   - *Realism:* "natural unretouched skin with visible pores and slight oil shine, uneven flyaway hairs, natural sensor noise, slightly underexposed, small everyday clutter on the desk."
   - *Finish:* "Looks like a frame grab from a real documentary. Clean raw footage: the laptop back, the walls and every surface are free of writing, logos and graphics."
2. **phone** (an edit of the approved desk still): "Keep exactly the same person, room, light and outfit as image 1. Change only the camera: a close-up of their right hand holding a phone at chest height, thumb over the screen; the screen is a soft even glow seen at a steep angle; 50 mm, f/1.8; the desk lamp bokeh behind." Add the realism and finish blocks.
3. **world** (the outcome): "Image 1 is the exact real product: keep its shape, proportions, materials, colours and printed label exactly as photographed. {{SCENE, e.g. resting on a wet city kerb at dusk, street lights as bokeh, a light rain}}; low angle, the product centred in the lower half; a cinema camera, 50 mm, f/2.8; true-to-life materials with fine dust; a frame grab from a real commercial shoot; clean raw footage, free of added writing." With no product, show the customer's world (a storefront, a team table, a city at dusk) with the same blocks.

**Reference images:** a JPG under 2 MB; a face photo as a tight crop; never a very large PNG.

### Clips (start frame = the approved still, one action)

Each clip starts from its approved still, uses the film's aspect ratio, runs about 5 s and has no generated audio. Each film size gets its own clips.

| Clip | 0-1.5 s | 1.5-3.5 s (the ONE action) | 3.5-5 s | Camera |
|---|---|---|---|---|
| c1 desk | still, typing slowly | leans in toward the screen, the screen light brightens on the face | holds, eyes on the screen | slow push-in toward the screen |
| c2 phone | the thumb hovers | taps twice, the phone tilts slightly toward the camera | settles | static macro, tiny handheld drift |
| c3 world | rain falls | a soft light sweep travels across the product | holds | slow push-in, 3% |

Add: "Real weight and physics. {Person: the face stays identical to image 1; natural blinking; hands anatomically correct.} {Product: the product stays one rigid object; every part, label and logo stays exactly as in image 1.} One continuous shot with no cuts, text, extra people or new objects."

**Counts:** 3 stills and 3 clips by default. **Light:** 1 still and 1 clip (desk only; the BEFORE and AFTER use the build page's hero image as a still with a handheld drift), or none (the Creative Team Intro tile).

**After each clip:** run `python3 lib/sheets.py clip clips/c1.mp4` (and c2, c3) in the film folder. Choose clean windows in the first 60 to 70% of each clip and write them into SHOTS as in-points.

**Reject a still and prompt it again, with the defect named, when you see:**
- any readable screen, letters, numbers, logos or UI anywhere (add "the screen faces away" or "a plain glow");
- plastic or tinted skin, a glowing rim light, a heavy teal-orange grade or haze (use the realism block again);
- a changed face, hairline or outfit between desk and phone (edit again from the approved desk still);
- a changed product part, shape, colour or label in the world shot (name the part-by-part truths: "the sole is one piece of white foam with a flat toe", "the label sits low on the left side");
- hands with wrong fingers, a room that changed between shots, or a light direction that changed.

**A refused face clip:** follow the notice in the result, the spending rules and "When a run delivers nothing" in SKILL.md. You may try once more with a tighter JPG crop of the face as the reference. That changes the request, so it needs its own quote, its own approval and a key with a higher version. If it is refused again, tell the user and wait.
