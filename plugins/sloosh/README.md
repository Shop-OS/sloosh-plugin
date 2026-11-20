# Sloosh

![Sloosh](assets/sloosh.png)

Sloosh makes product images, ad variants, short videos and voiceovers. This plugin connects Claude to your Sloosh workspace so you can do that from chat:

- Generate images, video clips and audio from a prompt or your own files.
- Find, run and review published Sloosh Spaces, ready-made recipes with a form of inputs, and build, test and publish your own Space on a canvas.
- Make a voiceover from a script with a stock voice or one of your saved voices, or clone a voice from your own samples.
- Edit a video with Calypso, for example to recast a clip with your own character.
- Upload files, import links and social posts, and keep your work in Sloosh projects.

It adds ten skills: product imagery, ad variants, published Spaces, product video, UGC storyboards, video remixes, creative iteration, batch runs, asset management and a skill router that picks the skill for a request that names none.

Sloosh uses the credits and the daily spending allowance of the workspace you connect. Claude shows you the quoted credits and asks for your approval before any paid work. Sloosh blocks paid calls above your "Ask before spending more than" amount until you approve. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Install

Install Sloosh from the Claude directory. Then open the plugin's Connectors tab, select Connect, sign in to Sloosh and authorize the workspace you want to use. In Claude Code, run `/mcp`, select sloosh and sign in.

On a Team or Enterprise plan, an Owner must add the Sloosh connector for the organization before members can connect.

You can also add Sloosh as a custom connector without the skills. In Claude, open Customize, then Connectors, and add a custom connector with this URL: https://mcp.sloosh.ai/mcp.

## What the plugin sends

The plugin runs no code on your computer and ships no scripts. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp with the prompts, files and choices you give it, using the access you grant when you connect. Sloosh stores the images, videos and audio it makes in your workspace.

- Voice cloning uploads the voice samples you give it. Claude asks you to confirm you are the speaker or have the speaker's consent before it clones. Sloosh stores the cloned voice in your workspace, under My voices in Sloosh Studio's Audio page (https://sloosh.ai/studio/audio), where you can delete it.
- Calypso runs editing scripts on your files in a private Sloosh sandbox on Sloosh servers, for your session only, and saves the finished video to your library.
- Importing a social post fetches the public Instagram or X post you paste and saves its media to your workspace.
- Importing a link fetches the public file at the HTTPS link you give and saves it to your workspace.

## Example prompts

- "Make a studio photo of my water bottle on a clean white background."
- "Create three 9:16 ad variants for my summer sale on this sneaker."
- "Find a Space in my workspace that makes product ad grids and tell me what a run costs."
- "Turn my latest product image into a short video clip."
- "Read this line in my warmest saved voice: Summer is here, and so is our new bottle."
- "Remix this 15-second dance clip with my brand character."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
