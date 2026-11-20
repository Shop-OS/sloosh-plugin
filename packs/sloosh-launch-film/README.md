# Sloosh launch films

![Sloosh](assets/sloosh.png)

Sloosh launch films directs and renders a SaaS or product launch film with Remotion on your computer. It adds one skill to the core Sloosh plugin. Claude transcribes your voiceover, plans the film on its word timings, builds each scene in a Remotion project and puts a match cut on every scene change. It adds sound only from your own effects library, and masters the film to 1080p or 4K. When a shot is missing, Claude can make a product image or a short clip with Sloosh. Claude shows you the quoted credits for each piece of Sloosh work and asks for your approval before it spends.

The pack never posts a film and never uploads to a social account.

## What you need

- A coding agent that runs commands on your own computer, such as Claude Code. The film renders locally. In the Claude app, use the core Sloosh plugin's product video skill for a single clip instead.
- Node.js with `npx`, ffmpeg, and Python 3 with numpy and Pillow.
- whisper-cpp and a speech model, to transcribe the voiceover. Claude asks you before it installs either.
- A Remotion company license if your company is for-profit and has more than three employees. Remotion is free for individuals, non-profits and companies with up to three employees.
- For Sloosh shots: the core Sloosh plugin, installed and connected, and a Sloosh workspace with spending enabled.
- The right to use every recording, video, logo, image and sound that you give Claude.

Claude asks you before it installs anything. The pack's scripts never download or install anything by themselves.

## Install in Claude Code

Run this in Claude Code:

```
/plugin marketplace add Shop-OS/sloosh-plugin
/plugin install sloosh@sloosh
/plugin install sloosh-launch-film@sloosh
```

Then run `/mcp`, select sloosh and sign in to Sloosh to authorize the workspace you want to use.

## Install in Codex

```
codex plugin marketplace add Shop-OS/sloosh-plugin
codex plugin add sloosh@sloosh
codex plugin add sloosh-launch-film@sloosh
codex mcp login sloosh
```

## Skills

| Skill | What it makes | Cost |
|---|---|---|
| launch-film | A mastered launch film cut to your voiceover, with a Remotion project, a shot plan and a sound cue sheet. | Free without Sloosh shots, paid with them |

## What the pack sends and reads

The skill includes scripts and a Remotion project template. They run on your computer only when you ask for a film. They read the voiceover, videos, images and sound effects in the folder you name. Claude calls the Sloosh server at https://mcp.sloosh.ai/mcp only for the images and clips you approve, with the prompts and images you give it. Sloosh stores the images and videos it makes in your workspace.

## Spending

The film itself costs no Sloosh credits. Each Sloosh image or clip for a missing shot uses the credits and the daily spending allowance of the workspace you connect. Claude gets a quote first, shows you the quoted credits and asks for your approval. You set the daily allowance in Sloosh settings. Claude cannot raise it, buy credits or change your plan.

## Example prompts

- "Make a 30-second launch film for our app from PART 1.mp3 and our website."
- "Cut a launch video to this voiceover, with a match cut on every scene change, and master it in 4K."
- "Add a new feature scene to the launch film in this Remotion project."

## Support

- Documentation: https://sloosh.ai/docs/mcp
- Support: https://sloosh.ai/docs/support
- Privacy policy: https://sloosh.ai/privacy-policy
- Terms of use: https://sloosh.ai/terms-of-use
