# Cinetic techniques, part 2 of 2

This part covers these groups: Logo and end card, Colour and light, Texture and finish, Layout and composition, Pacing and structure, Micro-interactions, Depth and 3D. Part 1 covers the other groups.

Each technique is one named move for a motion film. The entries are condensed and adapted from the cinetic technique library (MIT). See `THIRD-PARTY-NOTICES.md` in this folder.

## How to read an entry

- Looks like: what the viewer sees.
- Use when: the film or moment it suits.
- Avoid when: where it fails.
- Timing: lengths in frames (f) at 60 fps. 60 f is 1 s. px is pixels on a 1920x1080 frame. Scale the pixel values to the real frame size.
- Made with: the sloosh-motion skill that builds it.

The ease names in the timing lines describe the shape of a move:

- ease-out: fast start, gentle stop. Use it for things that arrive.
- ease-in: gentle start, fast end. Use it for things that leave.
- ease-in-out and smooth ease: gentle at both ends.
- soft ease-out and glide ease: a long, light landing.
- UI ease: a short, crisp move for interface parts.
- contact ease: speeds up into a landing, with a small squash on contact.
- camera ease and dolly ease: slow, weighted camera moves.
- whip ease: a very fast move with a hard stop.
- settle ease: the last small move into rest.
- typing ease: an even rhythm for typed characters.
- linear: constant speed.


## Logo and end card (18)

### End card replays the opening

- Looks like: The ending reuses the opening's stage and its mechanic, now carrying the brand, so the film closes on a rhyme the viewer has already learned.
- Use when: Films with a distinctive opening mechanic or stage. The signature move's third use. Loops, where the end hands back to frame 0.
- Avoid when: The opening was generic (replaying it only repeats a template). The reprise would be a frame-for-frame replay that adds nothing. Films under 10 s, where the rhyme has no time to land.
- Timing: Word-roll: 28 f with a 5 f stagger. Mirrored exits keep the entrance's distance and duration. Stage rise: 25 f on ease-out. Final hold: 96-120 f under the push.
- Made with: kinetic-typography

### Lockup keeps building through the hold

- Looks like: Once resolved, the lockup never freezes: the card slowly pushes in (or exhales back), the tracking tightens a touch and the stage dims, so the last 1.5-2 s read as intentional rather than stalled.
- Use when: Every lockup and URL hold, and any card that must sit for more than 48 f.
- Avoid when: A designed freeze of at most 15 f on a silence (then stop everything, the push included). Loops whose hold must end at the frame-0 scale (ease the push back down instead).
- Timing: Hold 90-120 f (1.5-2.0 s, never more than ~150 f). Push 10-20% over the hold on dolly ease. Tracking: 46 f on ease-out. Exhale: 10% over 120 f on ease-out, with a 36 f stage dim. Tail of at least 60 f after the last event, inside the hold.
- Made with: kinetic-typography

### Mark slides aside, name follows

- Looks like: The centred mark glides sideways, shrinking if it was hero-sized, to open its slot, and the name resolves beside it just before the mark stops, so the lockup forms in one gesture.
- Use when: Any end card whose mark is already on screen (it was the story device or the hero) and the name still has to arrive. The default lockup build.
- Avoid when: The mark has not been seen yet (give it its own beat first). The film already used a slide-to-make-room for the product. Long names that would push the slide past ~400 px (stack vertically instead).
- Timing: Slide: 36 f for up to ~250 px (smooth ease peaks ~20 px/f), 60 f for ~350 px (~17 px/f). Motion-blur pass on the mark whenever it moves faster than 12 px/f. Name starts at 0.55-0.6 x D: a block takes 14 f; letters take 16 f each at a 3 f stagger (10 letters inside ~43 f). Tracking: 46 f on ease-out. Lockup resolved by about D + 20 f, then hold 90-120 f.
- Made with: kinetic-typography

### Seed build with stroke draw-on

- Looks like: The mark grows from a small seed while its strokes, stripes or arcs draw on in a quick stagger, so it assembles itself in about half a second and the label rises in beside it.
- Use when: Geometric marks made of a body plus lines, stripes or orbits. A fresh logo reveal after a hard cut to a clean stage. Stings that must show the mark within 0.5 s.
- Avoid when: Solid single-shape marks (there is nothing to draw). Marks with more than ~5 parts (it turns into a slow queue). The mark already exists on screen as the story device.
- Timing: Seed growth: 54 f on ease-out (about 0.2x -> 1; first-frame edge speed ~4 px/f). Parts: 10 f each, 6 f apart (3 parts inside ~28 f). Label glyphs: 2 f apart, 12 f each on ease-out. The whole mark reads within ~0.5 s. Then a 90-120 f hold that pushes from 1.0 to 1.10-1.15 on dolly ease ("lockup keeps building through the hold").
- Made with: kinetic-typography

### Story object becomes the mark

- Looks like: The film's last object (a dot, circle, coin or pill) ends at exactly the mark's screen position and size, and the mark replaces it by a hard cut or an in-place morph, so the logo arrives as the answer to the story.
- Use when: Every film that has a story device: the default way to arrive at the mark, especially as the device's third and final use.
- Avoid when: There is no recurring object (a mark forced out of an unrelated shape reads as a pun). The object's shape and the mark's disagree (a square into a circle needs a morph, never a cut).
- Timing: Coin flip: 22 f on soft ease-out. Two-ended delete: 5 f per letter pair, pill width eased 4 f per step on UI ease. Pill-to-square morph: 30-40 f on ease-in-out. Cut pop: 18 f on ease-out (0.57 -> 1). In-place darkening: 12 f. Then hold ~20 f before the name follows.
- Made with: morph-shapeshift

### The product clears the stage

- Looks like: The last product element leaves (dropping out of frame, accelerating away, or bursting outward toward camera), and the brand, already waiting behind it, starts its reveal on the exact frame it is uncovered.
- Use when: Walkthroughs and feature films whose last shot is the product itself. The opening was a window or card entering, so the reverse bookends it. A crescendo of many screens that should give way to calm.
- Avoid when: The film's last beat is type, not product. A lockup that is already visible would be crossed by the exiting product. A burst with no build-up earlier to justify the energy.
- Timing: Drop: 44 f on smooth ease (~1000 px, peak ~64 px/f, motion-blur pass on). Float-out: 25 f on ease-in (5 -> 22 px/f, scale +33%). Burst: 20 f on ease-in, cut at ~75 px/f. The brand reveal starts within 0-1 f of the clear frame. Mark growth: 68 f on ease-out (edge speed ~17 px/f, no overshoot). Then hold 90-120 f under a 10-15% push ("lockup keeps building through the hold").
- Made with: kinetic-typography

### Accent icon cools to its neutral mark

- Looks like: The app icon pops up from tiny in the film's hot accent, cools through darker tones to its neutral final colours, lifts a little to make room, and the name fades in beneath it.
- Use when: Films whose accent stood for heat, urgency or the problem early on and should cool into the product. App-icon lockups.
- Avoid when: The accent already means something else in the film (one accent, one meaning). Icons whose final colour is the accent itself.
- Timing: Pop: 38 f on ease-out (0.19 -> 0.72 by f6). Colour: 28 f (f6-34) on smooth ease. Lift: 36 f on smooth ease. Label: 15 f. Then hold 90-120 f under a push.
- Made with: kinetic-typography

### Card shrinks to a pill, words close in

- Looks like: The last content card empties and shrinks into a small pill while the tagline words slide in from beyond the frame edges, blurred to sharp, to sit on either side of it; then the logo appears inside the pill.
- Use when: Films that opened with a gap or pill inside a headline (the reverse closes the bookend). Products whose output is a card, post, message or result. A tagline that brackets the brand: [wordL] [mark] [wordR].
- Avoid when: There is no card on screen to collapse. Words too long to fit beside the pill inside the safe width. Light-on-light stages where the pill loses its edge.
- Timing: Content fade: 6 f. Shrink: 30 f on whip ease (card ~1240 -> ~310 px; each word travels ~470 px at a peak of ~58 px/f with the motion-blur pass on, faded until it lands). Logo fade: 14 f, starting 8 f after the pill lands. Then hold 90-120 f under a 10-15% push ("lockup keeps building through the hold").
- Made with: kinetic-typography

### CTA line closes its gaps

- Looks like: The end line starts with exaggerated spaces between its words, which close as the line settles centred; the last word, often the URL, travels farthest, so the eye ends there.
- Use when: A one-line CTA (a sentence plus a URL) after a large type beat. Type-led films whose last beat is a phrase locking together.
- Avoid when: Lines that wrap to two rows. Films that already closed a word gap earlier. Vertical frames where the stretched line would exceed the safe width.
- Timing: tau = 14.6 f: 55% closed in 10 f, 95% by 44 f. The last word starts at no more than 20 px/f and only slows from there. Gaps of ~150/115/80 px close to a normal word space (~0.25 em). URL focus: soft for 8 f, resolved over 14 f.
- Made with: kinetic-typography

### Device keeps time inside the lockup

- Looks like: During the hold, the story device that became part of the mark (a dot, a bar, a stripe) gives one or two small ticks on the beat, so the bookend plays inside the finished lockup instead of after it.
- Use when: Films whose story device became a piece of the mark. Ends that should close the device's loop without ending on the device alone.
- Avoid when: Marks without a separable piece. Very still closes, where any pulse breaks the calm. Loops that need the device to travel back to its frame-0 position instead.
- Timing: 1-2 ticks at least 30 f apart. hitPulse attack 2 f, tau 6 f (gone in ~38 f). Amplitude 10-14% scale or 2-4 px. None in the final 30 f.
- Made with: kinetic-typography

### Mark turns through a key light

- Looks like: The mark (an extruded glyph, a coin or a tile) turns a few degrees in 3D, and its face passes through a light, so a single specular sweep crosses it as it settles face-on.
- Use when: Premium, material or physical brands (finance, hardware, collectibles). 3D marks. A mark that needs one moment of life early in its hold.
- Avoid when: Flat, playful or line marks (a sheen on a stroke looks like a template effect). Films with no other 3D. A second glint anywhere in the film (it reads as a preset).
- Timing: Turn: 40 f on soft ease-out (~4 deg/f peak for 35 deg). Glint: 14 f on smooth ease, starting ~f20. One glint per film.
- Made with: product-reveal

### Name types backwards, group stays centred

- Looks like: The name appears from its last letter to its first while the mark is pushed outward, so the lockup grows out of the mark's edge and stays centred on every frame.
- Use when: Agent, assistant or persona products whose mark is an avatar or a disc. Names of 4-12 characters. A centred lockup that must never jump.
- Avoid when: Two-word names whose second word makes no sense on its own first. Right-to-left scripts (it becomes an ordinary type-on). The headline already used a typewriter.
- Timing: 3.5 f per character (10 characters in 36 f), each fading in over 4 f on UI ease. Each width step eases on a firm spring (no overshoot, ~20 f to settle). The mark travels ~270 px at 7-8 px/f on average. Dot-to-mark darkening takes 12 f. The lockup settles ~20 f after the last character, then holds 90-120 f under a 10-15% push ("lockup keeps building through the hold").
- Made with: kinetic-typography

### Staircase echo shape morph

- Looks like: A large brand shape collapses into a slim pill around the URL, and mid-morph its moving edges show stepped echoes from staggered copies, like a mechanical transformation.
- Use when: Turning a big brand shape or frame into the CTA container. Mechanical, engineered or developer-tool brands. One moment that should feel designed rather than tweened.
- Avoid when: Short moves (under ~150 px the echoes collapse into a smear). Elements that already carry motion blur (double trails). More than once per film.
- Timing: Morph: 48 f on smooth ease, height 983 -> 227 px (edge peak ~22 px/f), width 1878 -> 997 px with a long tail. 7 copies at a 2 f delay each (14 f of echo after the leader stops). The URL stays readable for at least 102 f afterwards, under the card's 10-15% push ("lockup keeps building through the hold").
- Made with: morph-shapeshift

### Stop-motion brand strobe

