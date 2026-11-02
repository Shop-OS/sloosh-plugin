# Shot prompt for a direct lookbook frame

Write one prompt per shot. Keep the references in the same order in every prompt of the set.

- Reference 1: the garment photo, front or back as the shot needs.
- Reference 2: the model photo. When there is no model photo, the approved hero frame, from the second round on.
- Reference 3: the approved hero frame, for face, light and colour grade continuity, from the second round on.

The hero frame is the first frame of a set. It has no reference 3. With no model photo, it has no reference 2 either: describe the model in words, such as age range, hair, build and skin tone. Leave out the line "Match the light and colour grade of reference 3".

## Structure

```
Fashion catalogue photo: the model in reference 2, same face and hair, wearing the garment in reference 1 with its exact colour, print and fit.
<pose, such as a three-quarter turn, weight on the back foot, hands relaxed>, <framing, such as full length>, on <backdrop, such as a seamless light grey studio>.
Soft studio key light from the left, fill from the right, 85 mm lens look, eye level, <ratio>. Match the light and colour grade of reference 3.
<one line from the brand kit photo style>. No text, no props, no extra garments.
```

## Default shot list

| Shot | Framing | Pose |
|---|---|---|
| Hero | Full length | Facing the camera, weight even, arms relaxed |
| Three-quarter | Full length | Turned about 45 degrees, weight on the back foot |
| Side | Full length | Profile, one foot forward |
| Back | Full length | Back to the camera, head turned slightly |
| Detail | Close-up | Fabric, print, collar, cuff or hem |

## Checks

- The face and hair match across frames.
- The garment colour, print and fit match the garment photo.
- Each pose matches the shot list.
- The light matches the backdrop.
- There are no extra limbs and no invented text.

## Fixes when a check fails

| Problem | Fix |
|---|---|
| The face drifts between frames | Add an approved frame as reference 3. Change only the pose in this round, not the backdrop. |
| The garment colour shifts under location light | Add "exact colour as reference 1". Use a ghost mannequin garment photo. Shoot the studio set first, then the location. |
| The print or logo is wrong | Use a sharper, flatter garment photo. Add a detail shot with the print filling the frame. |
| The fit is wrong at the shoulders or hem | Name the cut in the prompt, such as dropped shoulder or cropped hem. Use the back photo for back shots. |
| Extra limbs or fingers | Use a simpler pose. Ask for hands relaxed at the sides or in pockets. |
| A second garment appears | Add "only the garment in reference 1" and name the lower half, such as plain black trousers. |
