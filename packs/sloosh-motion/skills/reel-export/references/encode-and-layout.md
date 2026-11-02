# Encode and layout for a vertical export

This file holds the numbers behind `scripts/reel_export.sh`, `scripts/check_reel.sh` and `assets/overlay.html`. Read it when a check fails or the user asks why.

## The 9:16 frame

The frame is 1080x1920. Every position below is a share of the frame, so it holds at any size.

| Zone | From | To | What goes there |
|---|---|---|---|
| Top band, kept clear | 0% | 14% | Nothing. The app's header and the account name sit here. |
| Logo row | 14% | 19% | Up to four logo tiles, centred. |
| Hook | 20.5% | 31% | Two lines, centred, inside 6% side margins. |
| Video box (fit) | 32% | 65% | The source video, scaled to fit and centred. |
| Bottom band, kept clear | 65% | 100% | Nothing. The caption, the buttons and the sound bar sit here. |
| Sides, kept clear | 0% and 94% | 6% and 100% | No words and no logos. |

- A 16:9 source fills the full width of the video box. A 1:1 or 4:5 source sits smaller in the box, with background at each side.
- Fill mode scales the source to cover the whole frame and crops the centre. It loses the sides of a wide source. Use it only when the subject and any words in the source stay inside the middle of the frame. If the source is already 9:16, use fill. It scales the video without a crop.
- Words and logos must stay in the safe zone in both modes.

## The hook

- Two lines. Four words or fewer on each line. The viewer reads it in one second with the sound off.
- Line 2 takes the accent colour. Line 1 is white.
- The overlay page measures each line and shrinks it until it fits the safe width. If it must shrink to 40 px, the page throws "hook too long" and the render fails. Ask the user for shorter lines.
- Use the user's words exactly. Do not add a claim, a price or an offer.

## Logo tiles

- Each logo sits on its own dark rounded tile, so it stays legible on light frames.
- Use the logo file the user gives. A transparent PNG works best.

## The encode

| Setting | Value | Why |
|---|---|---|
| Video codec | H.264 (libx264), High profile, CRF 18 | Every app accepts it. Some apps re-encode HEVC badly. |
| Pixel format | yuv420p | Other formats play wrong on some phones. |
| Range | limited (tv) | A full-range file looks washed out after upload. |
| Colour tags | BT.709 primaries, transfer and matrix | Untagged files shift colour in some players. |
| Frame rate | constant 30 fps | Variable frame rate can drift out of sync with the sound. |
| Audio | one AAC stereo track, 48 kHz | Some apps reject a file with no audio, so a silent track is added when the source has none. |
| Container | MP4 with faststart | The file starts to play before it has fully loaded. |

## What check_reel.sh passes

| Line | Pass value |
|---|---|
| video codec | h264 |
| size | 1080x1920 |
| pixel format | yuv420p |
| colour range | tv |
| colour space | bt709 |
| audio streams | 1 |
| audio codec | aac |
| faststart | yes |

## When a check fails

- Washed out after upload: the source was full range or HEVC. Export again with the script. It writes limited range and BT.709.
- HDR source: the script stops. Ask the user for an SDR export of the film. For a Sloosh-generated video, the asset's access URL is already its SDR preview.
- No audio stream: the script adds a silent track. If the check still shows none, the export did not finish. Run it again and read the error.
- Hook cut off or too small: shorten it to two lines of four words or fewer.
- Logo hard to read: check that the logo file has a transparent background and enough contrast with the dark tile.