- Looks like: A burst of hard-cut brand states (the poster, the lockup tiled in ever denser grids, one flood, the boxed wordmark, the glyph) flickers past in under a second as a punchy sign-off.
- Use when: Social stings and launch films with a poster-driven or stop-motion identity. A re-energising coda after a quiet end card. Autoplay loops that need a clean reset point.
- Avoid when: Calm or premium brands. Any film where you cannot keep large light-dark flips under 3 per second (photosensitivity). Any case where it would cut the lockup's hold below 1.5 s.
- Timing: Holds 7, 5, 5, 2, 2, 5, 5, 5, 7 f (43 f, ~0.72 s). Glyph ~2% of H, centred, for at most 30 f. A tick cluster under it that matches the opening's sound.
- Made with: kinetic-typography

### Words part, URL types into the gap

- Looks like: The closing line splits at its middle, both halves slide outward and dim, the URL types letter by letter into the gap, and the flanks fade so the URL holds alone.
- Use when: The closing line is a two-word phrase or pun built around the product, and the CTA is a URL. Minimal, type-only films.
- Avoid when: Lines longer than ~4 words. Films with no typing anywhere else (it would add a new device at the very end). URLs too long for the gap to open within the safe width.
- Timing: Split: 44 f on smooth ease over 250-300 px (peak 20 px/f or less). URL starts at 40% of the split, 4 f per character. Flank fade: 16 f after the last key. URL readable and still for at least 102 f.
- Made with: kinetic-typography

### Dark slam, spin and brighten

- Looks like: After a near-still beat, giant low-contrast arms of the mark sweep over the frame, and the mark rushes back to logo size while spinning into place and brightening to full contrast.
- Use when: The finale of a high-energy film, where the single biggest motion spike follows the single biggest stillness. Radially symmetric or rotational marks (asterisks, petals, rings).
- Avoid when: Marks with an obvious up direction that look wrong at -70 deg (lettermarks). Calm films. Films that already used a spin or a fast zoom-out seam.
- Timing: 66 f. Log rate 0.17/f at f0, 0.10 at f10, 0.04 at f20. Spin 5.2 deg/f at the start, 2.8 deg/f by f10, at rest by f60. Fill 31% of the way to white at f10, 70% at f20, 97% at f40. Preceded by a near-still hold of 60-90 f that ends in a freeze of at most 15 f.
- Made with: kinetic-typography

### Liquid blob resolves into the mark

- Looks like: A dot, or two soft lobes sliding in from the sides, swells into a liquid blob that stretches, splits and snaps into the crisp geometric mark.
- Use when: Products about raw input becoming structure, or about merging and joining. The story device is a dot. Marks made of a few separate primitives.
- Avoid when: Marks with thin strokes or text inside (the threshold eats them). Brands that need crisp precision throughout. Films already using a soft morph seam.
- Timing: 46 f. Parts travel f0-38 on smooth ease at a 2-4 f stagger, and the blob visibly splits ~26 f in. Blur ramp and crisp swap over the last 8 f. Two-lobe version: converge in 40 f on soft ease-out (first frame ~49 px/f, motion-blur pass on), then drift 0.3-0.5 px/f under the line.
- Made with: morph-shapeshift

### Pull out of the mark, undershoot, breathe

- Looks like: The mark arrives so large that only fragments of it fill the frame, collapses to slightly smaller than its final size, then gently breathes up to rest, as if the camera had found it.
- Use when: The mark's first full appearance at the end, or a logo sting. A hit after a short bass gap. Marks with a strong silhouette or inner shapes that read as abstract fragments when huge.
- Avoid when: Thin line marks (at macro scale they become two hairlines crossing the frame). Right after another zoom-through seam. The mark was already shown at hero size earlier (that makes this a replayed reveal).
- Timing: Collapse: N = 43 x ln(s0 / 0.93) frames on soft ease-out (72 f from 5x; log rate about 0.105/f at the start, outer edge under about 80 px/f, under 0.07/f by f10). Breathe: the last 24 f on smooth ease (0.93 -> 1.0), bottoming at 0.94 near f52. Settled by f72. Hold the mark ~20 f before the name follows.
- Made with: kinetic-typography


## Colour and light (25)

### Accent on the newest arrival

- Looks like: Whatever just arrived (a typed character, a snapped word, a generated pill) wears the accent for a moment and then settles to neutral, so a short coloured wake leads the eye.
- Use when: Prompts typing, statements building word by word, AI-generated items appearing, or any build where the newest piece should lead.
- Avoid when: The accent already means something else in the shot (a focus ring or a pressed button), or long paragraphs where the wake becomes noise.
- Timing: Glyph decay takes 12-16 f on linear. A word wave takes 16-20 f per word with an 8-12 f stagger. A step holds 16-20 f per word. An object's tint resolves over 20-40 f on ease-out.
- Made with: sloosh-motion-director

### Drain the stage, keep the hero

- Looks like: Everything around the hero fades and the world drops to dark or bleaches to white, while the hero stays crisp in place, isolating it or closing a section.
- Use when: Search results, a found item, a selected post or row, the moment before a detail view, and the ends of sections or of the film.
- Avoid when: The hero itself must move during the isolation, or the neighbours carry context the viewer still needs.
- Timing: Neighbours fade over 12 f on linear, the world dims over 10 f on ease-in, then hold about 30 f. A white drain takes 6-16 f on linear. Column focus takes 18 f on smooth ease. In the exhale, the stage fades over 36 f and the hero over 30 f starting 8 f later, with a tail of up to 22 f; a push-in dim takes 8 f on ease-in.
- Made with: sloosh-motion-director

### Ink resolve on arrival

- Looks like: Text never simply fades in: it arrives pale (or dim on a dark stage) and darkens or brightens to full ink as it settles.
- Use when: Every headline and caption reveal, especially over textured or busy backgrounds where an opacity fade alone looks washed out.
- Avoid when: Numbers that must read instantly on a cut (land them at full ink), or type that already sits inside a colour-band fill.
- Timing: Colour takes 12-16 f per word on ease-out (a headline-scale darkening may run 40 f). The rise takes 20 f, peaking under 20 px/f. Stagger words 8 f apart (4-10). Connector words go 0 to 0.5 in 2 f, then to 1 over 6-12 f.
- Made with: sloosh-motion-director

### Key-light edge hairline

- Looks like: Every card, device bezel and bevelled shape on a dark stage carries a hairline edge that is bright on the side facing one fixed key light and fades to nothing on the far side, so surfaces separate from black without shadows or halos.
- Use when: Dark UI films with flat cards, panels, device bezels or bevelled brand shapes on near-black, where a drop shadow disappears and a glow is off-limits.
- Avoid when: Light-mode shots, where a white hairline vanishes on paper. Also avoid it on cards that already carry "rim streak on card edges"'s travelling streak, and on layouts so dense that every lit edge turns the frame into wireframe noise.
- Timing: Static styling with no clock of its own: it rides every entrance and move of its surface. Lit-edge alpha is 0.40 at the light corner, 0.10 at 35% of the gradient line and 0 by 65%. The inner top highlight is 0.06. The angle is recomputed every frame as the light angle minus the card's turn. Tilt gain is 0.04 per degree, clamped to 0.6-1.4x. On a tilt resolve (for example rotateX 25 deg to 0 over 68 f on ease-out), the edge brightness settles on the same curve.
- Made with: product-reveal

### Monochrome world, one accent

- Looks like: Everything is black, white and grey, and one saturated accent marks the single element in each shot that carries the meaning.
- Use when: Films that mix photos, 3D, maps and UI, multi-cell layouts, or any shot where several things compete and the eye needs exactly one target.
- Avoid when: The product's own colourful UI is the subject of every shot and greying it would misrepresent it, or the story needs two semantic colours on screen at once.
- Timing: The palette stays the same for the whole film. The accent swaps on the cue frame (a step, 0 f). Focus outlines land 6-10 px wide with their container (26 f, ease-out), thin to 1 px over 12 f on ease-in, then decay to 30% opacity over 24 f on linear.
- Made with: sloosh-motion-director

### Now, was, next tone ladder

- Looks like: Items in a sequence sit on three neutral tones: the one being read is at full ink, the ones already read step down to a mid grey and stay as context, and the ones still to come wait in a dim grey.
- Use when: Captions that build in steps, lists and checklists that grow, slot rollers, status sequences, and flanking words that make way for a new focal word.
- Avoid when: A single statement that lands all at once, or real product UI whose own text colours must stay true. In lens lists, tone should follow distance from the focus line, not reading order.
- Timing: Promotion takes 6 f on UI ease. Demotion takes 10 f on smooth ease, starting with the next item's arrival. Each item holds NOW for at least 24 f. Rollers and ratchets step on the slot frame (0 f). An exit starts at least 8 f after the item reaches WAS. On ink, the tones sit at about 100% (NOW), 40% (WAS) and 24% (NEXT) of the way from the stage to white.
- Made with: sloosh-motion-director

### One-hue light ramp

- Looks like: Every lit thing (rims, rings, stage lifts, the end-card field) comes from adjacent lightness steps of one hue on a single near-black stage.
- Use when: Dark launch films with many light-built shapes (orbs, rings, rims) that need a recognisable look. It also makes a single bright card hit harder.
- Avoid when: Light-mode walkthroughs where the UI's own colours dominate, or films already using the monochrome-plus-accent system (pick one system).
- Timing: The palette stays the same. The end-card field holds 90-120 f with the bands drifting 0.3 px/f on linear.
- Made with: sloosh-motion-director

### Palette shift as context cue

- Looks like: The world's colour changes behind a steady foreground, for a whole act or for one beat, to say 'new context' or 'this is the moment' without words.
- Use when: Act changes without title cards, entering another app's world, or flagging the key moment (the user's prompt, the reveal).
- Avoid when: The foreground is moving at the same time (the cue gets lost), or the film is shorter than two acts.
- Timing: Act switches happen in 0 f on a cut. A neutral process act can be as short as 74 f. A backdrop shift takes 42 f on smooth ease. A hero-beat backdrop holds for up to about 300 f before stepping back.
- Made with: sloosh-motion-director

### Specular sweep

- Looks like: A soft bright band glides once across a settled number, word or logo face, so the element looks locked and made of a real material without moving.
- Use when: A final number, price or logo that has landed and must hold attention through a still beat, or loading and generating labels.
- Avoid when: The element is still moving, or you would need more than one sweep in the shot (it turns into decoration).
- Timing: A one-shot sweep takes 36 f on smooth ease (about 16 px/f mid-sweep, peaking near 26 px/f). A logo glint brightens over 9 f, holds about 11 f and is clear by 36 f. The loop has a 60 f period on linear and is held for up to about 74 f before the result.
- Made with: product-reveal

### Accent hit envelope

- Looks like: On a press or an impact, the element floods with the accent and peaks for one frame with its label inverted, then either bleeds back like decaying light or stays as the new state.
- Use when: Primary-button clicks, send or confirm moments, and contact hits that turn an object into its new state.
- Avoid when: Secondary controls and hovers (save it for the decisive action), or when the accent already floods the ground.
- Timing: Attack 10-12 f, a 1 f peak, then a release of 20-26 f (tau 8): an asymmetric 1:2 envelope. On an impact, the swap takes 1 f, the white flash about 4 f and the squash 8 f.
- Made with: sloosh-motion-director

### Brightness rides the move

- Looks like: A mark or icon takes its brightness from the same progress that drives its scale or depth, so an oversized pass stays a dark shape and the object reaches full brightness exactly as it lands.
- Use when: A logo mark or icon slams in oversized and shrinks to size, an icon lifts out of the UI toward camera, or a field of objects at several depths is pushed through on a dark stage.
- Avoid when: Text (use "ink resolve on arrival", which runs on time), and moves under about 150 px or 1.5x, where the change would not show. On a light stage a giant near-black pass would itself be the flash, so mix toward the paper there.
- Timing: Slam: 66 f on glide ease from s0 = 6-8. The fill follows p^3, so it passes mid-grey only in the second half of the move and reaches full brightness on the landing frame. Lift-out: 24 f of travel on ease-in-out, with the inversion complete at 75% (about 18 f); a mid-grey tile goes from about luma 160 to 248. Depth weights are 0.45 / 0.75 / 1.0 by z, re-read every frame of the push. Motion blur stays on while |delta log s| > 0.1 per frame, and edges stay under 80 px/f.
- Made with: sloosh-motion-director

### Duotone until featured

