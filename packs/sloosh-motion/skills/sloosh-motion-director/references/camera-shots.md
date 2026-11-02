# Camera shots: stills and clips

Sloosh makes the stills and the clips. The skill's "Make shots with Sloosh" section holds the round flow and the spending rules. This file holds the craft.

**Plan in parallel and build while you wait.** While a round renders, write tl.py, the type page and the score on placeholders. edit.py runs on placeholders, so the structure is checked before the real shots land. Reuse earlier stills and clips of this project before you plan new ones.

### Stills

Use positive phrasing only. A model can read "no X" as an instruction to include X. Describe what is in the frame. Build every still prompt from these blocks, in this order:

1. **Identity:** "Image 1 is the exact real {product or person}: keep its shape, proportions, materials, colours, and printed label and logo exactly as photographed." For a person: "keep the exact face, hairline, skin tone and texture, build and age."
2. **Shot:** the subject, the action or pose, the framing, the camera height and where the subject sits in the frame. Leave room for the type where the type system needs it.
3. **World and light:** a physical set and a practical light source with its direction. "The monitor is the key light." "One narrow strip softbox from camera-left at 45 degrees, a cool rim from behind right."
4. **Camera:** a lens, a stop and a sensor feel, in plain words. "A full-frame cinema camera, 35 mm lens, f/2, high ISO." Medium format for packshots.
5. **Realism:** "natural sensor noise, slightly underexposed, real micro-texture". For skin: "natural unretouched skin with visible pores and a slight oil shine, uneven flyaway hairs". For sets: "a lived-in set with small everyday imperfections". For products: "true-to-life materials with fine dust and handling marks".
6. **Finish:** "Looks like a frame grab from a real documentary or commercial shoot. Clean raw footage: every surface is free of added writing, captions or graphics."

**Continuity:** one room, one outfit and one light design from start to end. Make each new still by editing the previous approved still. Pass it with the real identity photo and say "keep exactly the same room, light and outfit; change only {the pose, the camera or the action}". Never make each still from scratch.

**Composition-master rule** (to recreate a reference or match a look): "The first attached image is the composition master: recreate it exactly, with the same camera position, angle, crop, lens, subject position and scale, and the same lighting. Change only the {subject}." Then list part-by-part truths, for example "slim three-element LED taillights". Attach a reference frame as the composition master only after the user confirms that they may use that reference.

**Never name a real brand, product line, person or film as a style reference** in any prompt. Describe the look in physical terms. The user's own product appears only as "the product in image 1".

After a still is made, look at it with `view_asset` for a quick check. `view_asset` shows only a small preview. Then download the still from the URL that `get_asset` returns into plates/, and look at the local file at full size before you approve it. Reject a changed letter, a wrong part or shape, colour drift, plastic skin, extra fingers or a lighting change. Make it again with the defect named, in a new round.

### Clips

One clip is one shot: one subject action and one camera move. Use the approved still as the start frame, the film's aspect ratio (3:4 for a 4:5 film when 4:5 is not offered), a length of about 5 s, and no generated sound when the model offers that choice. Template:

```
Realistic {handheld documentary | locked-off commercial} footage. The first frame is image 1: same {person or product},
same {room or set}, same light, same composition.
0-1.5 s: {calm start}. 1.5-3.5 s: {the one action}. 3.5-5 s: {settle and follow-through}.
Camera: {one move: slow push-in | static behind the shoulder with a handheld jolt | slow orbit of 20 degrees | lateral slide}.
Real weight and physics, natural motion blur on fast moves.
{Product: The product stays one rigid object; every part, label and logo stays exactly as in image 1.}
{Person: The face stays identical to image 1; natural blinking; hands anatomically correct.}
One continuous shot with no cuts, text, extra people or new objects.
```

Everything above the last line is positive. The last line is the only exclusion sentence.

**Faces:** get the intake yes first. Then animate the approved face still as the start frame. If a run settles with nothing delivered because a reference shows a real person who is not verified yet, follow "When a run delivers nothing" in the skill. If a face clip is refused for another reason, tell the user what happened. A retry with a changed input (start frame only, a slightly wider framing) needs a new quote and a new approval. If it is refused again, tell the user that the platform may need them to confirm the person's consent, and wait.

**After every clip:**

1. Download it into clips/ and run `python3 lib/sheets.py clip clips/c1.mp4` (3 fps).
2. Find the useful in and out points: the grab, the eyes opening, the lid snapping.
3. Choose each clip's clean window, usually inside the first 60-70 %, because faces, hands and labels degrade later.
4. Make those moments sync points in tl.py, and trim bad frames by number.

For ffmpeg treatments of a clip before the edit (datamosh, pixel sort, threshold flashes, speed ramps, freezes), run `python3 <director>/scripts/clipfx.py list`. Most looks are filmkit tags instead.
