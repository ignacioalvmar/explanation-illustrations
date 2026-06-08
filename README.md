# Explanation Illustrations (Claude Skill)

> Turn the judgments, processes, states, and metaphors in your papers and blog posts into clean, hand-drawn, absurd-but-tidy article illustrations on a pure-white background.
>
> 16:9 landscape | "Blackie" IP | pure-white hand-drawn | sparse red/orange/blue English annotations | Claude Code Skill

---

## What this repo is

Explanation Illustrations is a **Claude Code Skill** that guides Claude to generate explanatory figures for English papers, blog posts, articles, Notion docs, and methodology content.

It is not a generic illustration prompt, and it is not a PPT-infographic template. The core goal is: first understand the cognitive anchors in the text, then turn **one** judgment, process, structure, state, or metaphor into a memorable 16:9 hand-drawn explanatory figure.

The default visual IP is **Blackie** (originally "小黑"): a solid-black creature with white dot eyes, thin legs, and a blank expression. Blackie is not a mascot, a sticker, or a corner decoration — it is an absurd worker earnestly keeping a system running. For formal academic figures, Blackie can be reduced or omitted.

In one line: **make Claude not just "add an image," but draw out one key cognitive move from your text.**

> This skill was ported from Ian's original Codex skill ("Ian Xiaohei Illustrations"). It now runs on Claude Code, produces English-annotated figures, and is tuned for English papers and blogs. See [NOTICE.md](NOTICE.md) for attribution.

---

## Who it's for

A great fit for:

- People writing English papers, articles, or blog posts who need explanatory figures
- People producing knowledge content, methodology content, or AI-workflow content
- People who want to turn abstract judgments into concrete metaphors
- People who want a lighter, stranger, more personal illustration style than a PPT infographic
- People using Claude for content production who want to reuse one consistent visual language

Not a fit for:

- People who want commercial illustration, brand key visuals, or polished flat illustration
- People who want traditional PPT infographics, complex architecture diagrams, or flowcharts
- People who want children's cartoons, cute IP, or sticker-pack styles
- People who want to cram lots of body text or a full course page into one image
- People who need strictly editable vector source files

---

## What it produces

Default output:

- 16:9 landscape article illustrations
- A 4–8 figure shot list for an article
- Each figure's topic, core idea, structure type, Blackie's action, and suggested English labels
- Final PNG images, saved to `assets/<article-slug>-illustrations/` in your workspace

Not produced by default:

- PPTX / PDF / Keynote
- SVG / HTML / editable Canvas images
- Commercial posters or cover key visuals
- Text-heavy infographics

---

## Visual style

This skill defaults to a "Blackie absurd article illustration" style:

- Pure white background — no paper texture, beige, shadow, or gradient
- Black hand-drawn line art, thin lines, slightly wobbly
- Lots of white space — the subject occupies only ~40%–60% of the canvas
- A few red/orange/blue handwritten English annotations
- One image expresses only one core action, structure, state, or metaphor
- Blackie must participate in the core action — never just decoration
- Absurd, creative, clean — but not childish and not cutesy

---

## Examples

### Two breakpoints

![Two breakpoints](examples/images/01-two-breakpoints.png)

### Sort by purpose

![Sort by purpose](examples/images/02-sort-by-purpose.png)

### One fish, many uses

![One fish, many uses](examples/images/03-one-fish-many-uses.png)

### Handoff path

![Handoff path](examples/images/04-handoff-path.png)

### Information well

![Information well](examples/images/05-information-well.png)

### Idea press

![Idea press](examples/images/06-idea-press.png)

### Content fermentation

![Content fermentation](examples/images/07-content-fermentation.png)

### Trust bridge

![Trust bridge](examples/images/08-trust-bridge.png)

These images are style-calibration samples, not composition templates. Reinvent the metaphor from your current article — do not copy the objects or compositions of past cases.

---

## Install (Claude Code)

Clone the repo:

```bash
git clone https://github.com/helloianneo/ian-xiaohei-illustrations.git
cd ian-xiaohei-illustrations
```

Copy the skill into your Claude Code skills directory.

macOS / Linux:

```bash
mkdir -p ~/.claude/skills
cp -R ./explanation-illustrations ~/.claude/skills/explanation-illustrations
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse .\explanation-illustrations "$env:USERPROFILE\.claude\skills\explanation-illustrations"
```

Claude Code will auto-discover the skill from its `description`. You can also invoke it explicitly with `/explanation-illustrations`.

### Enable actual image generation (optional)

Claude has no built-in image generator. To have the skill create PNGs directly, configure the helper script's backend (default: OpenAI `gpt-image-1`):