- Looks like: Screenshots and photos sit in a two-tone grade until their beat. Then full colour opens out from the point of interaction, and the previous item returns to duotone.
- Use when: Grids of integrations, galleries, template pickers, and multi-cell layouts where one item at a time is the subject.
- Avoid when: Only one hero screenshot is on screen (nothing to contrast with), or the UI's colours are its selling point in every frame.
- Timing: The colour iris takes 18 f on ease-out from the interaction point. The return to duotone takes 20 f on smooth ease. A swap on a cut takes 0 f.
- Made with: sloosh-motion-director

### Graphic softens into the stage

- Looks like: A crisp graphic that has just finished its move, such as a wall of bars or a stripe field, loses its edges, widens and keeps drifting until it has become the soft backdrop for the next title, with no cut.
- Use when: After a graphic build (a bar wall, a stripe or tile field, a filled pattern), when the next beat is a title or the end-card mark and needs a backdrop born from what was just on screen.
- Avoid when: The graphic carries data the viewer still needs to read, or it is a UI act where the stage should stay flat. When no graphic build comes before the title, use "living gradient stage" directly.
- Timing: The soften takes 72 f on smooth ease (RackFocus t from 0 to 1, blur 48 px at 1080p). The widen from 1 to 1.5 and the 25% contrast drop run on the same curve. Each element's gradient drifts at 0.3-0.8% per frame on linear and keeps drifting for 60-120 f under the next element. The next foreground enters from frame 36.
- Made with: sloosh-motion-director

### Living gradient stage

- Looks like: Behind static cards the background never freezes: soft pools of colour at the corners breathe in brightness or drift slowly, like light through water.
- Use when: Holds, end cards and statement cards that would otherwise sit still for more than 48 f.
- Avoid when: Busy UI shots where any background motion competes, or films built on a hard flat-stage look. Behind a product window or readable type, where soft pools read as a generic gradient backdrop or as haze; light stages, where they read as smudges. A flat stage with one tonal step is the stronger default.
- Timing: The breathe period is 162 f. Drift loops run 360-660 f, at under 1 px/f. On brand beats the stage rises over 50 f on ease-out (translateY +40% to 0) and drains to flat in 8 f.
- Made with: sloosh-motion-director

### Rim streak on card edges

- Looks like: A bright streak travels along a dark card's border while its edges carry a faint lit rim, separating it from a black stage without a drop shadow.
- Use when: Flat dark UI cards floating on pure black that need depth and separation without tilting or shadows.
- Avoid when: Light-mode UI (use a soft neutral shadow instead), or several cards on screen at once (the streaks compete).
- Timing: The streak crosses one edge in 20-30 f on linear. The rim breathes ±20% over 180 f and stays on for the whole UI act.
- Made with: sloosh-motion-director

### Rising colour wash carrier

- Looks like: A soft single-hue field rises from the bottom edge behind the type, swells and sweeps up across the frame on the change, then recedes off the top, so the foreground swap reads as one move.
- Use when: Changing cards behind continuous colour, leading into an accent-ground claim or the end card, or smoothing a hard cut into a new scene.
- Avoid when: Shots already on an accent ground, or dense UI that the wash would tint. A soft accent haze behind type reads as glow.
- Timing: The rise takes 39 f on ease-out. The swell and wipe take 12 f on ease-in-out (about 28 px/f). The recede takes 90 f on soft ease-out. The pre-cut band takes 16 f on ease-in (about +14 luma levels).
- Made with: sloosh-motion-director

### Shadows tinted by the stage

- Looks like: On a tinted light stage, lifted cards and solid pills cast soft shadows in a dark step of the stage's own hue instead of grey, so depth reads as part of the world's colour rather than dirt on it.
- Use when: Light-mode acts on pale tinted stages, pastel product worlds, and black pills or tiles floating on a tinted field where a grey shadow looks muddy.
- Avoid when: Dark stages, where a coloured shadow becomes a glow. Keep shadows neutral in neutral C.paper films, and skip the tint wherever it would echo the accent and spend its meaning.
- Timing: Static while parked. On a lift (scale 1 to 1.04 over 20-26 f on ease-out), the ambient blur goes from about 56 to 63 px and the alpha from 0.22 to 0.20 on the same curve. On seating, it returns on the seat move's own easing. A palette switch retints the shadows in 0 f, on the cut.
- Made with: sloosh-motion-director

### Tilt-linked sheen

- Looks like: As a card or device tilts in 3D, a faint highlight band slides across its face in step with the angle, so the surface reads as a real material catching a key light.
- Use when: Perspective UI tilt-ups, cards flipping or settling out of 3D, device turns, and logo tiles yawing.
- Avoid when: Flat 2D layouts with no rotation (use the one-shot specular sweep instead).
- Timing: It follows the tilt move: for example, rotateY going from 12° to 0 over 40 f on ease-out moves the band about 30% and parks it. Peak overlay opacity is 0.18 on dark UI and 0.10 on light UI.
- Made with: product-reveal

### Travelling tone band fill

- Looks like: A word, URL or logo mark fills through a band of colour (dark, then accent, then light) that sweeps across it and settles on the final ink.
- Use when: Hero words, the URL card, or a logo mark that should introduce the accent before it fills the frame.
- Avoid when: Small UI text, or type that is still moving (the band and the motion fight).
- Timing: A word sweep takes 32 f on smooth ease (the front peaks at about 25 px/f). A URL takes 42 f, easing into the final ink on ease-out, with the path lagging 8-12 f. A mark wipe takes 8 f on linear, then the tone scrolls for 36 f on smooth ease. Letters stagger 2 f.
- Made with: sloosh-motion-director

### Type solidity arc

- Looks like: The type gains body across the film. Early statements are translucent white that lets the coloured stage show through, and the closing line and lockup are solid, so the payoff reads as more certain than the promise.
- Use when: Brand films and launches on a coloured or living stage, built as question to answer or promise to proof, where the closing line should feel firmer than the opening.
- Avoid when: Neutral black or grey stages, where translucent white just reads as dim grey. Also avoid it for small UI text, in films under about 10 s, and on light stages, where translucent ink loses contrast.
- Timing: Act values are 0.65, 0.85 and 1.0 (opening, middle, end), stepped in 0 f on cuts or act changes. Each arrival's ink resolve (12-16 f on ease-out) lands at the act's value. The end-card line and lockup stay at 1.0 for their whole 90-120 f hold.
- Made with: sloosh-motion-director

### Accent ground for claims only

- Looks like: Narrative shots sit on the neutral stage, other claims flip to the opposite neutral, and the single full-bleed accent ground is saved for the hero claim or the closing card, so colour works as punctuation.
- Use when: Films with a few big statements that must feel louder than the walkthrough around them, and endings that need to feel conclusive.
- Avoid when: The accent fails contrast as a ground for display type, or the film has no distinct claims (a pure UI tour).
- Timing: Grounds swap on cut frames. The radial flood takes 6 f, with tint steps on f0, f2 and f4 decided per frame. The ring stays from f4 to the end of the shot. Claim shots run 60-120 f each.
- Made with: sloosh-motion-director

### Light swell bridge into the hero

- Looks like: Light swells around a small panel until the frame is bright, the film cuts on the brightest frame to the hero card sitting in the same light, and that light slowly exhales back to dark.
- Use when: Releasing a dark section into the hero card or title: the biggest reveal in a dark film.
- Avoid when: Light-mode films, or a second time in the same film.
- Timing: The swell takes 28 f on linear. Cut at the peak, on a downbeat. The exhale takes 86 f on smooth ease (a fade-out never runs on an expo-out).
- Made with: sloosh-motion-director

### Rolling band flood

- Looks like: A light frame fills with the brand colour as soft horizontal bands of it roll upward and grow opaque. The text tints and dissolves into it, and the film arrives on its end-card field without a cut.
- Use when: Closing a light product act into the end card, or returning to the brand world after the last UI beat (a success state, a published page) without a hard cut.
- Avoid when: Dark films, where the flood reads as fog over black. Also avoid it a second time in the same film, and before an end card whose ground is not the flood's hue.
- Timing: 60 f in total. The bands roll one frame height on linear (about 18 px/f at 1080p), and the opacity follows p^2 over the same 60 f. The text tints over 12 f and fades over f12-f40 on smooth ease. Frame mean luma goes from about 250 to 215: a light-to-mid flood, not a polarity flip. The bands then ease to a 0.3 px/f drift for the end card's 90-120 f.
- Made with: sloosh-motion-director

### Single inversion card

- Looks like: In an otherwise dark film, one card cuts to a near-white field with dark type for one second, marking the key promise.
- Use when: A dark film's single most important promise needs to stop the viewer halfway through.
- Avoid when: Light-mode films, films that already alternate dark and light, or when the music has no gap to place it in.
- Timing: Hold for 60 f. The type rises over 18 f on ease-out, starting on f4. The ring breathes with a period of 120 f, ±2%. Place it at about 40% of runtime.
- Made with: sloosh-motion-director

### Theme flip mid-move

- Looks like: In the middle of a camera fly-over, the dark page and stage flash to their light versions, top first, and the motion never pauses.
- Use when: Products with dark and light modes, or as the single dark-to-light act transition of a film.
- Avoid when: The camera is static (the flip turns into a plain crossfade), or the light version would not match the dark one pixel for pixel.
- Timing: 6 f in total, with the mask edge on linear (frame luma goes about 40, 140, 205, 235). The top leads by 2 f. Leave the camera's own easing untouched.
- Made with: sloosh-motion-director


## Texture and finish (20)

### Feathered edge mask

- Looks like: Lists, reels and overflowing lines dissolve into the stage at a soft edge instead of being cut by a hard crop, so content feels endless and the eye stays in the clear middle.
- Use when: Endless-feeling lists, proof reels, logs, chats, card stacks, and type that overflows its line as it is typed.
- Avoid when: Content that must be read right at the container edge; a hard-cropped bento look; as a full-frame vignette (that is lighting, not a mask).
- Timing: Feather 10-15% of the container; list steps 26-40 f on glide ease, or an inertia coast over 30-60 f (friction 0.89) for a proof reel; text under the mask at most 20 px/f while it must read; the mask itself never moves.
- Made with: sloosh-motion-director

### Fog floor

- Looks like: The bottom fifth of the frame lightens toward the stage's brightest tone, as if the UI hovers above a softly lit floor that receding planes can sink into.
- Use when: Light or pastel stages with 3D tilt-backs, lifts and recedes; any film that wants a horizon without drawing a floor.
- Avoid when: Flat, front-on UI with no depth moves; dark stages that already have a light pool; vertical frames where captions sit in the bottom fifth.
- Timing: The floor band is 22% of frame height and fixed to the stage; tilt-backs 30-40 f on ease-in with the fade over their last 12 f.
- Made with: sloosh-motion-director

### Global frame-keyed grain

- Looks like: A fine, even grain sits over the whole film at one strength, breaking banding in soft ramps and blurred plates and giving flat colour fields a tactile surface.
- Use when: Films with large flat or saturated colour fields, soft lighting ramps, blurred photo plates, or a tactile, filmic brand.
- Avoid when: Crisp, clinical UI films where any texture reads as dirt; when the strength would have to change between scenes; as a fix for banding that dithered PNGs should solve.
- Timing: New tile every 2 f; constant strength (sigma ~1-2.3 code levels) for the whole film; no fades and no per-scene changes.
- Made with: dot-matrix-particles

### Gobo-lit studio backdrop

- Looks like: The UI floats over an off-white studio backdrop crossed by huge, very soft diagonal shadows, like window light through leaves, so flat screens feel photographed.
- Use when: Light-stage product films and walkthroughs that need depth and physicality without glass, colour or a 3D set.
- Avoid when: Dark stages; dense UI that fills the frame edge to edge; strictly flat graphic brands.
- Timing: Band drift under 0.5 px/f on sines with 600-900 f periods and spread phases; present in every light shot of the act, unchanged between shots.
- Made with: sloosh-motion-director

### Hairline edge and key shadow

- Looks like: Every floating surface gets a 1 px edge plus one soft key shadow on paper, or a top inner highlight on ink, so flat UI reads as a physical object in a lit space.
- Use when: Any floating card, panel, modal or window, in every format.
- Avoid when: Flush full-bleed UI or gutterless grids whose cells should merge into one board; anything tempting a glass panel or a coloured halo instead.
- Timing: Static finish; shadow and highlight follow the element's z and tilt every frame (lift 14 f on ease-out, drop 10 f on ease-in); highlight alpha changes by at most 0.04 over a tilt.
- Made with: sloosh-motion-director

