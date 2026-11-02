# QA and delivery

Nothing goes to the user until you have looked at it. Render a few stills, tile them, look, fix and repeat.

1. **Stills before full renders:** `python3 edit.py out/sheet.jpg 0.3,1.2,...`. A 16-still sheet covers every section in under a minute.
2. **Section sheets after the full render:** `python3 lib/sheets.py film out/<name>_vN.mp4 a b --fps 5` for the risky parts (transitions, the drop, UI, the end card). Read them in order.
3. **What to look for every time:**
    - text that overlaps text or the subject; words cut off mid-wipe or clipped at the frame edge; words off-centre
    - the cursor on the right element when it clicks
    - continuity: the same outfit, room, light and product shape across shots
    - cuts on the beats; no black frames at joins except the breath
    - anything that reads as generated: plastic skin, melted hands, extra fingers, warped labels, a changed product part
    - no text in the generated footage
4. **Technical report:** Run `python3 <director>/scripts/qa.py out/<name>_vN_final.mp4`. It checks the size, fps, duration, file size, loudness, true peak, audio clicks and frozen spans. Only the final hold may freeze. It lists every cut and flash frame, and writes labelled sheets and report.json into out/qa/. Check each flash frame with `qa.py <file> strip 6.2`, which shows 12 labelled frames from just before that time. `qa.py <file> at 1.0 4.5` gives full-size stills. It adds to looking; it never replaces it.
5. **Fix the system, not the frame.** When a word overlaps, place every word by measured width. When a cursor misses, place every cursor from measured boxes.
6. **Deliver:** `python3 audio.py out/<name>_vN.mp4` muxes H.264 and AAC into out/<name>_vN_final.mp4, under MAX_MB in audio.py, at -14 LUFS with a true peak at or under -1 dBTP. Save it in the user's project folder. Say in one line what changed, what needs their ears, and one next step. Keep tl.py, edit.py, audio.py, the ui/ pages, the prompts and the generation ids, so that any revision is exact.

**Quality checklist before you call it done:**

- [ ] The story reads with the sound off: hook, reveal or change, proof, payoff, end card.
- [ ] Every cut after the drop lands on a beat. The breath is there.
- [ ] Every generated clip started from an approved still. Identity, outfit, room and product match everywhere. No generated text anywhere.
- [ ] UI text is sharp, the cursor clicks the right element, and the real logo is used.
- [ ] Text never covers the subject's face or another word. Wipes finish on screen. Every line is inside the safe zone.
- [ ] The audio is original, with an SFX on every click, slam and drop, and a voice line on each slam when a voice-over was chosen. -14 LUFS, and a true peak at or under -1 dBTP.
- [ ] You have looked at the final file's contact sheet section by section. It has the briefed size and fps and is under the size cap.

**Process mistakes to avoid:** one prompt for the whole film; text, UI or logos asked of a model; brand names in prompts; a reference image over 2 MB (export it as a JPG first); planning shots without a check of the allowance; assuming that a download landed; pkill -f with a pattern that matches your own shell command; copying a reference's audio; a different font per slam; guessed x positions.
