#!/usr/bin/env bash
# check_reel.sh: probe a vertical export and say PASS or FAIL for each upload rule.
#
#   bash <this skill>/scripts/check_reel.sh <reel.mp4> [--frame mid.jpg]
#
# Pass: video h264, 1080x1920, yuv420p, tv (limited) range, bt709, one aac audio stream, and the moov
# atom at the front of the file (faststart). --frame also writes one frame from the middle of the
# file, to look at at phone size. Exit code 0 when every rule passes, 1 when one fails.
# It downloads and installs nothing.
set -euo pipefail

[ $# -ge 1 ] || { sed -n '3,4p' "$0" | sed 's/^# \{0,1\}//'; exit 64; }
FILE=$1; shift
FRAME=""
if [ "${1:-}" = "--frame" ]; then FRAME=${2:?}; fi
command -v ffprobe >/dev/null 2>&1 || { echo "check_reel.sh: ffprobe is missing. Install ffmpeg, then run this again." >&2; exit 2; }
[ -f "$FILE" ] || { echo "check_reel.sh: no such file: $FILE" >&2; exit 66; }

value() { ffprobe -v error -select_streams "$1" -show_entries "stream=$2" -of default=nw=1:nk=1 "$FILE" | head -n 1; }
failed=0
rule() {
    local name=$1 got=$2 want=$3
    if [ "$got" = "$want" ]; then echo "PASS  $name = $got"; else echo "FAIL  $name = ${got:-none} (want $want)"; failed=1; fi
}

rule "video codec" "$(value v:0 codec_name)" "h264"
rule "size" "$(value v:0 width)x$(value v:0 height)" "1080x1920"
rule "pixel format" "$(value v:0 pix_fmt)" "yuv420p"
rule "colour range" "$(value v:0 color_range)" "tv"
rule "colour space" "$(value v:0 color_space)" "bt709"
rule "audio streams" "$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$FILE" | wc -l | tr -d ' ')" "1"
rule "audio codec" "$(value a:0 codec_name)" "aac"
if head -c 4096 "$FILE" | LC_ALL=C grep -aq moov; then rule "faststart" "yes" "yes"; else rule "faststart" "no" "yes"; fi
echo "INFO  frame rate = $(value v:0 r_frame_rate), duration = $(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$FILE") s"

if [ -n "$FRAME" ]; then
    duration=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$FILE")
    middle=$(awk -v d="$duration" 'BEGIN { printf "%.3f", d / 2 }')
    ffmpeg -hide_banner -loglevel error -y -ss "$middle" -i "$FILE" -frames:v 1 -q:v 3 "$FRAME"
    echo "INFO  middle frame -> $FRAME"
fi

if [ "$failed" -eq 0 ]; then echo "RESULT PASS"; else echo "RESULT FAIL"; fi
exit "$failed"