### Low-luma photo plate

- Looks like: A real photograph sits behind the UI or type, graded almost to black or thrown out of focus, adding context and tonal texture without stealing contrast from the copy.
- Use when: Dark-stage films that need real-world context (a desk, a city, a workspace) or a material, crafted feel behind sparse type or a floating panel.
- Avoid when: Light stages; a busy photo that stays above ~12% mean luma and fights the type; stock imagery unrelated to the product's world; decorative bokeh that names no job.
- Timing: A plate holds its shot (90-420 f) with 0.3x parallax or a 0.5-1.5 px/f drift; montage cuts under a locked foreground every 15-30 f on beats; never a fade on the plate.
- Made with: sloosh-motion-director

### Micro-tick UI sound

- Looks like: (Sound) Typing and UI changes get tiny, dry ticks at or under the music, and once the drums run the UI goes silent, so the picture feels tactile without a loud keyboard sample.
- Use when: Typed prompts, word-by-word builds, cold opens before the beat drops, any UI moment that wants touch without an effect announcing itself.
- Avoid when: Under voiceover syllables; inside a dense drum section; loud keyboard samples; a film whose idea is silent UI over a beat bed throughout.
- Timing: Ticks 2-6 ms long, at least 60 ms (3.6 f) apart, sigma 3.5 ms timing jitter and +-1 dB gain jitter; peaks -23 to -36 dBFS, at or under the bed's RMS; zero UI sounds once the drums enter.
- Made with: sloosh-motion-director

### One grade across mixed media

- Looks like: Desaturated photography, matte grey 3D, flat vector maps and line diagrams cut freely against each other without clashing, because every medium shares one dark value range and only the hero prop carries the accent.
- Use when: Films that must combine photos, renders, maps, diagrams and UI, especially grid or bento layouts with several media on screen at once.
- Avoid when: Light, pastel or colourful brands; single-medium films; hero product photography that must keep its true colour.
- Timing: Swap media inside a shot or cell every 48-90 f, on beats; hard cuts between media need no transition because the value range already matches.
- Made with: sloosh-motion-director

### Speed-gated motion blur

- Looks like: Fast whips, flings and flicked scrolls streak like a real shutter while holds and slow drifts stay pin-sharp, so the eye rests on the readable frames.
- Use when: Any film with whips, flings, drops or flicked scrolls; walkthroughs that travel fast between setups and need every hold razor-sharp.
- Avoid when: Moves that would need more than 80 px/f (redesign as a cut on the beat, a match cut or a mask wipe); readable text moving above 20 px/f; a deliberately stepped on-twos section.
- Timing: Whip 12-20 f on whip ease with a 40-70 px/f peak, the shots either side at 0.3-1.5 px/f; streak length is about 2/3 of the per-frame travel (a 60 px/f card smears ~40 px); a flick is an inertia coast over 50-70 f (friction 0.89), coasting ~8.6 x v0 px and under 0.5 px/f after its settle frames; nothing above 80 px/f.
- Made with: sloosh-motion-director

### Brushed micro-streaks

- Looks like: Fine directional streaks and a satin grain across a hero object's face make it read as machined material instead of flat vector.
- Use when: Hero objects shown big enough for micro detail (coins, cards, devices, extruded marks); hardware and finance brands with a physical metaphor.
- Avoid when: Small or minified objects, where 1 px streaks alias and crawl; soft, friendly brands; flat UI.
- Timing: Constant while the object is at hero scale (at least 30% of frame height); fade it out over 10-14 f on smooth ease before the object shrinks below that.
- Made with: dot-matrix-particles

### Faint dot-matrix silhouette

