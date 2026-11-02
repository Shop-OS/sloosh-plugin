# Loop effects

16 short looping effects for posts, landing pages and reports, in four groups. Each effect is one clear change that plays, holds and reverses. The descriptions are our own summaries of the motion-graphics-skills effects (MIT). See `THIRD-PARTY-NOTICES.md` in this folder.

## The shared clock

Every effect loops on the same 8 s clock.

| Phase | Time | What happens |
|---|---|---|
| Move | 0.0 to 2.2 s | The one change plays, with a smooth ease in and out. |
| Hold | 2.2 to 6.6 s | The finished state stays on screen. A small detail keeps moving, so the frame never looks frozen. |
| Return | 6.6 to 8.0 s | Everything eases back to the start. |
| Loop | 8.0 s | The last frame matches the first frame exactly. |

Inside the move, "early" means 0 to 0.8 s, "middle" means 0.8 to 1.4 s and "late" means 1.4 to 2.2 s. Use the brand colours for the ground, surface, text and accent. Replace the sample words with the user's real words.

## Interfaces

### 01 Button to player

- Looks like: A small play button stretches into a full video player. The play icon travels to the centre, gains a disc and turns into a pause icon.
- Use when: A "watch the demo" moment on a landing page or in a launch email.
- Timing: Shell grows 0 to 2.2 s. The button label fades in the first quarter. The player contents fade in over the second half. Play turns to pause at about 2.6 s. In the hold, the progress bar creeps and the time counts up.
- Key detail: It is one object that changes shape, not a cross-fade. A faint ghost stays where the button was.
- Made with: saas-product-video

### 02 Search to results

- Looks like: A small search pill widens, a query types itself, and three result cards rise in one after another.
- Use when: Showing what people find in a help centre, shop or content library.
- Timing: Pill widens early. Typing runs from about 0.75 to 1.2 s. Results rise from 1.1 s, each a beat after the last. The return removes the results first.
- Key detail: The pill opens before the typing starts. Each result shows one real number.
- Made with: saas-product-video

### 03 Card to workspace

- Looks like: A small card in a corner opens into the full editor window it belongs to. Its title flies into the window's title bar.
- Use when: A feature launch where one item becomes the whole tool.
- Timing: Shell grows 0 to about 1.4 s. The card text fades in the first fifth. The window contents fade in only after the shell passes halfway.
- Key detail: The title is one shared element that moves. A dashed ghost of the card stays at the start point.
- Made with: saas-product-video

### 04 Tabs to panels

- Looks like: A selection pill slides from one tab to the next and stretches as it moves. The panel below swaps its rows to match.
- Use when: Comparing plans, packages or channels without a wall of text.
- Timing: Pill moves early. Its front edge leads and its back edge follows a beat later. Panel rows swap from about 0.9 s, top row first, each sliding a short way as it fades.
- Key detail: The stretch. A pill that slides at a fixed width looks mechanical.
- Made with: saas-product-video

## Data and lists

### 05 Chart morph

- Looks like: Six bars thin down to hairlines, and a smooth line draws through their tops with a soft fill under it. The last point gets a value tag.
- Use when: One weekly or monthly result in a client report or a results post.
- Timing: Bars thin left to right from 0 s. The line draws from about 0.84 s, and each dot pops as the line reaches it. The value tag lands at about 1.5 s.
- Key detail: The values never change between bars and line. The line draws on; it does not fade in.
- Made with: animated-chart

### 06 Dashboard zoom

- Looks like: Corner brackets lock onto one tile in a dashboard. The rest dims, and the tile grows forward into a large card with a big number and a small trend line.
- Use when: Pulling out the one figure that matters.
- Timing: Brackets snap on in the first 0.9 s. The tile grows from about 0.7 s. The card contents fade in over the second half of the move.
- Key detail: The card grows from the tile's exact position, so it reads as the same object coming closer.
- Made with: animated-chart

### 07 Spring stack

- Looks like: A neat stack of three cards fans out on springs. The top card swings past its resting angle and wobbles back.
- Use when: Three offers, case studies or testimonials.
- Timing: The top card leads. The other two follow at 0.05 s and 0.1 s. The springs settle by about 1.8 s. The return eases back with no spring.
- Key detail: Each card has a different spring, so the top card bounces most and the back card least.
- Made with: saas-product-video

