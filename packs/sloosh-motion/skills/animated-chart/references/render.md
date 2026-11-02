# Render, check and export

Read this only when you can run shell commands on the user's own computer. In chat, deliver the HTML file instead (see SKILL.md).

In the commands below, <skill> is the folder of the animated-chart skill.

## 1. Set up once

1. Make a work folder for the chart, for example chart-q3-orders. Copy `assets/chart.html` from the skill folder into it. Edit only the copy.
2. Check what is already installed:

        python3 --version
        ffmpeg -version
        python3 -c "import playwright"

3. Ask the user before you install anything. Install Playwright in a virtual environment, never system-wide, and never with --break-system-packages:

        python3 -m venv .venv
        .venv/bin/pip install playwright
        .venv/bin/python -m playwright install chromium

    The browser download is large. Tell the user before it starts.
4. You need ffmpeg only for the MP4 and the GIF. If it is missing, ask the user how they want to install it (for example Homebrew on a Mac). Stills work without it.

## 2. Look again before you export

Render stills at the moments that show each state:

        .venv/bin/python <skill>/scripts/render_chart.py chart-q3-orders/chart.html --stills 0,1,2,4,7

For a 12 s milestone loop, use --stills 0,2,5,7,9,11.

Open each still and check, with your own eyes, only these:

- Every number on screen matches the user's number exactly, digit by digit, with the same unit, decimals and separators.
- No label, value or title is cut off, overlaps another, or touches the frame edge.
- At 9:16, nothing important sits in the top 14%, the bottom 35% or 6% at each side.
- The headline value is the one in the accent colour.
- Every label and value is readable at phone width.
- "Illustrative data" shows on every still when the data is sample data.
- "Illustrative data" does not show when the user gave real numbers.

Report only the problems you see. Fix them in CONFIG and render the stills again. Keep the earlier version until the fix is better. Do not restyle a chart that has no problem.

## 3. Check the loop seam

The script checks the seam on every run and prints two lines:

- "seek(0) vs seek(D) changed pixels" must be 0.
- "last frame vs first frame mean difference" must be small (the script fails above 2 of 255).

If the check fails, the return does not end on the start state. Make the timing values add up to less than the duration, so the loop rests on the start state before it repeats. Do not hide a seam with a fade to black.

## 4. Export

        .venv/bin/python <skill>/scripts/render_chart.py chart-q3-orders/chart.html --mp4 --gif

- MP4: H.264, yuv420p, 30 fps by default, with +faststart. It plays on LinkedIn, Instagram, X, Slack and in decks.
- GIF: 25 fps, 720 px wide by default (--gif-width 1080 for a sharper, bigger file), a two-pass palette, and it loops forever.
- --out <path> sets the file names. --fps 60 renders a smoother MP4 when the user asks.

After the export, show the user three frames: the start, the hold and the last frame. The last frame must look like the start.

## 5. When something fails

- The plate does not show: the file named in CONFIG.plate is missing from the work folder. Check the file name.
- The page never sets READY: the CONFIG block has a typing error, such as a missing comma or quote. Open the page in a browser and read the console.
- A blank frame: the motion name in CONFIG.motion is wrong. Use one of the names listed in CONFIG.
- A plate image makes the export fail: the plate must sit in the same folder as the page. The script serves that folder over 127.0.0.1.
- The numbers wrap or shrink too much: shorten the label or the title. Do not change the number.
