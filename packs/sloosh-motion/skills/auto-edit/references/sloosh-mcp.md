# What Sloosh does in this skill

The cut, the mattes, the render and the mix run on the user's computer and cost nothing. Sloosh does three
optional, paid things: a world edit of the cut (branch A1), B-roll stills and clips (A2, B1, B4), and sound
from a published Space. The tool descriptions and the server's guides win over this page.

## 0. The connection check (first)

Call `get_connection` once in the conversation. Read three things from the result:

- Whether spending is enabled. If it is not, give the user the settings link it returns and do no paid
  work. The local edit still runs.
- The allowance left, in millicredits. Divide it by 1000 to get credits.
- A plan notice, if there is one. Tell the user its message and link, and do no paid work.

Workspace and product come from the grant. Never infer them from tool inputs.

## 1. The loop for every paid step

1. Discover. Call `list_models` with the mode (video_edit, image_gen or video_gen). Take the model, its
   limits and its options from the result, never from memory or from this page.
2. Quote with `quote_generation`, or `quote_space` for a Space. A quote starts nothing.
3. Tell the user the credits of each step and the total, with any warning. Wait for the user.
4. Run with `generate` or `run_space`, the quote, one stable idempotency key such as
   `motion-autoedit-<project>-world-v1`, and confirmed=true only after the user approves this quote. The call
   returns an operation id at once. Never submit again to check on it.
5. If `show_generation` is available, call `show_generation` once with the operation id. If not, poll
   `get_generation` (or `get_space_run`) about every 15 seconds until it settles. A slow run is not a failure.
6. Call `get_asset` with each output's kind and id. Download the file from the URL it returns. If a link
   has expired, call `get_asset` again for a fresh one.

For quotes, expiry and errors, read the `generation`, `spending` and `recovery` guides with `get_guide`.

## 2. Getting a local file into the workspace

For a local file, follow the server's upload instruction for this client. For a file on a public HTTPS URL,
call `import_asset`, within the size limit in its description. For a file the workspace already holds, find
it with `list_assets`. Then call `get_asset` for its current URL. If none of these works, skip the paid step
and tell the user.

## 3. The sound kit and the music bed

film.py places kit sounds by file name and skips any that are missing. A sound goes in
`<project>/audio/sfx/<name>.wav` (or .mp3), the bed in `<project>/audio/music.wav` (or .mp3 or .m4a).
Then run `audio_prep.py`: it measures each sound's attack and peak and the bed's drop, so cues land on the
frame.

Take sound from these sources, in this order:

1. **The user's own files.** Ask the user to confirm they own or have licensed them.
2. **A published Space.** Call `list_spaces` with output type audio and a search such as sound effects,
   sound kit or music bed. Read each description with `get_space`. If one fits, read its form with
   `get_space_input_schema`, quote it with `quote_space`, and run it with `run_space` after the user
   approves (section 1). Save each output under its kit name. If no Space fits, tell the user. Sloosh
   `generate` has no audio mode, so do not try it for sound.
3. **Local synthesis.** `synth_kit.py --project <dir>` writes all twelve sounds, and `--music` adds a bed.
   Use `--only whoosh_air` to make one. The synthesized bed has a drop, so it suits A4 only.

The twelve kit names, with target lengths and characters (use them to match the user's files or a Space's
outputs). `synth_kit.py` makes its own lengths. audio_prep.py measures every sound, so a length need not
match:

| name | seconds | character |
| --- | --- | --- |
| whoosh_air | 0.9 | fast clean airy pass-by for a transition, short tail |
| whoosh_sub | 1.0 | deep low whoosh with sub rumble for a fast zoom-in |
| boom | 2.5 | one massive cinematic impact with a deep sub drop and a short dark tail |
| punch | 0.8 | tight punchy hit for type slamming on, snappy transient |
| odometer | 0.7 | a mechanical counter rolling, clicks speeding up then stopping on one solid click |
| riser | 3.0 | tension riser, noise swell with a rising tone, stops at the peak |
| shimmer | 2.0 | bright sparkle chime for a logo reveal, soft reverb tail |
| lights_off | 1.3 | a heavy stage light switching off, a deep thunk then a fading hum |
| key_tap | 0.5 | one soft crisp keyboard key tap |
| glitch | 0.5 | a short digital stutter burst |
| swipe | 0.6 | a quick whip-pan air movement, bright and crisp |
| portal | 2.6 | an airy rising whoosh with shimmering harmonics |

For the music bed, the briefs are in `references/prompts.md` §2. Transcribe each take with the local
transcriber and discard any take that has words in it. Measure the drop. Never trust a stated timing.

## 4. The world edit (branch A1)

1. Export the cut: `world.py export --project <dir>`. It writes `upload/cut.mp4`: the cut as prep made
   it, no type, short side 1080 px, tagged BT.709, and prints its length and size.
2. Call `list_models` with mode video_edit. Pick a model whose minimum and maximum video seconds take the
   cut's length and whose resolutions include the delivery size. If no model takes the cut, trim it or
   edit only the beats that need the world. Note whether the model lists cameraControls.
3. Get `upload/cut.mp4` into the workspace (section 2). Call `get_asset` for its URL.
4. Write the five-block prompt (`references/prompts.md` §1) with beat times from the cut. The prompt
   enhancer does not take edit modes.
5. Call `quote_generation` with mode video_edit, enhancePrompt false, the prompt, and modelConfig with the
   model's modelName, the resolution, a duration of the cut's length rounded up to a whole second, and
   generateAudio false (the mix is built locally from the original voice). Pass the cut as the one source
   video in uploadedAssets with its kind, id, type video and the URL from `get_asset`. Add cameraControls
   (camera, lens, aperture) only with keys the model lists. Use a lower resolution only for a look test.
6. Show the credits and any warning. Wait for the user to approve. Call `generate` with the quote and a
   stable idempotency key. Set confirmed=true only after the user approves this quote.
7. When it settles, call `get_asset` for the output and download it to `<project>/world/edit.mp4`.
8. Import it: `world.py import <dir>/world/edit.mp4 --project <dir>`. It measures the edit's length against the
   cut (film.py retimes by that rate), mattes every frame with Apple Vision, and aligns the plate to the
   cut by the two face tracks.
9. Add `"world": {"from_word": N}` to beats.json. The real room plays until word N, a short flash covers
   the switch, and the world plate plays from there (`until_word` switches back).

The world edit can also go to the user as its own version, untouched.

## 5. Traps seen in production

- A refused generation or a moderation error means the content filter flagged the input. In one test it
  was third-party logos on a cap and a shirt. Stop and ask the user how to go on, for example with footage
  without the logos. Never reword the prompt or alter the footage to get past a filter.
- Edit mode keeps the source camera and ignores camera moves in the prompt. Do camera work in film.py.
- The edit can come back slightly short. `world.py import` prints the rate. A rate far from 1 means the
  wrong file.
- Fast montages can sprout pseudo-letters on signs. Pull frames locally and look at every one at full
  size. Cover an offender with a flash frame or replace the section.
- A quote is single-use and expires. After an expired quote, quote again and ask for a new approval.
- A confirmation-required result on `generate` means the user must approve that quote first. Show the
  credits, wait for the user, then call again with confirmed=true.