### 08 Magnetic dock

- Looks like: A row of app icons in a dock. Icons near the cursor swell in a smooth curve, and a label floats over the biggest one.
- Use when: Showing a tool set or the integrations a product supports.
- Timing: The cursor glides in during the move. In the hold it sweeps left and right once, and the swell follows it.
- Key detail: Size falls off smoothly with distance from the cursor. The dock re-centres as it widens.
- Made with: saas-product-video

## Type

### 09 Masked type

- Looks like: A big outlined word fills with artwork from the bottom up. An accent line marks the fill edge. A second line rises from behind a clean cut below.
- Use when: Revealing a campaign name, an issue title or a launch headline.
- Timing: The fill rises over the first 1.35 s. The second line rises from about 0.95 s.
- Key detail: The artwork shows only inside the letters. The second line is masked in, not faded in.
- Made with: kinetic-typography

### 10 Elastic type

- Looks like: The letters of one word stretch up from a fixed baseline into a peak. The middle letter is the tallest and narrowest.
- Use when: A title card for an event, a webinar or a podcast.
- Timing: The stretch spreads out from the middle letter. The middle letter peaks at about 1.3 s, and the outer letters finish at 2.2 s. The return relaxes all letters together.
- Key detail: The baseline never moves. Letters change width as well as height, so the word stays one word.
- Made with: kinetic-typography

### 11 Text to layout

- Looks like: One plain headline splits in two and grows into the headline of a full article page. A label, body lines, an image and a quote card arrive around it.
- Use when: Turning a blog headline into a cover, a teaser or a carousel opener.
- Timing: The halves travel from 0 s. The label arrives at about 1.0 s, the image wipes open from about 1.05 s, the body lines draw from about 1.1 s and the quote card rises from about 1.2 s.
- Key detail: The headline is the same text moving, never retyped. Everything else arrives in reading order.
- Made with: kinetic-typography

### 12 Image reveal

- Looks like: Seven dark vertical slats narrow to nothing, left to right, and reveal a full image with a small label.
- Use when: Teasing a product drop or a new photo.
- Timing: Slats open one after another and the last one is gone at about 1.7 s. The label fades in from about 1.05 s.
- Key detail: Each slat has a faint light edge, so it reads as a real shutter.
- Made with: product-reveal

## Systems

### 13 Perspective shift

- Looks like: Three flat layers of a page pull apart in depth and angle towards one vanishing point. Each layer keeps its real content.
- Use when: Explaining the layers of a service, a brand system or a tech stack.
- Timing: Layers separate back to front, each a beat after the last. Guide lines fade in from about 0.9 s. In the hold, the vanishing point drifts slowly, so the stack breathes.
- Key detail: All layers share one vanishing point, so the depth looks correct.
- Made with: saas-product-video

### 14 Glass focus

- Looks like: A glass lens slides down a blurred report. Only the row under the lens is sharp and slightly larger.
- Use when: Making people read one line of a report or a price table.
- Timing: The lens steps to the second row during the move. In the hold it travels to the last row and back.
- Key detail: Text inside the lens is about 1.1 times larger, with faint colour fringes and a highlighted rim, like real glass.
- Made with: saas-product-video

### 15 Flowing paths

- Looks like: Pulses of light leave one source, run along three curved lines to three channels, then merge into one result. Each node rings when a pulse arrives.
- Use when: One piece of content feeding several channels, or a simple funnel.
- Timing: The first pulses leave at 0.25 s, 0.14 s apart, and take about 1 s each. The second leg starts at about 1.75 s. A second wave runs at about 3.6 s to keep the hold alive.
- Key detail: Nodes react on arrival, so cause and effect are visible. The pulse draws the line.
- Made with: animated-chart

### 16 Particle logo

- Looks like: A scatter of dots flies in on gentle arcs with short trails and packs into a crisp logo mark.
- Use when: Closing a video, a reel or a launch post on the brand mark.
- Timing: Dots launch over the first 1.1 s, left side first. The last dots land at 2.2 s. The return sends each dot back to its exact start point.
- Key detail: The dots sit on a grid inside the real shape of the mark, so the final logo is sharp. Every loop is identical.
- Made with: dot-matrix-particles
