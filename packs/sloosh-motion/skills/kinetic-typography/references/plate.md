# The plate

Read SKILL.md, "Optional plate", first. The consent and rights checks there come before any quote.

## Plate prompt (the still)

Use positive phrasing only. Describe the look physically.

```
Image 1 is the exact real {{SUBJECT}}: keep {{identity: face, hairline, skin texture | shape, label, colours}} exactly as photographed.
{{SUBJECT}} {{pose / placement}}, framed so the top {{28-32}}% of the frame is clean {{seamless paper / plaster wall / sky}} in
{{FIELD_BG tones}} behind the head {{/ product top}}; the subject's head top sits at {{30}}% of the frame height, centred.
One {{narrow strip softbox from camera-left at 45 deg}}, soft falloff, {{cool rim from behind right}}.
Shot on {{medium format 80 mm f/4 | full-frame cinema camera 50 mm f/2}}, ISO {{400}}, natural sensor grain, true-to-life skin with
visible pores {{| real micro-texture and fine handling marks}}. Looks like a frame grab from a real {{editorial / commercial}} shoot;
every surface is free of added writing, captions or graphics.
```

- Never name a brand, product line, public figure or film in a prompt.
- Never ask for text, a masthead or a logo in the still. The type is code.
- The still comes first. Make the animated plate only after the user approves the still.

## Use the plate

- Cut-out: python3 <kinetic-typography>/scripts/cutout.py plates/plate.jpg plates/plate_matte.png [--box x0,y0,x1,y1]. It uses GrabCut by default.
- The --rembg option uses rembg only if it is already installed. Ask the user before anyone installs it, because it also fetches a model on first use.
- Look at the matte. Hair and fingers need a clean edge. The matte must come from the same approved still.
- Truth rules: the plate keeps the subject's identity and the product's shape exactly. The head may overlap at most the lower third of the masthead's last line, and the line must stay readable. Text never covers the face.
- In tl.py: PLATE = dict(path="plates/plate.jpg", matte="plates/plate_matte.png", t=[0.0, DROP], z=[1.0, 1.06], focus=[0.5, 0.4], look="dim").
- look is dim (x0.72, for light ink), duo (duotone dark to light), bw or raw. While the plate is on, set the field ink to a light colour (see USE_PLATE in examples/editorial-serif/tl.py).
- Animated plate: set PLATE_CLIP = "clips/plate.mp4" in tl.py. The bold-poster edit.py then uses it through the director CutList as the background instead of the fields, with one slow 1.00 to 1.05 push. A moving plate gets no cut-out, so keep the type off the subject.
- Before the real still exists, python3 <kinetic-typography>/scripts/make_placeholders.py <film> writes a stand-in plate and matte.