- Looks like: Behind a claim, a barely visible field of dots forms a meaningful silhouette (a world map, a region, the product's own shape), adding literal context without competing with the type.
- Use when: Claims about reach, coverage, location or scale, and any shot where a silhouette adds literal meaning behind the copy.
- Avoid when: Generic decoration with no meaning; contrast above ~6%, where it starts competing with the copy; small vertical frames where 13 px dots read as noise (scale the pitch up instead).
- Timing: Holds one shot of 80-100 f; scale 1.00 to 1.02 linear across it (well under 1 px/f); arrives and leaves on cuts, no fades.
- Made with: dot-matrix-particles

### Glyph-grid shock pulse

- Looks like: On the film's biggest hit, the dark background flashes a grid of tiny monoline marks that bend outward from the impact like a shockwave, then settles back to a quiet grained field.
- Use when: A digital or developer brand's payoff hit or lockup landing that needs a shockwave without colour or glow.
- Avoid when: Calm films; more than once per film; light stages; behind type that is still arriving.
- Timing: About 12-14 f visible, peaking 4 f after the hit (a hit pulse (4 f up, 3 f down)); 30 px radial push at peak; once per film.
- Made with: dot-matrix-particles

### Halftone shading

- Looks like: A flat hero shape gains volume from a single-colour halftone dot field whose dots swell in the shadow side and shrink toward a slowly moving light.
- Use when: Flat marks, icons or objects that need volume without 3D; technical or print-minded brands; alongside other dot-matrix devices.
- Avoid when: Shapes under ~200 px, where the dots turn to mush; photographic or 3D scenes; busy UI behind the shape.
- Timing: Reveal 36 f (a 24 f diagonal stagger plus 12 f per dot on ease-out); light point drift under 0.5 px/f; holds as long as the shape stays the hero.
- Made with: dot-matrix-particles

### Stepped cadence on twos

- Looks like: One designated layer or section updates only on every second frame, so its motion reads crisp, precise and slightly mechanical against an otherwise smooth 60 fps film.
- Use when: Mechanical, developer or precision brands; a UI section that should feel like a live screen; a short sting that wants a punchy graphic cadence.
- Avoid when: Slow drifts and camera pushes (they judder); moves that would exceed 24 px per step; a few isolated shots in a smooth film, where it reads as dropped frames.
- Timing: Steps every 2 f (30 Hz in a 60 fps file); moves of 60-150 px over 24-40 f on glide ease or a firm spring evaluated at f2, peaking at or under 24 px per step; at least one full shot or act long.
- Made with: sloosh-motion-director

### Stepped mosaic resolve

- Looks like: An image or screen arrives as coarse grey blocks that halve in size every two frames until the real picture snaps in, sharp and in full colour.
- Use when: Revealing an image, avatar, map or screen in a digital or tech brand; the resolve after a locked state; a beat-synced reveal.
- Avoid when: Text-heavy screens (half-resolved text looks broken); calm, quiet brands; more than twice per film.
- Timing: 48, 24, 12, 6, 3, then 1 px over 10-12 f (2 f per size); saturation and brightness over 12 f on smooth ease; an optional 4-6 f hold at 48 px so the resolve starts on a beat.
- Made with: dot-matrix-particles

### Stipple only in lit ramps

- Looks like: A visible dithered stipple lives only inside lit edges and light falloffs, while the flat stage around them stays perfectly clean.
- Use when: Dark films with lit edges, light pools or soft falloffs that risk banding, where a global grain would dirty a deliberately clean stage.
- Avoid when: Films already running global grain (double texture); light stages; hard-edged flat design with no ramps.
- Timing: Static texture that moves rigidly with its ramp; high-pass sigma about 1.9 code levels in the brightest ramps, 0.5-0.9 in faint falloffs, 0.0 on the flat stage.
- Made with: dot-matrix-particles

### Intersecting ring field

- Looks like: Above and below a centred band of type, families of huge overlapping ellipse outlines rotate slowly in opposite directions and whip on every copy swap, giving the words an ownable abstract environment.
- Use when: Type-led launch cards or a statement sequence on a dark stage that needs a signature environment and a motivated way to change copy without cuts.
- Avoid when: UI demos, where it competes with the product; light stages, where 2 px rings vanish; more than ~4 s of pure ambience.
- Timing: Drift 0.2 degrees/f between swaps; whip +12-16 degrees over 12 f on smooth ease (peak ~3 degrees/f, ~50 px/f at the outer rim); copy swaps every 60-120 f on the whip's peak frame.
- Made with: sloosh-motion-director

### Locked-state mosaic

- Looks like: Withheld content shows as pixelated, desaturated, darkened art with a lock glyph and thin light lines sliding across it, until an unlock snaps it to clean full-tone art.
- Use when: Premium, gated or upcoming features; a reveal sequence where concealment builds desire; access or unlock stories.
- Avoid when: Products with nothing gated; text content (pixelated text reads as broken); more than one reveal device in the same act.
- Timing: Locked state 54-108 f (the strokes keep moving, so nothing is static); unlock = 12 f brighten, 4 f dip, swap, 10 f settle; repeated unlocks 30-45 f apart, each ~25% quicker.
- Made with: dot-matrix-particles

### Scanline transmutation

- Looks like: A bright bar sweeps down a hero object: above the bar the object has already become its digital form, a dot-matrix disc with a crisp rim, while below it the original solid object remains.
- Use when: One hero transformation per film: an object becoming its private, digital, encrypted or connected form; the moment the concept turns.
- Avoid when: More than once per film; ordinary UI state changes; objects under ~25% of frame height, where the dot pitch cannot read.
- Timing: 34 f in all: 11 f fast (20-30 px/f at 1080p), a 6 f near-hold at ~4-6 px/f on the symbol, 17 f on glide ease to rest; bar 36-40 px; the transformed object then holds 24-40 f with a drift under 1 px/f.
- Made with: glitch-fx

### Wireframe-to-product scan

- Looks like: A thin accent line sweeps across a UI card: ahead of it the card is still a wireframe of outlines and skeleton bars, behind it the finished product is already there.
- Use when: Idea-to-product, design-to-code, generation or build stories; the first appearance of the hero UI.
- Avoid when: More than once per film; UI too sparse to read as a wireframe; a film that already uses another scan device such as scanline transmutation.
- Timing: Sweep 40-48 f on smooth ease across a 600-900 px card (edge peak ~40-58 px/f; the UI itself never moves); line fade 10 f; the finished card then holds at least 30 f under a 0.5-1.5 px/f camera drift.
- Made with: sloosh-motion-director


## Layout and composition (16)

### Caption in the subject's negative space

- Looks like: Each camera move ends on a pose where the product covers about two-thirds of the frame and leaves a clean band of empty stage, and the caption builds inside that band.
- Use when: Single-take product walkthroughs and 3D UI slabs where each feature gets one pose and one caption; any shot where text laid over the UI would fight it.
- Avoid when: The subject must stay full-frame to be legible (caption above or below it instead), or a 9:16 frame, where the band should be top or bottom only.
- Timing: Caption starts at 75% of the move, or within 6 f of landing; Words stagger 8 f, dur 26 f. Block exit 12-16 f on smooth ease, ending as the next move starts. Camera moves on camera ease.
- Made with: kinetic-typography

### Live cause-and-effect split

- Looks like: Two panels share the frame side by side, the cause on one side (a chat, a list, an input) and the effect on the other (a generated page, a photo, a result), both live, while the camera creeps in.
- Use when: Showing that an input produces an output (prompt to page, list to detail, setting to preview), where seeing both at once is the point.
- Avoid when: Phone-first or vertical films (stack the two instead), or when either side's text would drop under 24 px at 1080p.
- Timing: Hold 180-240 f. Creep about +0.017%/f (+4% over 4 s) on linear. Swaps every 54 f with a 6 f settle. Exit pan 40 f on ease-in, cut at the peak (at most 60 px/f).
- Made with: kinetic-typography

### One huge centred subject

- Looks like: Every frame has exactly one subject, centred and large: a single line of type, or one UI card scaled to most of the frame width and often bleeding past the edges, with everything else dimmed.
- Use when: Fast, phone-first films; walkthroughs where the viewer must never search for the subject; the default framing between more designed compositions.
- Avoid when: Comparison or cause-and-effect beats that need two things on screen at once (use a split), or bento-style loops.
- Timing: Holds of 30-72 f per hero. Cards at 85-100% of frame width or bleeding past it, header bars up to full width, tables at least 80%; type 5-8% of frame height per line. Dims and rack focus 12-20 f on smooth ease.
- Made with: kinetic-typography

### Subtract to the one

- Looks like: A busy board loses its elements one by one until a single survivor remains, which either re-centres or stays exactly where it was while the world around it dims.
- Use when: Isolating the deliverable, the found result or the keyword before entering its world; turning a crowded problem state into one focus.
- Avoid when: The removed elements are themselves the message (show them first), or the survivor is small enough to float lost in an empty frame (push in after isolating it).
- Timing: Staccato: a removal every 5-7 f; last survivor held 17 f. Graded: neighbours fade over 12 f, world dims over 10 f, hold 30 f. Word exits 4 f each, 3 f apart (a line clears in about 12 f). Re-centre 20-40 f on a soft spring.
- Made with: kinetic-typography

### Vertical clear-band stack

- Looks like: In a 9:16 frame, the caption and the subject stack vertically inside the band the feed leaves clear, with their combined mass centred on that band rather than on the frame, and nothing important under the bottom caption zone or the right action rail.
- Use when: Any vertical cut-down or vertical-first film for feeds.
- Avoid when: 16:9 masters (use a side-by-side composition there), or full-bleed moments where one giant word fills the screen anyway.
- Timing: Subject rises 120 px over 40 f on glide ease; caption Words (stagger 8 f, dur 26 f) start 8 f after the subject; exits 16 f on ease-in; hold 60-90 f per stack.
- Made with: kinetic-typography

### Words part for an inserted object

- Looks like: Inside a finished line, the words slide apart to open a gap and an object pops into it (an icon, a photo, a token, or a caret that grows into a container), so the sentence becomes a frame for the object.
- Use when: Making a sentence about the object literally contain it (a product photo in a claim, a lock icon beside 'private', a prompt box between two words); morphing a headline into the first UI element of the next scene.
- Avoid when: Long lines whose parted words would leave the frame unintentionally, or an object that needs more room than a word gap can give (use a push-aside or a cut).
- Timing: Gap opens over 16 f on glide ease, which keeps a 200 px gap under 20 px/f per side. Object pop 6 f on a small quick spring. Hold 14-60 f. Exit: words 16 f on ease-in, object scale-up 8-20 f into the cut. Caret variant: grow 6 f, hold 8 f, thicken 14 f, widen 24-62 f.
- Made with: kinetic-typography

### Centre object with mirrored flanks

- Looks like: A narrow centre object (a phone-width window, a pill, a big number) holds the middle while matching elements sit on both sides: the two halves of a caption, or two mirrored columns of items.
- Use when: A narrow device or pill leaves empty sides; a stat that needs visible volume on either side; inputs and outputs around one product; the tagline that frames a logo pill before the end.
- Avoid when: Wide centre subjects (each flank gets squeezed under 20% of the frame), or vertical formats (stack above and below instead).
- Timing: Caption halves 20-42 f apart; hold about 60 f. Column rows 6 f apart (five rows in about 30 f); outward drift 3.8, then 0.7, then 1.8 px/f over about 120 f. Centre numeral rises 50 px over 38 f.
- Made with: kinetic-typography

### Headline over a ghost of the UI

- Looks like: A headline inks in from light grey to near-black while a faint copy of the product interface sits behind it, then the UI resolves to full strength as the headline leaves.
- Use when: Setting up a demo during a statement, so the move into the product needs no transition; a claim that names the product area about to be shown.
- Avoid when: High-contrast UIs whose ghost would muddy the type, or UI text at the same scale as the headline sitting directly behind it.
- Timing: Ink resolve 40 f. Ghost UI at 10-20% opacity under the headline; it resolves to 100% over 60 f, starting when the headline's exit begins.
- Made with: kinetic-typography

### Hero icon becomes the inline glyph

- Looks like: The centred hero icon shrinks and travels into a slot at the start of, or inside, a sentence, and the words of the claim spill out of it, so the icon becomes a word.
- Use when: Bridging from a hero object to a claim about it: an icon becoming the bullet of its benefit, a mark becoming the subject of a sentence, a feature glyph leading a metric line.
- Avoid when: Detailed icons that will not read at cap height (50-90 px), or sentences long enough to wrap.
- Timing: Icon travel 22-30 f on smooth ease, scaling to about 0.42 (cap height). Words at icon landing + 2, + 6 and + 10 f, each a 14 f slide of 24 px with a 12 f colour resolve. Residual drift 0.5-1 px/f.
- Made with: kinetic-typography

### Hub-and-spoke concept diagram

- Looks like: A central product tile sits inside two thin concentric rings with a short streak orbiting it, inputs on the left and outputs on the right, under a centred one-line headline.
- Use when: Explaining a many-inputs, many-outputs product (integrations, sources to results) in one still composition without narration; the concept beat before a walkthrough.
- Avoid when: More than five chips per side, or when the real product UI can show the same thing directly.
- Timing: Rows 6 f apart, 12 f each; connectors 16 f on ease-out; streak 1.5 deg/f (a quarter turn per second) on linear. Hold 120-200 f; the rotation keeps it moving.
- Made with: kinetic-typography

### Icon-led ragged word stack

- Looks like: A short lead word is followed by three or four keywords on separate lines, each with a small line icon, set at staggered x positions so the list has a rag instead of bullets.
- Use when: Listing three or four abstract capabilities, platforms or audiences that would otherwise be a bullet list; a 'works across X, Y, Z' beat.
- Avoid when: More than four items, items longer than two words, or icons that decorate rather than mean something (then drop them and keep the rag).
- Timing: Rows 8-12 f apart (10 by default), 22 f each on ease-out, 12 px rise. Hold the full stack 60-80 f with the drift, then exit in reading order 4 f apart.
- Made with: kinetic-typography

### Mark set as a word

- Looks like: A logo, partner mark or icon sits inside a sentence on the baseline at cap height, as if it were a word, appearing with its own delayed fade or swapping with a word in the same slot.
- Use when: Co-branding inside a claim, naming a platform or integration without a separate logo slate, or turning a generic noun into the product name in place.
- Avoid when: Marks with fine detail or wide aspect ratios that cannot read at cap height, or the film's own final lockup, which appears once, at the end, on its own.
- Timing: Mark appears about 17 f after the first word with a 4-6 f fade. Slot swap 8 f with 8 px travel. The line then drifts at 0.5 px/f.
- Made with: kinetic-typography

### Opposite-corner caption relay

- Looks like: One caption fades out of one upper corner while the next starts building in the mirrored corner, so the eye travels across a locked frame and that travel is the motion.
- Use when: Two consecutive beats over one held product shot with no camera move or cut; alternating claims about one screen.
- Avoid when: Captions longer than a short line (the eye cannot finish A while B starts), or as the default for every caption change; repeated more than twice it reads as a device.
- Timing: A fades over 28 f on smooth ease; B starts 10 f after A's exit begins; 18 f of overlap. Each caption stays readable for at least 48-60 f.
- Made with: kinetic-typography

### Arc carousel

- Looks like: A row of cards rides a wide smile-shaped arc across the lower part of the frame, each tilted tangent to the curve, rushing in, coasting slowly through the middle and speeding out.
- Use when: Showing an inventory or collection (templates, cards, products, integrations) where several items should read at once and the set should feel endless; a looping feature beat.
- Avoid when: Items with dense text that must be read at the edges (tilted edge cards are glanced at, not read), or vertical frames where the arc gets too tight.
- Timing: 90 f per pass. Card speed 58 px/f on entry, about 8 px/f through the middle, 39 px/f on exit (angular 1.9, then 0.25, then 1.3 deg/f). Spacing 11 deg, about 336 px of arc, for cards 260-300 px wide.
- Made with: kinetic-typography

### Bento cell takes over the frame

- Looks like: In a flush four-cell grid, one cell grows to fill the whole frame while its siblings are pushed off the edges, still playing as they go, turning a breadth overview into one focused shot without a cut.
- Use when: A loop or launch that opens on four-up breadth and then dives into one feature; returning to the overview between features.
- Avoid when: A chosen cell whose scene was not composed for full frame (it will look sparse), or more than twice per film.
- Timing: 64 f on smooth ease; content at the far frame edge peaks around 60 px/f (the far corner about 68 px/f), with motion blur. Cells keep playing throughout. Follow with at least 90 f of the full-frame scene. To return to the overview, run it in reverse (scale 2 to 1, 64 f, smooth ease).
- Made with: kinetic-typography

### Swarm, cluster and burst reveal

- Looks like: About twenty cards or screenshots fly in from every edge, swirl, pack into a dense overlapping cluster that slowly swells, then blow outward past the camera to uncover a hero object that was waiting behind them.
- Use when: A crescendo near the end that proves breadth (many apps, templates, outputs) and clears the stage for the lockup or a hero stat; the film's single biggest motion spike.
- Avoid when: Calm or minimal films, more than once per film, or when the cards' content has to be read (nothing in the swarm is legible). If it reveals the lockup, the lockup still holds only 1.5-2.0 s.
- Timing: Fly-in 28-40 f, entering at 56 px/f and decaying. Swirl 60 f. Converge 32 f (cluster width 1474 to 1076 px at 1080p). Build 104 f at +0.2%/f, linear. Burst 24 f, peaking at 72 px/f with motion blur; the last cards clear by f24, then hold the hero. Shorter scatter-only version: cards leave on ease-in over 22 f, with travel scaled by (1 + 0.1 * index).
- Made with: dot-matrix-particles


## Pacing and structure (23)

### Breath envelope per card

- Looks like: Every card arrives fast and decelerates, keeps moving gently through its hold, then accelerates away and is cut on its fastest frame.
- Use when: Statement cards, kinetic type and feature cards in a fast-cut film where nothing should ever look frozen.
- Avoid when: Dense UI that needs a dead-still read (lock the camera instead), and the final lockup hold.
- Timing: Arrival 20-50 f ease-out (default 36, peak about 15 px/f). Hold = 36 f + 6 f per word at 0.4-1 px/f or +0.06%/f scale; the drift rate is never 0 for more than 6 f. Exit 14-20 f ease-in, reaching 19-39 px/f on the cut frame. Example U: 14 then 3 then 39 px/f across 56 f. No near-still run over about 22 f before the end card.
- Made with: sloosh-motion-director

### Camera locks, the interface performs

- Looks like: After each move the camera stops dead, and for a 1-4 s read only the caption, the cursor and one micro-interaction move.
- Use when: Dense product UI that must be read, walkthroughs, and films where every move should feel deliberate because it contrasts with stillness.
- Avoid when: Kinetic type or fast montages where a dead camera reads as a stalled player, or holds with nothing in the UI to animate.
- Timing: Holds 60-240 f (median about 150 f) at exactly 0 px/f; an in-frame event at least every 40 f; moves between holds 56-108 f camera ease; caption exit 26-28 f smooth ease, ending 0-56 f before the next move.
- Made with: sloosh-motion-director

### Each repeat runs faster

- Looks like: The first instance of a repeated action plays at full length, the second runs about 40% quicker, and later ones are implied or ratchet faster still.
- Use when: Repeated unlocks, card reveals, list items, word deletes, and captions that recur across a film.
- Avoid when: Items that each need a full read, and the first instance, which must teach the pattern at full length.
- Timing: Second instance at 0.6x length (for example a rise of 12 f becomes 7 f), starting about 46 f after the first. Ratchet gaps 26, 14, 12, 8, 8, 4, 4 f. Caption word stagger falling from 24 f on the title to 5 f on late captions.
- Made with: sloosh-motion-director

### Fixed-length ask, variable answer

- Looks like: A demo repeats a fixed-length ask beat followed by a result whose length varies with its importance, so the rhythm teaches itself and the variations prevent fatigue.
- Use when: Prompt-to-result products, feature tours with one repeated action, and walkthroughs of 3-6 capabilities.
- Avoid when: Fewer than 3 instances (there is no pattern to learn), and stings.
- Timing: Ask beat 180-188 f (6 beats); results 138-234 f, the hero result about 490 f; 4-5 cycles; close-up insert from cycle 3.
- Made with: sloosh-motion-director

### Hard stop into a silent sign-off

- Looks like: Tension rises under the back half, the music stops dead on the cut to the last line or URL, the picture all but freezes, and the lockup arrives at full speed under a single low stinger.
- Use when: The last 4-6 s of launch films and feature reels for fast, confident brands.
- Avoid when: Calm brands, where a sub stinger reads as trailer noise (end on one soft chord instead), and loops with no ending.
- Timing: Riser 180-300 f ending where the silence begins; music falls to silence within 2 f; URL readable for at least 102 f with drift of at most 0.03%/f; designed freeze 12-15 f on true silence; logo move 30-68 f ease-out from full speed; stinger on the wordmark's resolve frame; lockup hold 90-120 f; tail of at least 60 f.
- Made with: sloosh-motion-director

### Image act, then type act

- Looks like: A short spot splits in half: the first half is pure imagery with no words at all, the second is pure type with no imagery.
- Use when: 6-12 s spots and social cut-downs with one claim and a strong visual metaphor, especially when watched on mute.
- Avoid when: Product walkthroughs that need captions on the UI, and films over 20 s.
- Timing: Total 480-600 f. Act 1: 3 shots of 70-90 f. Act 2: claim 70-80 f, headline 60-70 f, CTA 60 f, then lockup 90-110 f.
- Made with: sloosh-motion-director

### Light and dark as chapters

- Looks like: Acts are planned by stage polarity, dark for the abstract or problem beats and light for the product, so chapter changes read without any title cards.
- Use when: Films with distinct problem/solution or prompt/result halves, and 20-60 s pieces that need a rhythm at the scale of whole acts.
- Avoid when: Very short stings, and brands locked to a single stage colour.
- Timing: 3-5 flips per film, each on beat n; iris 20 f ease-in-out; bleach 26 f smooth ease; theme flip during a move 6 f; wash rise 50 f ease-out, drain 8 f ease-in.
- Made with: sloosh-motion-director

### Long-tailed beat lengths

- Looks like: Beat lengths follow a long tail instead of an even grid: most beats sit near one median length, a few connective beats snap past at a third of it, and one or two hero beats run about three times as long, so the film never settles into a slideshow rhythm.
- Use when: Launch films and walkthroughs of 15 s or more with eight or more beats, any cut list that came out evenly spaced, and deciding where the hero feature gets its time.
- Avoid when: Polyrhythm loops and fixed-length ask cycles, where equal length is the point; stings under about 8 s, which have too few beats for a distribution; accelerando runs, which set their own length ratios.
- Timing: M = 60-72 f. Connective beats 24-36 f (never under 24 f); core 0.75-1.33x M; long 1.5-2x M; hero 2.5-3x M, at most 180 f and at most 2 per film; coefficient of variation 0.4-0.8. Example 28.75 s cut at 120 BPM: 75, 60, 30, 75, 120, 45, 60, 75, 30, 75, 60, 45, 105, 60, 30, 180, 75, 45, 30, 180, 90 and 60 f, then a 120 f lockup (M 60, max/M 3.0, CV 0.56).
- Made with: sloosh-motion-director

### Loop seam hidden at a motion peak

- Looks like: A loop wraps around on the fastest frame of a whip or push, so the last frame flows into the first with no visible restart.
- Use when: Autoplay loops for social, landing pages and product pages.
- Avoid when: Pieces that end on a lockup (it appears once, at the end), and loops whose first frame must work as a readable poster.
- Timing: L = whole bars (240, 480 or 960 f); seam move at 20-40 px/f with true motion blur; entry ease-out 30-50 f, exit ease-in 12-24 f; seam on the downbeat.
- Made with: sloosh-motion-director

### Machine on the grid, hands off it

- Looks like: Work the product does (rows inserting, items stacking, text streaming) ticks on a strict metronome, while what a person does (moving the cursor, flipping toggles, clicking) arrives on uneven, deliberating gaps, so the viewer can feel who is acting.
- Use when: Product demos where a person gives an instruction and the product or an agent responds, walkthroughs that mix input with generated output, and any sequence where automation should feel tireless next to a human.
- Avoid when: Pure type films or brand stings with no user in the story; polyrhythm grids, which run their own clocks; musical montages where every event must land on the beat.
- Timing: SYS: one event every 15 f (an 8th at 120 BPM), or every 7-8 f (16ths) in bursts; identical 12 f UI ease reveals; streams at 25-40 characters per second. USER: gaps such as 4, 15 and 18 f, or 10, 26 and 14 f; cursor travel max(14, D/20) f on glide ease, peak under 60 px/f, with motion blur above 12 px/f; dwell 6-18 f; press 12 f via pressAt; the decisive press on the beat ±1 f.
- Made with: sloosh-motion-director

### Music hole, then slam on the cut

- Looks like: The low end, or the whole bed, vanishes for a fraction of a second under a key statement, then slams back on the exact frame of a picture event.
- Use when: Statement cards, key claims and the hero cut in any film with a groove bed.
- Avoid when: Calm brands with no drums, or more than one hole every 8 bars, where it stops working as an accent.
- Timing: Hole 12-24 f for one statement or 2-4 beats for a line; the bed drops 10-20 dB or the sub goes fully silent; re-entry on a downbeat within ±1 f of a picture event; 2-4 holes per minute.
- Made with: sloosh-motion-director

### One screen direction per act

- Looks like: Each act owns one direction of travel, so every entrance, exit, drift and camera ramp in it runs the same way, and the direction turns only at an act seam, where the turn itself marks the new chapter.
- Use when: Films built from hard cuts with velocity handoffs, two-act spots (imagery, then type), runs of statements (an upward feed), and vertical films with a rising vector.
- Avoid when: Oners and single camera journeys, where the layout of the surface sets the direction; films whose motion is mostly radial zooms; multi-cell grids; a film with no act change, which should keep one vector throughout.
- Timing: 2-4 vectors per film, one per act, each turn on beat n at an act seam. Entrance offsets 8-15% of frame width (150-290 px at 1080p), braking on ease-out over 30-50 f; hold drift 0.3-1 px/f downstream; exit ramps 18-24 f on ease-in, reaching 17-38 px/f; counter-motion above 2 px/f lasts at most 6 f and only in settle tails.
- Made with: sloosh-motion-director

### Phrase chunks on the beat

- Looks like: A line arrives in two or three chunks split by meaning, each landing exactly on the next beat, so the reading rhythm is performed by the track.
- Use when: Statement lines over music with a clear pulse, launch openers, and 3-7 word claims.
- Avoid when: No music or a free-time score, and sentences of more than 8 words.
- Timing: One beat per chunk (30 f at 120 BPM); 4 f word stagger inside a chunk; masked rise 6-8 f ease-out, stretched to 10-12 f for words over 60 px tall so legible glyphs stay under 20 px/f; calm variant 20-22 f per word.
- Made with: sloosh-motion-director

### Silent UI over a steady bed

- Looks like: In dense, fast-changing sequences the interface makes no sound of its own, with no per-key or per-event effects, and a steady groove carries all the energy.
- Use when: Loops, grids, speed-typed prompts, counters, and any sequence with more than 3 events per second.
- Avoid when: Sparse, calm films where each event deserves its own tuned sound, and the payoff moment.
- Timing: No per-character sounds; at most 1 tick per word; 6-8 accent ticks per 45 s; ticks 5-15 ms attack, 40-80 ms decay, 18-24 dB under the bed.
- Made with: sloosh-motion-director

### Spectacle, diagram, walkthrough, sign-off

- Looks like: A launch film in four sequences: a short spectacle open, one concept diagram, a long real-product walkthrough and a brief brand close.
- Use when: 30-60 s launch films that have to earn attention, explain an idea and then prove it in the product.
- Avoid when: Spots under 15 s (use the image-then-type plan instead) and products with nothing to diagram.
- Timing: Shares 19/14/58/9% (at 30 s: about 342/252/1044/162 f). Walkthrough shot median 75-100 f; wides 90-180 f, close-ups 76-154 f at 4-4.5x. Lockup hold 90-120 f inside the close.
- Made with: sloosh-motion-director

### Accelerando into the climax

- Looks like: Shot lengths shrink step by step toward the climax, then one designed freeze on silence resets the clock just before the payoff lands.
- Use when: The run-up to a reveal, a collage burst or the lockup in launch films and stings.
- Avoid when: Walkthroughs where each shot carries UI that must be read, and films already cutting under 60 f per shot throughout.
- Timing: Shots 120, 90, 60, 45, 30, 30 f (about x0.7 each, minimum 24 f without text); exit ramps on the last 40% of each shot, ease-in; freeze 12-15 f on true silence; climax on the next downbeat.
- Made with: sloosh-motion-director

### Empty ground after a cut

- Looks like: Right after some hard cuts the new stage shows for two empty frames before its type appears, a tiny palate cleanser that makes the cut read crisply without any flash.
- Use when: Type-led films on white or flat stages with many statement cuts.
- Avoid when: Velocity-matched cuts, where the gap kills the momentum, and frame 0.
- Timing: 2 empty frames at 60 fps; the incoming card starts at cut + 2 on its usual entrance; on at most a third of the cuts.
- Made with: sloosh-motion-director

### The one long hold

- Looks like: In a film that otherwise never stops, a single key claim sits nearly still for over a second, which tells the viewer it is the line to remember.
- Use when: The single claim or number the film exists to say, in a launch film or short spot that is relentless everywhere else.
- Avoid when: Films already built on long holds, where it stops reading as special, or when two lines compete for the slot.
- Timing: Settle 20-36 f; hold 60-90 f at under 0.3 px/f; exit creep +6% over 18 f ease-in. Every other near-still run stays at or under 30 f.
- Made with: sloosh-motion-director

### One camera journey across one surface

- Looks like: Every product state lives on one large surface and the film is a single camera path between poses; scene changes are pushes, pulls, orbits, whips and the interface's own window actions.
- Use when: Walkthroughs of a single app, features where spatial orientation matters, and calm, premium product films.
- Avoid when: Multi-app or abstract stories, and films under 10 s.
- Timing: 0 cuts; about 3 moves per 10 s; moves 42-108 f camera ease; holds 18-252 f (median setup about 170 f); window actions 8-52 f.
- Made with: sloosh-motion-director

### Oner through a morph chain

- Looks like: The whole film plays as one continuous shot, every new scene growing out of an object already on screen, with no hard cuts at all.
- Use when: Multi-step workflows and multi-app stories, or any film where the viewer should never have to re-orient.
- Avoid when: Films that use polarity cuts as punctuation, or footage-based shots that cannot share elements.
- Timing: About 3.6 morphs per 10 s; beats median 72-144 f, minimum 23-34 f, maximum 194-410 f; each morph 5 f ease-in plus 10-16 f ease-out; world swap 10-14 f under the held element.
- Made with: morph-shapeshift

### Score arranged to the acts

- Looks like: The music's arrangement tells the story's structure: a sparse filtered intro, the drop on the first product frame, a breakdown for the calm act, a return for the proof, a final hit on the climax and the logo in silence.
- Use when: 20-60 s launch films with clear acts, when the score is generated or its stems can be edited.
- Avoid when: A supplied track with a fixed structure (retime the picture to its bars instead), and 3-6 s stings.
- Timing: Intro 120-160 f; the drop and its cut within 1 f (or the picture leads by up to 8 f); cuts within ±4 f of onsets; breakdown 2-4 bars; the final hit's tail reaches -60 dB in about 35-55 f.
- Made with: sloosh-motion-director

### Silence as the default bed

- Looks like: There is no running music: most of the film is true silence, sound appears only on decisive events, one low swell carries the single reveal act, and the audio cuts dead on the frame a key value lands.
- Use when: Short stings and feature spots under about 15 s, calm or premium tones, number and unlock reveals, and films with fewer than about one decisive event per second.
- Avoid when: Launch films and walkthroughs over about 20 s, dense sequences with more than about 3 visible events per second (use a steady bed instead), briefs that supply a music track, or feeds where the brief asks for high energy.
- Timing: At least 50% of the runtime silent, in gaps of 30-96 f between sound clusters. Opening cluster: 5 ticks over 14 f from frame 0. Reveal pad: on from the act's first frame, swell peak on the first reveal, about 42 f of plateau, about 84 f of ring-out. Sound stops within 1 f of each resolution; the shimmer bell (weight 0.15) fades over about 54 f. Removal ticks rise about 2 dB each. Lockup hold 90-120 f in silence after its single land, under a push of at least 10% across the hold.
- Made with: sloosh-motion-director

### Travelling thread object

- Looks like: One small accent object (a dot, a packet or a streak) recurs across shots and acts, carrying the idea from problem to feature to feature as a single causal chain.
- Use when: Abstract or concept-led launch films whose beats are visually disconnected, and stories about value or data travelling.
- Avoid when: Plain UI walkthroughs where a cursor already guides the eye, since two guides compete.
- Timing: 3-5 appearances of 20-60 f each; head 2-3% of frame height; travel 20-60 px/f with true motion blur; contact squash over about 8 f; a hit pulse (2 f up, 5 f down) on the struck element.
- Made with: sloosh-motion-director


## Micro-interactions (20)

### Chip bloom around content

- Looks like: A container grows out of its content: a dropped icon tile widens into a labelled chip that floods with the accent and wipes back to an outline, or a solid pill swells behind a name so the group becomes a button.
- Use when: An integration, tag or name should become a tangible, clickable object (attached, added, now a button), shown as cause and effect.
- Avoid when: The fill would need several hues to read, or the chip has nothing to do next (a bloom with no follow-up reads as decoration).
- Timing: Tile pop 8 f ease-out; widen 12 f ease-out; fill wipe-off 20 f soft ease-out with an 80 px feather; bloom behind 10 f ease-out with a 6 f text inversion; hold at least 18 f.
- Made with: saas-product-video

### Click to focus: I-beam, ring, caret

- Looks like: An arrow cursor turns into an I-beam as it enters an empty field and clicks. The field's border sharpens, a caret appears and blinks twice at an uneven, human pace, and on the first key the placeholder vanishes and the pointer fades away.
- Use when: A shot opens on an empty prompt, search or chat field and the first action is typing into it, so the click into the field becomes the cause of everything after.
- Avoid when: The field is already focused or pre-filled, the product acts on its own with no cursor, or the film has already played the full two-blink wait once (later prompts start at the first key).
- Timing: Arrive in 24-36 f on smooth ease, 8-12 f before the click; glyph swap 1 f; press 4 f down, 8 f recoil; focus border 5 f UI ease from CLICK - 1; caret blink in hard steps of 18/16/24/12 f (70 f) or 18/16 f (34 f); placeholder gone in 1 f on the first key; I-beam fade 8 f smooth ease; push up to 1.8x over 40-44 f camera ease.
- Made with: saas-product-video

### Cursor glyph follows context

- Looks like: The pointer changes shape with what it is over, as a real system pointer does: an I-beam over text, an open hand over something draggable, a closed fist while dragging, and the arrow everywhere else. Each change is a one-frame swap.
- Use when: A cursor drives a walkthrough that both types and drags, and the pointer must behave like the real system's rather than an arrow stamped on everything.
- Avoid when: The cursor only clicks buttons (the arrow is correct there), or a snappy vertical edit would flash the glyph changes past before they read.
- Timing: Swap in 1 f on the frame the hotspot crosses a rect edge; fist on the pressAt down stroke (4 f down, 8 f recoil); open hand for 6-10 f after the release; item trails the fist by 1-3 f; I-beam approaches at 15 px/f or less.
- Made with: saas-product-video

### Drag, lift and seat

- Looks like: A chip or file picked up by the cursor lifts off the surface, follows the hand with a slight lag and tilt, then drops into its slot with a small contact squash as the slot accepts it.
- Use when: A drag-and-drop (attach a file, add an integration, reorder a card) causes the next state.
- Avoid when: The drag path is long (over about 600 px, cut it), or the item contains text that must be read while it tilts.
- Timing: Lift 8 f ease-out to 1.04 with a 16/32 px shadow. Follow lag 3 f; tilt at most 6 degrees. Slot tint 6 f UI ease. Drop 8 f contact ease, plus squash over about 8 f.
- Made with: saas-product-video

### Guide cursor: arrive, hover, press

- Looks like: A cursor travels a bowed path to the element about to act, the target shows its hover state a few frames after the cursor arrives, and a short press triggers the response on the same frame.
- Use when: A person is driving the product, and dense UI needs a point of view that shows the viewer where to look next.
- Avoid when: The product acts on its own, clicks would come faster than one per 30 f, or the shot already has a pointer such as a focus ring.
- Timing: Calm: arcs at 5-15 px/f on smooth ease, bow 0.15-0.25, arriving 6-12 f early; hover starts 4 f after arrival and takes 4 f. Press: 4 f down, 8 f recoil (pressAt). Snappy: 300 px in 24 f ease-out, dwell about 60 f. At most one click per 30 f, at uneven gaps; exit fade 10 f.
- Made with: saas-product-video

### Send as a ghosted handoff

- Looks like: On send, the composer's text drifts up and fades away while the same content appears above as a posted message, briefly overlapping the old text, instead of flying between containers.
- Use when: A message, prompt or post is submitted and the result appears elsewhere in the same frame; this is calmer and cheaper than a flight.
- Avoid when: The journey itself is the point (show the flight), or the move would serve as a transition between shots, where a crossfade is never the default.
- Timing: Composer out over 12 f smooth ease (-12 px, blur up to 4 px). Bubble in over 18 f from +4 f (12 to 0 px, ease-out with arrive). 8 f of overlap; placeholder back over 8 f.
- Made with: saas-product-video

### Shared highlight walks the menu

- Looks like: One rounded highlight slides from row to row of a sidebar or menu, trailing the cursor, and the chosen row settles into a pale accent tint.
- Use when: Navigation through a menu, sidebar or list should read as a small human decision, with spatial continuity.
- Avoid when: The rows are too small to read at the shot's framing (push in first), or a soft radial bloom would be added to the highlight.
- Timing: 12 f ease-out per hop; about 24 f per row; trails the cursor by 4 f; click tint 8 f UI ease; highlight fade 8 f.
- Made with: saas-product-video

### Spinner resolves to a check

- Looks like: A working indicator (a rotating dashed ring in a step list, or a small spinning disc pushed into the middle of a sentence) turns into a check with a short tag the moment the step is done.
- Use when: The product works through steps on its own (an agent, a sync, an import), and each completion should land as a small lock.
- Avoid when: There is a single long wait with nothing resolving (show progress instead), or all the checks would resolve on one frame.
- Timing: Ring: one turn per 48 f, linear (disc: one per 24 f). Slot opens over 6 f ease-out. Check ring 8 f ease-out from 0.6; tick draws over 8 f from +3 f; tag 8 f. One step every 24-36 f.
- Made with: saas-product-video

### Two-beat confirm cascade

- Looks like: A row of buttons or toggles confirms one by one: the label or knob changes first, the fill follows a beat later, and the rows go at uneven, human gaps.
- Use when: Several integrations, permissions or capabilities switch on, and each confirmation must stay legible at video speed.
- Avoid when: There is only one control (use the press envelope), or every row would start at the same interval.
- Timing: Label 4-6 f; fill 8 f ease-out at +12 f. Knob 8 f ease-out; track 10 f smooth ease. Row gaps such as 4, 15 and 18 f.
- Made with: saas-product-video

### Badge count bump

- Looks like: A notification badge or counter chip ticks up: the digit rolls to the next value while the badge gives a small pulse, once per increment.
- Use when: Incoming activity (messages, leads, approvals) should register as small, countable events on the UI.
- Avoid when: The count is the hero number of the shot (use a full counter), or increments would come faster than about one per 12 f.
- Timing: Digit roll 8 f ease-out; pulse a hit pulse (2 f up, 5 f down) x 0.12; width 8 f ease-out; first appearance on a small quick spring; increments at least 12 f apart, uneven.
- Made with: saas-product-video

### Drag-select snaps glyph by glyph

- Looks like: An I-beam presses at the start of a phrase and drags across it, a tinted highlight grows behind the text one whole character at a time, and on release a small action bar grows out of the selection, ready for the product to act on it.
- Use when: The product acts on a piece of text the user picks (rewrite, translate, comment, format, ask about a passage), and the pick should read as a human choice rather than a preset.
- Avoid when: The text is under about 40 px tall at the shot's framing (push in first), the range spans more than two lines, or the cursor never touches text anywhere else in the film.
- Timing: Drag about 2 f per glyph (24-40 f) on smooth ease, cursor at 12 px/f or less; highlight steps per glyph on whole frames; release 6 f after the last step; action bar 10 f ease-out from +4 f; hold at least 36 f before the edit; replacement typed over about 26 f; double-click presses 8 f apart.
- Made with: saas-product-video

### Focus ring: pop on click, trim to point

- Looks like: A thin outline around a control either pops outward and fades the moment it is clicked, or draws itself clockwise around a target and erases from the tail, pointing at the action without a cursor.
- Use when: A click needs a visible result the next shot can build on, or a calm frame must point at the next action without moving a cursor.
- Avoid when: The cursor already sits on the target (the ring is redundant), or the ring would need a glow or blurred halo to read.
- Timing: Pop: outset 4 to 14 px in 8 f ease-out; opacity 0.9 to 0 over 20 f, linear from the press. Trim: draw 24 f and erase 24 f, both smooth ease (a 48 f loop); dashes 10/8 px, 3 px stroke; next target about 108 f later.
- Made with: saas-product-video

### In-place character rewrite

- Looks like: A small monospace status field is overwritten left to right by its new state, or a sensitive value turns to dots and deletes from the right, all inside the same fixed slot with no layout change.
- Use when: The product's own status (sending, receiving, connected) or a privacy claim should change in place and read as the machine's voice.
- Avoid when: The text is decorative rather than real UI status (it becomes filler text), or the field uses a proportional face, so the columns jump.
- Timing: Overwrite at about 1 character per frame (13 characters in 12 f), linear, starting 8 f after the press peak. Redact: 1 f swap, then 1 dot deleted every 2 f; camera pan 40 f ease-in-out.
- Made with: saas-product-video

### Launch hop that never lands

- Looks like: A centred app icon hops up as if launching, hangs at the top for a beat and starts to fall, and the camera leaves before it lands, so the hop motivates the scene change.
- Use when: Opening the app or launching a feature should motivate the move to the next scene with a familiar OS gesture.
- Avoid when: The icon must come to rest in the same shot (then it needs a real landing), or several icons would hop in turn.
- Timing: Rise 77 px in 10 f soft ease-out; hold 4 f at the top; fall 18 f contact ease; the camera leaves from frame 14; 32 f in all.
- Made with: saas-product-video

### One-element tell before the event

- Looks like: Just before a state change or a cut, exactly one small thing moves, such as a plus glyph turning 45 degrees into an x or an object slowly turning toward its target, while everything else holds.
- Use when: A repeated result cut, or a sudden 2-4 f event, needs anticipation so it reads as caused rather than random.
- Avoid when: Several things already move in the frame (the tell gets lost), or the yaw would leave the rest of the frame static for more than 48 f.
- Timing: Plus: 10 f smooth ease, finishing 6 f before the cut. Yaw: 40 f linear to 35 degrees, with the event on the next frame; camera creep at most 0.1% per frame.
- Made with: saas-product-video

### Radial dash burst around a word

- Looks like: Short dashes burst outward around a hero word on the beat, drift almost imperceptibly while it is read, then fly outward faster as the frame pushes into the cut.
- Use when: A single hero word on a beat needs a physical punch.
- Avoid when: The text is body copy, the shot is UI, or the burst has already been used once in the film.
- Timing: Burst +87 px in 16 f ease-out; drift 0.5 px/f for about 50 f; exit +176 px over the last 20 f ease-in into the cut.
- Made with: saas-product-video

### Anticipation dip before an unlock

- Looks like: Light builds on a locked card, the card briefly darkens as the lock's shackle swings open, then it pops to clean full-tone content, so the release feels bigger than it is.
- Use when: Something locked, gated or hidden becomes available (an unlock, a reveal, access granted) and the moment should land as a payoff.
- Avoid when: The brightness would clip whites into a bloom, or the film already has two big payoff beats.
- Timing: Build 14 f ease-in to 1.5x. Dip 12 f ease-out to 0.8x, with the shackle at -30 degrees. Pop 12 f (7 f on the repeat) with a a hit pulse (3 f up, 6 f down) brightness pulse and a 2.4% scale pulse. About 38 f in all.
- Made with: saas-product-video

### Shape handoff: pill becomes the icon

- Looks like: A labelled capsule empties its text, then collapses at a fixed height into a square tile or circle that becomes the next thing (the app icon, a loader or a dock slot), so the object never disappears, it changes role.
- Use when: A thinking state, prompt or button should hand off to the product identity, or to its new place in the interface, in one continuous take.
- Avoid when: The target shape has nothing to do with the source (the continuity feels arbitrary), or the shot needs a hard cut for rhythm.
- Timing: Backspace 1 character every 1-2 f (pairs every 5 f, width hug 8 f ease-out). Collapse max(40, edge travel / 7) f on ease-in-out at a fixed height (each edge under about 55 px/f). Dock variant 20 f ease-out plus a small quick spring siblings at 6 f. The loader holds about 72 f.
- Made with: morph-shapeshift

### Stretchy tab indicator

- Looks like: The selected pill of a segmented control shoots to the new option with its leading edge arriving first, stretches to about 1.9x its width mid-travel, then hugs the new label as the label takes the active colour.
- Use when: A tab, filter or toggle switch causes the next state (the chart changes, the list swaps) and deserves weight.
- Avoid when: The control has more than about five options in a tight row (the stretch overlaps its neighbours), or the indicator would only read with refraction or a frosted backdrop behind it.
- Timing: Leading edge 12 f, trailing edge 20 f, both glide ease, for hops up to about 250 px. For longer hops keep the 0.6 ratio and lengthen both so the leading edge stays under about 65 px/f (a 420 px hop takes 18 f / 30 f). Label colour 8 f. Calm variant: 48 f smooth ease, 6 f fill fade, 4 f snap.
- Made with: saas-product-video

### Velocity-stretch dot

- Looks like: A small round dot (a cursor or a list marker) stretches into a capsule along its motion in proportion to its speed, anchored at its trailing end, and shrinks back to a dot when it stops.
- Use when: A tiny element must lead the eye across a slab or down a list, and needs speed, direction and character.
- Avoid when: UI truth requires a standard system arrow, or several dots would stretch at once (the trick only reads once).
- Timing: Tail weights 0.8^i over 30 f (a lag of about 4 f): length about rest + 4-5.5 f x speed, back to a dot in 16-20 f. Marker: drop 31 f ease-out; hop 54 px in 22 f smooth ease every 54 f; label colour 8 f; exit: stretch to an ~84 px dash over 17 f (smooth ease), then off on ease-in.
- Made with: saas-product-video


## Depth and 3D (14)

### 3D flip that swaps state

- Looks like: An icon or card turns over in 3D and comes back around changed (outline to solid, grey to full colour), then shrinks and travels to its next place.
- Use when: A state change (activated, connected, colourised) needs a physical cause, especially as the film's only 3D turn.
- Avoid when: Several flips have already happened, or the cards carry heavy text (it goes mirrored and soft mid-turn).
- Timing: Hero flip 10 f ease-in-out, swap on the edge-on frame (about f5); shrink x0.38 plus 290 px over 16 f whip ease (peak about 62 px/f). Deck: 6 f flips, 6 f apart, slot move 12 f glide ease, labels 8 f.
- Made with: saas-product-video

### Product on a thick extruded slab

- Looks like: The live interface sits on the front of a thick matte slab with rounded corners. When the camera orbits or yaws, the slab's solid edge appears, which turns a screen into an object and makes every angle readable.
- Use when: A single-take product walkthrough or a feature film where the camera travels across one interface.
- Avoid when: The film is flat 2D throughout, or the camera never yaws (the edge never shows and the build is wasted).
- Timing: Slab depth 4-5% of its height; the edge reads from 20 deg of yaw and clearly at 30-35 deg. Hero push 60 f smooth ease (peak about 47 px/f mid-move); whip orbit 74 f whip ease, roll at most 11 deg; the caption builds while the camera decelerates.
- Made with: product-reveal

### Tilted object on a spotlit ground

- Looks like: A real card or device lies in perspective on a dark surface under one soft pool of light. Most of the frame falls to black, and a slow drift slides the light across the object's face.
- Use when: A single notification, card or device should feel like an object in a room, not on a slide, especially in a dark, low-key film.
- Avoid when: The same act already tilts things on this axis, or the film is bright and flat; never on a bare screenshot without ground and shadow.
- Timing: Shot 30-84 f. Drift 0.5 px/f linear (eased in from rest over about 60 f at a seam), plus yaw 0.03 deg/f or an orbit of 0.1 deg/f. Pool radius about 35-40% of the frame. Content state changes over 10-14 f on UI ease.
- Made with: product-reveal

### Cube turn to a blank face

- Looks like: Words converge and slide under an icon, then the icon turns 90 degrees like a cube to show a plain accent face that becomes the field for what comes next.
- Use when: Clearing a sentence into a single colour field or a seed for the logo with a clean geometric gesture.
- Avoid when: The tile carries fine detail (it shears during the turn), or the same element was already flipped.
- Timing: Converge 22 f ease-in; cube turn 12 f smooth ease; blank-face freeze 6 f; then the next move.
- Made with: saas-product-video

### Depth orbit ring that collapses into the mark

- Looks like: Small icons orbit the central mark on a tilted ellipse: they grow and pass in front as they come near and shrink behind it as they go far. Then the ring speeds up and contracts into the mark.
- Use when: Showing an ecosystem of integrations or inputs around one core in about 1.5 s, without words.
- Avoid when: The icons must be read or named, or the film already used an orbit; more than 8 icons turns into noise.
- Timing: Orbit omega = 0.67 deg/f (40 deg/s) linear for about 50 f; contraction 34 f on ease-in (ring x0.3, omega x2); icon fade over the last 8 f; mark punch a hit pulse (2 f up, 6 f down) x 0.03.
- Made with: saas-product-video

### Edge-on sliver snaps face-on

- Looks like: A thin edge-on sliver snaps open into a full face-on coin or badge. Most of the turn happens in the first frame, then it eases into place as its face catches the light.
- Use when: Revealing a token, coin, badge or mark decisively, or turning a physical object into the logo at the close.
- Avoid when: Flat UI icons without thickness (the edge-on frame becomes an invisible line), or the film already has several flips.
- Timing: Edge hold 4 f. Snap 10 f ease-out: frames 1-9 reach about 37, 48, 56, 61, 68, 77, 88, 94 and 100% of the turn. Calm form: 22 f soft ease-out to 10 deg with a 0.2H rise. Match cut on the first settled frame.
- Made with: saas-product-video

### Exploded layer stack

- Looks like: A live UI component turns to a three-quarter view and separates into its layers along depth to show how it is built, then snaps back together and turns flat.
- Use when: Explaining what a product is made of (data, logic, interface), or that one surface stacks several capabilities.
- Avoid when: The component is visually thin (the layers look identical), or the act's axis is already yaw.
- Timing: Turn 36 f camera ease; separate 24 f ease-out with a 12 f stagger span, 80-120 px per layer; hold up to 48 f with a 0.05 deg/f yaw; collapse 16 f contact ease plus punch a hit pulse (2 f up, 6 f down) x 0.015; flatten 30 f settle ease, overlapping by 10 f.
- Made with: saas-product-video

### Folded channel that unfolds flat

- Looks like: A wide card starts bent into a U-shaped channel with its side walls folded toward camera. It flattens open while the cards stacked inside fan out into a neat row, then the whole thing tips away.
- Use when: Revealing a list, a set of plans or a stack of items as a tangible moment, not a flat fade-up.
- Avoid when: The same act already uses a vertical-hinge yaw, or the contents are dense text that must be read during the unfold.
- Timing: Unfold 24 f ease-out; inner cards 20 f ease-out, 2 f apart; live hold 30-48 f with breath +2%; tilt-away 16 f ease-in (width 1650 to 1225 px).
- Made with: saas-product-video

### Peek, hover, launch and recede

- Looks like: A device or product panel barely rises from the bottom edge, pauses, then shoots up to centre. It is tipped back as it rises, faces camera as it arrives, and slowly settles away from camera.
- Use when: Introducing hardware or a hero product surface, where anticipation makes the main move feel powerful.
- Avoid when: The film has already used anticipation twice, or the object is small UI (it reads as a bounce).
- Timing: Peek 170 px over 14 f ease-out (peak about 64 px/f); hover 4 f; launch of up to 640 px over 34 f whip ease; tilt 10 to 0 deg over the last 20 f on settle ease; recede x0.93 over 60 f smooth ease.
- Made with: saas-product-video

### Pinned label over a swapping world

- Looks like: A pin pops on a 3D-rendered place and a short data tag on a leader line tracks that point as the camera orbits. On a cut, the world underneath switches between 3D and flat while the tag holds its screen position.
- Use when: Location or geography matters ('this happens in a real place'), or a flat diagram should be revealed as a real object, and back.
- Avoid when: There is no real 3D plate or scene to anchor to; a tag floating over a flat screenshot gains nothing from projection.
- Timing: Pin 8 f ease-out; leader 8 f from +4 f; name 25 px over 12 f ease-out from +12 f; orbit yaw 0.1-0.2 deg/f linear. 3D segment about 90 f, flat segment about 70 f; cut on the zoom's velocity peak, a zoom handoff settle 30 f. Flat-to-3D: 8x to 1x over 18 f ease-out (fastest per-frame ratio about 0.65 at frame 2), settled by f22.
- Made with: saas-product-video

### Press tilt that hides a swap

- Looks like: A card tips in 3D toward the point that was clicked or tapped and relaxes back flat. The content changes on the tilt's peak frame, so the change has a physical cause.
- Use when: Clicks, copies, likes and swaps in a UI walkthrough that need tactility without a flash.
- Avoid when: Every click in the film already tilts (use it for 1-3 key presses), or the target is a tiny chip where the tilt cannot be seen.
- Timing: Press at 10 deg: 8 f in, tau 9 f (under 1 deg by about f30). Snap rock at 12 deg: attack 1 f, tau 2.5 f, settled in about 8 f. Swap on the peak frame; repeat cadence 54 f; often preceded by a 24 f camera ease push-in.
- Made with: saas-product-video

### Card fan that buries, then scatters

- Looks like: A dozen identical cards swoop in from two corners along a curved arc and stack in depth until they bury the frame. They drift for a beat, then scatter outward and leave one small card in the centre that carries the number.
- Use when: A big count or scale claim (cards issued, transactions, users) needs to feel physical before it collapses to one legible number.
- Avoid when: The film already has a card or tile swarm, or the stat must be read at once; in a calm film the 50 f bury is too loud.
- Timing: Per card 50 f on soft ease-out, starts 2 f apart (22 f span): the fan covers 50% of its final area by f6, 90% by f26 and all of it by f50 (peak about 62 px/f). Drift 84 f at 0.2-0.5 px/f plus breath +2%. Scatter 26 f on ease-in, peak about 75 px/f (master motion blur). The hero figure locks 4-6 f after the last card clears.
- Made with: saas-product-video

### Icon lifts out of its row into a 3D hero

- Looks like: A small icon tile peels out of a settings row and inverts from dark to light. It flies to frame centre growing almost 2x, tilted in 3D and slowly turning as it floats into the next chapter.
- Use when: A tiny detail (an integration, a setting, a source) should become the hero of the next section, bridging two chapters.
- Avoid when: The icon has no follow-up role, or another element already did a lift-to-centre in this film.
- Timing: Travel 24-30 f whip ease; colour inversion 18 f smooth ease; grow x1.9 over 27 f ease-out (fastest growth about 3 f in); float 45 f linear (rotateY +4 deg, rotateZ -1.5 deg); exit x0.43 over 12 f ease-in.
- Made with: saas-product-video

### Impact morph with stretch and floor ripple

- Looks like: Something accelerates into a 3D tile. On contact the tile swaps shape and colour in one frame, stretches tall and settles without rebound while the floor beneath it ripples.
- Use when: Cause and effect is the message: raw input hits the product and becomes something new.
- Avoid when: The film has already spent its two true landings or is calm; never as a generic transition.
- Timing: Approach 12 f contact ease (at most 270 px); swap in 1 f; height stretch +31% decaying over about 12 f (a hit pulse (1 f up, 4 f down)); ripple 6 px, tau 6 f, front at 15 px/f, gone by about f20; punch a hit pulse (2 f up, 6 f down) x 0.02.
- Made with: morph-shapeshift
