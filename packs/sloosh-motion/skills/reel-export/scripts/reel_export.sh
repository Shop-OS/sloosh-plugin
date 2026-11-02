#!/usr/bin/env bash
# reel_export.sh: turn a finished video into a 1080x1920 vertical file that uploads cleanly.
#
#   bash <this skill>/scripts/reel_export.sh <in.mp4> <out.mp4> [--overlay overlay.png] [--bg 0B0B0F] [--fill] [--fps 30]
#
# fit (the default): the video is scaled to fit a box between 32% and 65% of the frame height, centred,
#   on a solid background colour. The top 14%, the bottom 35% and 6% at each side stay free for the
#   platform's buttons, and the hook and logos sit above the video inside the safe zone.
# --fill: the video is scaled to cover the whole frame and cropped at the centre. The sides are lost.
# --overlay: a transparent 1080x1920 PNG (the hook and logo tiles) laid over the whole frame.
#
# The encode: H.264 High, yuv420p, limited (tv) range, BT.709 tags, constant frame rate, faststart.
# When the source has no audio, a silent stereo AAC track is added, because some apps reject a file
# without one. Then check_reel.sh probes the result.
# It downloads and installs nothing. If ffmpeg is missing, it says so and stops.
set -euo pipefail

usage() { sed -n '3,4p' "$0" | sed 's/^# \{0,1\}//'; exit 64; }
[ $# -ge 2 ] || usage
IN=$1; OUT=$2; shift 2
OVERLAY=""; BG="0B0B0F"; MODE="fit"; FPS=30
while [ $# -gt 0 ]; do
    case "$1" in
        --overlay) OVERLAY=${2:?}; shift 2 ;;
        --bg) BG=${2:?}; BG=${BG#\#}; shift 2 ;;
        --fill) MODE="fill"; shift ;;
        --fps) FPS=${2:?}; shift 2 ;;
        *) usage ;;
    esac
done

for tool in ffmpeg ffprobe; do
    if ! command -v "$tool" >/dev/null 2>&1; then
        echo "reel_export.sh: $tool is missing. Install ffmpeg (it includes ffprobe), then run this again." >&2
        exit 2
    fi
done
[ -f "$IN" ] || { echo "reel_export.sh: no such file: $IN" >&2; exit 66; }
[ -z "$OVERLAY" ] || [ -f "$OVERLAY" ] || { echo "reel_export.sh: no such overlay: $OVERLAY" >&2; exit 66; }
case "$BG" in
    [0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]) ;;
    *) echo "reel_export.sh: --bg takes a six-digit hex colour, such as 0B0B0F" >&2; exit 64 ;;
esac

W=1080; H=1920
BOX_TOP=$(( H * 32 / 100 )); BOX_H=$(( H * (65 - 32) / 100 ))

transfer=$(ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer -of default=nw=1:nk=1 "$IN" || true)
case "$transfer" in
    smpte2084|arib-std-b67)
        echo "reel_export.sh: the source is HDR ($transfer). Export an SDR version first; this script does not tone-map." >&2
        exit 65 ;;
esac
has_audio=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$IN" | head -n 1)

inputs=(-i "$IN"); next=1
if [ "$MODE" = "fit" ]; then
    inputs+=(-f lavfi -i "color=c=0x${BG}:s=${W}x${H}:r=${FPS}"); bg_index=$next; next=$((next + 1))
    graph="[0:v]scale=w=${W}:h=${BOX_H}:force_original_aspect_ratio=decrease:force_divisible_by=2,setsar=1[src];"
    graph+="[${bg_index}:v][src]overlay=x=(W-w)/2:y=${BOX_TOP}+(${BOX_H}-h)/2:shortest=1[base];"
else
    graph="[0:v]scale=w=${W}:h=${H}:force_original_aspect_ratio=increase,crop=${W}:${H},setsar=1[base];"
fi
if [ -n "$OVERLAY" ]; then
    inputs+=(-loop 1 -i "$OVERLAY"); ov_index=$next; next=$((next + 1))
    graph+="[${ov_index}:v]scale=${W}:${H},format=rgba[ov];[base][ov]overlay=0:0:shortest=1[comp];"
else
    graph+="[base]null[comp];"
fi
graph+="[comp]fps=${FPS},scale=out_color_matrix=bt709:out_range=tv,format=yuv420p[v]"

audio_map=(-map 0:a:0)
if [ -z "$has_audio" ]; then
    inputs+=(-f lavfi -i "anullsrc=channel_layout=stereo:sample_rate=48000"); audio_map=(-map "${next}:a")
fi

ffmpeg -hide_banner -loglevel error -y "${inputs[@]}" \
    -filter_complex "$graph" -map "[v]" "${audio_map[@]}" \
    -c:v libx264 -preset slow -crf 18 -profile:v high -pix_fmt yuv420p \
    -colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv \
    -c:a aac -b:a 192k -ar 48000 -ac 2 \
    -shortest -movflags +faststart "$OUT"

bash "$(dirname "$0")/check_reel.sh" "$OUT"
