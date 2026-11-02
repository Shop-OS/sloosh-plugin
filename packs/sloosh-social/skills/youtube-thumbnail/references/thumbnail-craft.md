# Thumbnail craft

Use this file for step 3 (concepts), the direct path prompt and the quality check.

A good thumbnail has one focal subject, one information gap and 3 to 5 words. It reads at 120 px wide. It promises only what the video delivers.

## Concept frameworks

Write up to five concepts, one per framework. Skip a framework the video does not support. Recommend the concept with the strongest single information gap.

| Framework | Use it when | Example headline |
|---|---|---|
| Reaction and object | A person reacts to one thing the video is about. | WORTH IT? |
| Before and after | The video really shows a change. Use a split frame. Do not use it otherwise. | 30 DAYS LATER |
| Versus | The video compares two things. Do not mock a real brand or product unless the video shows that claim and the user confirms it. | CHEAP VS PRICEY |
| Result number | The video has a real, checked number. | 1 WINNER |
| Question | The video answers one clear question. | DOES IT WORK? |

Rules for every concept:

- One focal subject and one information gap.
- A headline of 3 to 5 words. Each word has at most 10 characters.
- The headline adds to the title. It does not repeat it.
- The promise matches what the video shows.

## Craft rules

- One focal subject. Put the face on one third and the object or result on the other.
- Show a clear emotion that fits the video, such as surprise or doubt. Do not fake a reaction the video does not have.
- Use at most three colours and a flat or blurred background. Remove small details.
- Make the headline large, heavy and high-contrast, with a thin dark outline. Use all caps for short words.
- For 16:9, keep the headline and face out of the bottom-right corner, where YouTube shows the video length.
- Put a vertical cover's headline in the middle of the safe area, between 14% and 65% from the top.
- When list_models offers a resolution choice, pick one at least 1280 px wide for 16:9.

## Prompt template

Fill each bracket. Keep the headline word for word in quotes.

"YouTube thumbnail, 16:9. [Person from reference 1], [expression, such as wide-eyed surprise or a doubtful frown], framed on the [left third], looking at [object, large, on the right third]. Headline exactly: "[HEADLINE]" in a heavy condensed sans serif, [colour] with a thin dark outline, [top left], at least 15% of the frame height. Background: [one flat colour or a blurred, simple scene]. High contrast, at most three colours, no other text, no small details. Keep the face exactly as in reference 1."

For a vertical cover: use 9:16 and put the headline between 14% and 65% from the top. Keep the face and the text inside the 9:16 safe zone in SKILL.md.

With a logo: add "Logo from reference 2, small, in the [top right], unchanged."

## Variants

- To vary an approved thumbnail, pass it as a reference image in a new quote. Tell the user the model makes a new image. The face and layout can shift.

## Fixes

- If a headline word is wrong, use shorter or fewer words. Or pick another model whose description says it renders text well.
- If the face drifts, ask for a sharper reference. Put the face instruction first in the prompt.

## Quality check

Look at each image with view_asset and check:

- Every headline word is spelled exactly as approved.
- The face matches the reference.
- There is one focal subject.
- It reads in one second at 120 px wide.
- There is no extra or invented text.
- The bottom-right corner of a 16:9 thumbnail is clear.
- The claim is true for the video.

## Naming

Name each image from the video, the concept and the version, for example serum-test-reaction-v1.
