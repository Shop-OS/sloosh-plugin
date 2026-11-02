# Reference study: frame by frame, then shot for shot

Before you write any prompt, turn every reference into contact sheets and write down its grammar:

```bash
python3 lib/sheets.py ref refs/ref.mp4                    # 1 fps overview of the whole reference, and every cut (frame, time)
python3 lib/sheets.py dense refs/ref.mp4 10.5 21 --fps 8  # 6-12 fps sheets of each key moment
python3 lib/sheets.py cuts refs/ref.mp4                   # every cut as frame number and time
```

Look at the sheets. Write the observed moves as a numbered list before you build anything, for example: "macro zoom on the account chip; 3D-tilted window; whip blur between scenes; chip shine; send button morphs into the logo; wide heavy italic two-line stacks". This list becomes the shot list and the code to-do list. The style skill's breakdowns are ready-made lists for its genre.

**To recreate a reference shot for shot:**

1. Extract the cut list to the frame (sheets.py cuts and dense). Write it as rows: (start, end, source, in_point, speed, zoom_from, zoom_to, focus_x, focus_y, tags). Many shots last only 4-10 frames.
2. Name every camera move, and save the first frame of each move (sheets.py dense at that time).
3. Attach a reference frame to a generation only after the user confirms that they may use the reference. Without that yes, rebuild each keyframe from the written move list only. With it, rebuild each keyframe from the reference frame with the composition-master rule (camera-shots.md). Attach the real subject photos as more references, and say what must change, part by part.
4. Animate each keyframe with its move described in words, and add the identity sentence (camera-shots.md).
5. Map reference time to clip time. A generated 4 s clip performs reference move k, which spans [a, b] in the reference. So reference time r plays clip time (r - a) x 4 / (b - a), and the edit keeps the reference's exact cut points.
6. Lock the music to the same grid: cut the user's track so that its drop lands on the reference's drop frame, or set the score's BPM to the reference tempo.
