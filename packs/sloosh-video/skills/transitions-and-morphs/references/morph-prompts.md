# Morph prompts

Use these to write the prompt for one start-frame and end-frame clip.

## The prompt shape

"Start exactly on frame A and end exactly on frame B. [What changes, such as: the colour sweeps across the bottle from black to sand, left to right.] [What stays locked: camera, framing, label, shadows.] Smooth, weighted motion, no bounce, no cut. No new objects or text. The last second holds still as frame B."

For a zoom-through match cut: "The camera pushes into [the element in A] until it fills the frame, and the frame becomes B without a cut."

## Recipes

| Morph | Length | How to make frame B | Prompt cue |
|---|---|---|---|
| Colourway A to B, product locked | 3 s | edit frame A to the second colour | the colour sweeps across the surface |
| Scene change, same camera | 4 to 5 s | edit frame A to add or remove the object | name what enters and what leaves |
| Pose to pose | 5 s | a second photo of the same person and outfit | the body moves through one natural step to the end pose |
| Day to dusk | 5 to 8 s | relight frame A as the same room at dusk | the light changes, nothing else moves |
| Before to after | 4 s | a truthful photo of the real result | truthful frames only, no invented result |
| Zoom-through | 3 s | a detail shot of the element in frame A | frame A is the wide, frame B is the detail |

## Fixes

- The end drifts from frame B: shorten the clip, or add "the last second holds still as frame B".
- The model rejects the pair: the ratios differ. Remake frame B at frame A's ratio.
- Objects appear mid-way: simplify the prompt. If `list_models` shows that the model takes reference images together with start and end frames, add one of the product.
- The model needs a start frame whenever it takes an end frame: pass both frames.
- Audio is off unless the user wants sound.
