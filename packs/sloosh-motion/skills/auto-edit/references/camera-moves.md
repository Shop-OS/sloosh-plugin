# Camera moves: subtle in, subtle out, and when

All moves are float-precise crops of the plate (`fx.cam_warp`), anchored on the face so the eyes stay put.
Amounts are zoom deltas (0.03 = 3 %). Everything here is set in beats.json under `camera` and `punches`.

| move | what | amount and time | when |
| --- | --- | --- | --- |
| settle | a micro push right after every cut, eased out | 0.03 over 0.22 s | every cut: it hides the jump and reads as a camera finding its frame |
| drift in | one slow push across the shot | 0.02 per shot | the default on a claim, a build or a list |
| drift out | one slow pull across the shot | 0.02 per shot | a reveal, an aside, "and here's the thing", after a tight claim |
| breathe | a sine in-and-out so slow it is felt, not seen | about 0.006, 4 s period | long holds on the speaker (A2, A3) |
| punch | a quick push on a word | 0.08 to 0.13 over 0.22 s | the number, the product name, the turn |
| pull | a quick ease-out on a word (negative `punches[].amount`) | -0.06 to -0.10 over 0.3 s | a deflation, a punchline that lands flat on purpose |
| cut-in | a punch so short it reads as a cut | +0.10 over 0.04 s | the payoff word: a cut, never a zoom |
| alternate | shots alternate base 1.0 and 1.10 | per shot | jump-cut cover on caption cuts (A3) |
| end push | a long push into the end card | set by the end card | only with a card |

Rules:

1. One direction per shot. A push then a pull inside one shot reads as a mistake.
2. The eyes stay where they are. Moves are anchored on the face (`fx.anchor_cam`). A crop for a vertical
   edit from a landscape source follows the face.
3. Zoom never drops below 1.0, because the frame must stay filled. To allow a pull, set `camera.base`
   above 1.0.
4. Nothing moves on the caption layer. Type is pinned to the frame, not to the camera.
5. Hard cuts only. A two-frame light flash at most on a plate switch.
6. Motion blur comes from sub-frame samples that never cross a cut. The engine does this at 24 fps.

Settings that read as film on a seated talking head (A2, A3):

```json
"camera": { "style": "breathe", "base": 1.04, "settle": 0.03, "drift_amount": 0.02, "drift": ["in", "out", "in"] }
```

Settings for a hook with a payoff (A1):

```json
"camera": { "style": "push", "base": 1.0, "settle": 0.0, "drift_amount": 0.05 },
"punches": [{ "word": 19, "amount": 0.10, "seconds": 0.04 }]
```
