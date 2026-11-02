# Room prompts

Each prompt has four parts in this order: the room line, the placement and scale line, the light line and the keep line. Give the room as reference 1 and the product as reference 2.

## Placement skeleton

```
The room in reference 1, with the same camera, walls, windows and floor.
Place the [product] from reference 2 [against the back wall, centred under the window], at real scale: it is [180] cm wide and [85] cm high, about [the height of the window sill].
Match the room's light from [the left window]. Cast a soft contact shadow on the floor to the [right]. Reflect the room colours faintly on glossy parts.
Keep the product's exact shape, fabric, colour, legs and hardware. Remove the [old sofa] it replaces. Change nothing else. No text.
```

## Restyle skeleton

```
The room in reference 1, with the same camera, walls, windows and floor plan.
Restyle the room in a [Scandinavian] style: [pale oak, white linen, soft wool, warm low light].
Place the [bed frame] from reference 2 as the hero piece [against the back wall], at real scale: it is [160] cm wide.
Keep the product's exact shape, fabric, colour and legs. Keep the walls, windows, doors and camera. No text.
```

## Described room skeleton

Use this when the user has no room photo. The product is the only reference.

```
A [bright living room with white walls, a pale oak floor and a large window on the left], eye-level camera, natural daylight.
The [product] from reference 1 stands [against the back wall], at real scale: it is [180] cm wide, about [the height of the window sill].
Soft contact shadow on the floor. Keep the product's exact shape, fabric, colour and legs. No text.
```

## Scale cues by product

| Product | Size words | Reference object |
|---|---|---|
| Sofa or bed | width and seat or frame height in cm | the window sill, a door handle |
| Floor lamp | total height in cm | the armchair back, the door frame |
| Rug | width and length in cm | the sofa's length, the floor boards |
| Wall art or mirror | width and height in cm, hung at eye level | the sofa back, the light switch |
| Side table or stool | height in cm | the sofa arm, the bed side |
| Pendant light | drop length and shade width in cm | the table top, the ceiling height |

## Fixes

| Problem | Fix words |
|---|---|
| Product too big or too small | Give both scale cues: the size in cm and a reference object. |
| Product floats | "the feet touch the floor, soft contact shadow under the product" |
| Shadow in the wrong direction | Name the light source and the side the shadow falls to. Use a relight Space for small decor. |
| Other furniture changed | Put "change nothing else" first. Name the one piece the product replaces. |
| Perspective off | "the product's lines follow the floor boards and the wall edges" |
| Fabric or colour drifted | "keep the exact fabric weave and colour of reference 2" |
