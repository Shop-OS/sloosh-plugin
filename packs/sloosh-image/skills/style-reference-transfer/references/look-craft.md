# Look craft for style reference transfer

Read this when you write the prompt or fix a weak result.

## Prompt shape

Fill the brackets from the style note. Keep the product as reference 1.

```text
Photograph the product from reference 1 (label, shape and colours exact) in the visual style of references 2 to 4.
Take their colour palette [terracotta, cream, deep green], light [hard low sun from the right, long shadows],
lens [35 mm, slight wide distortion], texture [fine film grain], set [raw concrete, dried grasses]
and framing [product low in frame, open sky above].
Do not copy any product, person, logo or text from references 2 to 4.
[Aspect ratio and space left for copy.] No text in the image.
```

## More craft rules

- Name the three strongest traits of the look. A long list makes the look weak and generic.
- Put the product photo first. The model treats the first reference as the subject.
- For several references that disagree, drop the busiest one. Two coherent references beat four mixed ones.
- If the user has no reference image, tell them this skill needs one. A look described only in words belongs to the product-imagery skill.
- If the chosen model takes a seed, note the seed with the style note. Reuse it for later shots of the same look.
- For 9:16 ad or social placements, keep the product and any copy space out of the top 14%, the bottom 35% and 6% at each side of the frame.
- Make one or two images first. Make more sizes only after the user approves the look.


## Fixes for a weak result

- If a reference's product, logo or text leaked in, put "do not copy any object, logo or text from the style references" first in the prompt. Drop the busiest reference.
- If the look is too weak, use one or two references, or the Space path. Name only the three strongest traits.
- If the product was redrawn, put the product photo first. Add a close crop of the label as a second product reference. Then the style references start at reference 3. Change the reference numbers in the prompt. Check that the model's reference limit from the model list still fits.
- If the look drifted toward a generic stock photo, tell the user. Name the set and the light more exactly.
