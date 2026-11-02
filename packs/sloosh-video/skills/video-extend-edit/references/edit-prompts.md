# Prompts and fixes for video extend and edit

Fill the brackets. Keep each prompt to the change. Do not add on-screen text.

## Branches

- Extend: the clip ends too soon. Collect what happens next.
- Edit: one thing is wrong, such as the light, an object, the time of day or the background. Collect what to change and what to keep.
- Restyle: the whole look changes, such as a new setting, a grade from a reference or a film look. Collect the look in words and an optional reference still.

## Rules per branch

- Extend: continue the scene with no cut. Keep the subject, the camera move, the light and the pace. Describe what happens next in one clause.
- Edit: change only one thing. List what must stay exactly as in the source: the product, its label, the camera move, the framing and the pace.
- Restyle: apply the look evenly to every frame. Keep the product colours, the motion, the timing and the length.

## Prompt templates

| Branch | Template |
|---|---|
| Extend | Continue the scene past the last frame. [What happens next, in one clause]. Same subject, same camera move continuing, same light. No cut. No on-screen text. |
| Edit | Change only the [time of day, background or object]: [the new state]. Keep the product, its label, the camera move, the framing and the pace exactly as in the source. No on-screen text. |
| Remove | Remove the [object] from the scene. Fill the space with what is behind it. Keep everything else exactly as in the source. No on-screen text. |
| Remove: rights marks | Do not remove a watermark, a credit or a rights mark from a clip. If the user asks for this, say no and stop that edit. |
| Restyle | Restyle the whole clip as [the look, such as 35 mm film with warm halation and soft grain, or a festive living room at night with lamps and marigolds]. Keep the product, its label and colours, its motion, the camera move and the timing exactly as in the source. Apply the look evenly from the first frame to the last. No on-screen text. |
| Restyle with a reference | Match the colour palette, contrast and light direction of reference 1. Take the subject, the motion and the framing from the source video. Keep the product colours exactly. No on-screen text. |

## Examples

- "Extend this clip so the bottle keeps turning": extend branch, mode `video_extend`.
- "Make the background dusk instead of noon, keep the product": edit branch, mode `video_edit`.
- "Remove the extra cup on the table": edit branch, remove template.
- "Put this turntable clip in a festive living room": restyle branch. Look for a scene transformation Space first.
- "Match this clip's grade to my reference still": restyle branch. Look for a palette transfer Space first.

## Checks for the user

- Extend: the seam at the join.
- Edit: nothing else changed.
- Restyle: the look is even, it does not flicker and the length stays the same.
- All three: the product label and colours.

## Fixes

| Problem | Fix |
|---|---|
| The seam at the join shows | Ask the user for a cut of the clip that ends on a calmer moment, then extend again. Or make the next shot as a new clip from a product image. |
| The edit changed too much | Shorten the instruction to one change. Add a "keep exactly" list of what must not move. |
| The look recoloured the product | Start the prompt with "the product keeps its exact colours". Add the product photo as a reference when the model takes references. |
| The restyle flickers | Use a shorter or slower source clip. Or use a scene transformation Space if its description says it keeps the product apart from the new setting. |
| The source is too long for the model | Pick another listed model that takes a longer source. Or ask the user for a shorter cut. |
| Only a small tone change is needed | Tell the user a model run may be more than the job needs. Let the user decide before any quote. |