```bash
pip install openai
```

```powershell
$env:OPENAI_API_KEY = "sk-..."
```

**Allow the API through the Claude Code sandbox.** Claude Code runs Bash commands in a sandbox that blocks outbound network by default, so even with a valid key the OpenAI call returns `403`. This repo ships a `.claude/settings.json` that allowlists `api.openai.com`:

```json
{ "sandbox": { "enabled": true, "network": { "allowedDomains": ["api.openai.com"] } } }
```

Settings reload live (no restart). If you installed the skill into `~/.claude/skills`, add the same `allowedDomains` entry to your user `~/.claude/settings.json` so it applies in every project. Alternatively, approve the unsandboxed retry when prompted. Details in [explanation-illustrations/scripts/README.md](explanation-illustrations/scripts/README.md) → "Sandbox / network access".

**Without a key, the skill still works** — it falls back to prompt-only mode and gives you ready-to-paste prompts.

---

## How to use

### Planning only (shot list)

```text
Use the explanation-illustrations skill. Don't generate images yet.
Analyze where this article is worth illustrating and output a ~5-figure shot list.
For each figure, state: which paragraph it follows, the topic, the core idea,
the structure type, what Blackie is doing, and suggested English labels.

<paste article>
```

### Generate article illustrations directly

```text
Use the explanation-illustrations skill to generate 4 illustrations for this article.
Requirements: 16:9 landscape, pure white background, black hand-drawn line art,
a few red/orange/blue handwritten English annotations.

<paste article>
```

### One figure for a single idea

```text
Use the explanation-illustrations skill to create one article illustration for:
"Trust isn't shouted into existence — it's laid down one piece of evidence at a time."
Make it absurd but clean, and Blackie must carry the core action.
```

### Edit a figure (remove a title or wrong text)

```text
Use the explanation-illustrations skill to edit this image: remove the
"Flowchart" title in the top-left corner and keep everything else unchanged.
```

More examples in [examples/prompts.md](examples/prompts.md).

---

## Workflow

This skill's flow is:

1. Read the article, Markdown, Notion content, screenshot, or user-supplied topic
2. Extract the core claims, cognitive turns, process structures, and visually suitable paragraphs
3. Output a shot list first — each figure picks only one cognitive anchor
4. Choose a structure type per figure: Workflow, system fragment, before/after, role/state, concept metaphor, layered method, map/route, or mini comic panels
5. Reinvent a low-tech, absurd-but-coherent physical metaphor
6. Let Blackie carry the core action
7. Generate each figure separately via the image model (or output prompts if no key)
8. Check against the QA checklist: white background, white space, Blackie's action, English labels, non-PPT feel, no copied old case
9. Save the final PNGs and report purpose and paths

---

## Directory structure

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── .claude/
│   └── settings.json          # allowlists api.openai.com through the sandbox
├── assets/
│   └── ian-wechat-qr.jpg
├── examples/
│   ├── images/
│   │   ├── 01-two-breakpoints.png
│   │   ├── 02-sort-by-purpose.png
│   │   └── ...
│   └── prompts.md
└── explanation-illustrations/
    ├── SKILL.md
    ├── scripts/
    │   ├── generate_image.py
    │   └── README.md
    ├── assets/
    │   └── examples/
    └── references/
        ├── style-dna.md
        ├── xiaohei-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        └── qa-checklist.md
```

The part you actually install into Claude Code is the subdirectory:

```text
explanation-illustrations/
```

The root README, LICENSE, NOTICE, and examples are GitHub sharing docs.

---

## Notes

- The shorter the in-image text, the more stable the result.
- Each figure should tell one core structure — do not turn the article into a manual.
- Blackie must carry the core action; if removing Blackie leaves the image fully intact, Blackie was too decorative.
- Example images only calibrate line density, white space, color restraint, and how Blackie participates — do not copy their compositions.
- AI image models can produce typos, hallucinated labels, style drift, or extra titles — always review after generating.
- If spelling errors are bad, reduce the number of labels and regenerate.

---

## Related projects

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) — a skill for generating hand-drawn, technical PPT-style page images
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) — a curated list of Claude Code Skills / Agents / Plugins
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) — a guide to building a personal knowledge base with Obsidian + Claude AI

---

## About the author

**Ian** — product designer / one-person-company practitioner / AI builder

Building a one-person company with an AI team.

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- Website: [www.ianneo.xyz](https://www.ianneo.xyz)
- Email: hello.neoc@gmail.com

---

## License

MIT License. See [LICENSE](LICENSE).
