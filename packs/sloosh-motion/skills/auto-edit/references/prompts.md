# Prompt library

Angle brackets are slots. Keep the block structure: the blocks are what the edit responds to. Write
every prompt in full yourself. The prompt enhancer does not take edit modes, so quote a world edit
with enhancePrompt false and keep the LOCKED and NO TEXT blocks word for word.

## 1. World edit (mode video_edit, branch A1)

### 1.1 The five-block template

```
Edit the source video. Locked-off <aspect> photoreal cinematic <shot size> shot, shallow depth of field.
<one sentence: who is on camera, what they wear, what is in frame, where the mic is>.

LOCKED, frame for frame: <their> face, identity, skin, glasses, hair, every mouth shape and every blink,
<their> hand gestures, <the wardrobe>, <the mic and its arm>, <their> position and scale, the fixed camera.
Lip sync matches the original exactly. Only the environment and the light on <them> change.

<BEATS: one paragraph per beat, "From a to b seconds, ...", one transformation each, light on the face named>

NO TEXT anywhere: no letters, numbers, logos, signs, screens, UI or watermarks. Photoreal, physically
plausible light, restrained palette per beat.
```

Take the beat times from the words prep.py printed for the cut (the output clock), not from the raw clip.

### 1.2 Beat paragraphs that worked (a four-beat hook at 1080p)

- Archive: "he is in a dim dusty museum archive at night with tall glass vitrines, one cold spotlight on an
  empty pedestal, and floating dust; cool blue-grey light."
- Launch party: "a hard light change: the room becomes a product launch party at its peak, warm tungsten
  and amber light on his face, confetti falling, silhouettes of a crowd with raised phones, champagne
  glasses catching light, lens flare from a spotlight, no screens, no signs."
- Time drains: "time rushes forward as the party drains away into cold overcast grey; confetti turns into
  dead leaves and dust, the crowd vanishes, and pale window light takes over, desaturated."
- Empty hall: "it settles into a vast empty concrete hall with stacked folding chairs, one deflated balloon
  on the floor, a tumbleweed of tangled cables rolling past behind him, flat white light, and total stillness."

What failed on a first look test: "screens showing abstract rising bar shapes" grew pseudo-text labels.
Never put screens, monitors, dashboards, posters or signs in a beat.

### 1.3 Camera controls on the quote

When the chosen model lists cameraControls in `list_models`, pass a camera, a lens and an aperture from
that list, for example camera modern, lens clean-sharp and aperture f-1-4-wide-open. An anamorphic lens
suits a launch or trailer beat, a warm vintage lens a lab or workshop. Take the keys from the list, never
from this page. Edit mode keeps the source camera, so camera moves belong in film.py, not in the prompt.

### 1.4 Other world ideas by beat type

- Claim: "a bare white cyclorama studio, one hard key, long shadow"
- Number or proof: "a server hall, rows of racks glowing a single colour, cold air haze" (no screens)
- Turn: "the same room at golden hour, blinds throwing stripes, dust in the light"
- Payoff: "night exterior, a city skyline behind glass, rain on the window, the room lit only by the city"
- Call to action: "the real room again" (`until_word` in beats.json switches back)

## 2. Sound briefs

These are briefs, not prompts for `generate`: it has no audio mode. Use them to choose among the user's
licensed tracks, to fill a published Space's form, or to set the synthesized kit.

### 2.1 Underscore for a world-edit hook

```
Minimal cinematic underscore for a short film scene, <n> seconds, instrumental only. A quiet felt piano and
a low sustained string drone open it. A soft warm pulse enters and gently swells with anticipation through
the middle. Then the pulse collapses and everything thins to one cold held note with faint tape hiss and
room air at the end. Intimate, restrained, slow, around 70 bpm. No drums, no drop, no trailer hits, no
vocals, no lyrics, no singing, no electronic dance music.
```

Never name artists or songs in a brief. Describe the sound.

### 2.2 Trailer bed (A4 only)

Four sections in this order: an intro that leaves room for the voice, a short build that stops dead for
half a beat, a drop (a big low hit, heavy sub, driving drums, bright wide synths) and a ring-out. About
120 bpm, instrumental, no vocals. Put the drop a little before the payoff word. Section lengths drift, so
`audio_prep.py` measures the drop. Never trust the brief's timing. Transcribe each take with the local
transcriber and discard any take that has words in it.

### 2.3 Sound effects

The twelve kit names and their characters are in `references/sloosh-mcp.md` §3. On a cinematic edit use
at most one, on the cut.

## 3. B-roll and plates (branches A2, B1, B4)

### 3.1 Reference sheet first (mode image_gen)

```
<subject> on a plain <grey|white> seamless background, three-quarter view, soft studio light, photoreal,
no text, no logo. One object, centred, room around it.
```

Pass it with role reference on every later image so the montage reads as one idea.

### 3.2 Clip from a still (mode video_gen, about 5 s; a lower resolution for a look test only)

```
<the still's content>. Slow push in, handheld micro-drift, natural weighty motion, shallow depth of field,
real light. No text.
```

Pass the still with role start_frame.

### 3.3 Generated B-roll that matches phone-shot B-roll (the lab look)

```
Handheld close-up of <hands doing the thing> on a <desk / bench>, overhead warm practical light and a cool
window fill, slight motion blur, phone camera look, shallow depth of field. No text, no logos.
```

Match the cadence: cut every generated clip at 1.0 to 1.5 s like the real ones.

### 3.4 App-icon stickers

Use the user's own icon files for real apps. Never reproduce another company's mark. For an invented app,
an image_gen prompt such as "a rounded-square app icon for <colour, symbol described in words>, flat,
centred on a plain white background, no text" gives a plate. Key out the white background locally.

## 4. Logging the user's footage (local)

Pull one frame a second with ffmpeg into a contact sheet and look at it. For each shot, note the start and
end time, what is in frame (nouns), the camera motion (static, handheld, push, pan), the light (warm, cool,
mixed), whether a person or hands show, whether any text or logo shows, and a usable in and out point.
The shot log is the B-roll library. Match the transcript's nouns against it before you generate anything.
