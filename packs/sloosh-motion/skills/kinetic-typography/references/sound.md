# Sound (audio.py)

| Preset | GENRE, BPM, key | Arrangement that follows the picture |
|---|---|---|
| Bold Poster | house 120 to 128, Am | filtered intro under the hook; riser into the drop; a 3-frame gap; full groove from the zoom-through |
| Swiss Clean | house 118 to 122 (or ambient), Dm | sparse; the one loud moment is the grid on the drop |
| Editorial Serif | luxury 80 to 95, Cm | piano-led; the strike is the turn |
| Lyric / Beat | trap 140 or the user's track, F#m | a word per beat; a black breath frame; the drop on the accent block |
| Variable Stretch | techno 124 to 130, Em | build through the stretches; drop through the counter |
| Scroll List | house 120, Gm | a tick per row; a suspense beat; a pop on the payoff |

KEY must be one the director's audiokit knows: F#m, Am, Em, Dm, Cm, Gm, C, F or G. Any other key stops audio.py with a KeyError.

SFX per word hit come from kf.sfx_cues(tl), from the same scenes the page animates:

| Event | SFX and level |
|---|---|
| stack, rise or lyric word landing | tick -15 or -20 dB |
| slam word | impact(0.9) -12 (the last -9) |
| stretch line | whoosh -15, 0.12 s early |
| frame | impact -8 and subdrop -12 |
| echo, echo walk | impact -9, shutter -12 per step |
| flap lock | tick -19 per tile (same lock formula), a whoosh at the start |
| count | 10 accelerating ticks -20, impact -11 at the landing |
| list | tick -16 per step, pop -12 on the payoff |
| grid wave, axis-wave skew snap | shutter -12 or -13 |
| zoom | impact on the landing, whoosh -11 into the hole, subdrop -10 through it |
| per-word inversion | shutter -13 |
| strike | click -14 |
| field wipe | whoosh -16, 0.2 s early |
| HITS | glitch (negatives) or shutter -12 |
| end | impact -13 and sparkle -14 |

A 1.5 s riser ends on the drop. Music sits at 0.8 under the SFX. Master to -14 LUFS.

Voice-over is optional, and only if the user asks: one shouted line per slam, for example VO = {t: ("Ends Sunday!", "shout")}. It uses only a voice already on the computer and fetches nothing. The music ducks to 45% under it.

You cannot hear the mix. Read the RMS report and ask the user to listen.
