# Shallow depth of field: a blurred room behind a sharp person

Two ways. Use the first on every talking-head branch. Add the second when the room itself changes.

## 1. Local, from the matte (free, exact)

`prep.py` writes an Apple Vision person matte for every kept frame (macOS only). `fx.plate_and_fg` splits
each frame into a halo-free background plate B and the subject F, such that `B*(1-m) + F*m == I`. The
`dof` beat blurs only B:

```json
"dof": { "blur": 18, "bokeh": 0.5, "bokeh_threshold": 0.72, "ramp": 0.0 }
```

- `blur` 12 feels like a 35 mm lens at f/2.8, with the room still readable. 18 feels like a 50 mm lens wide
  open and is the default. 28 is a long lens: the room becomes colour. Above 32 the matte edge starts to
  show, so stop there.
- `bokeh` blooms highlights above `bokeh_threshold` into soft discs, so lamps, a ring light or a window read
  as lens bokeh, not mush. Use 0.4 to 0.6.
- `ramp` eases into the blur from `from_word`, a rack-focus feel on "and here's the thing". 0 means always on.
- Blacks lift a little under the blur on purpose: a blurred room never has true black.

The subject is never touched. A sharp face in front of a soft room is the strongest cinema-camera cue a
phone clip can borrow.

Hair and glasses edges are where the matte shows. Check a still at 200 % on the hair line. If the edge
looks cut out, lower `blur` until it does not.

## 2. In the world edit (paid, part of the prompt)

When the room is rebuilt anyway (A1), ask for the depth in the prompt and in the camera controls:

- In the prompt's visual-language block: "shallow depth of field: he is sharp, the world behind him is soft,
  practicals bloom into bokeh".
- On the quote, pass `cameraControls` with a camera, a lens and a wide-open aperture. Take the keys from the
  model's `cameraControls` in the `list_models` result, never from memory. An anamorphic lens gives oval
  bokeh and a horizontal flare on a launch beat. A warm vintage lens suits a lab or workshop.

Then still run the local `dof` at a low `blur` (8 to 10) over the world plate, so both plates share one depth.

## What it is not

Not a vignette, not a radial blur, not a blur that includes the subject. A blurred subject edge reads as fake
faster than no blur at all.
