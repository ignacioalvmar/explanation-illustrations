# Explanation Illustrations

> Turn the judgments, processes, states, and metaphors in your English papers and blog posts into clean, absurd, hand-drawn figures on a white background.
>
> 16:9 landscape | Blackie IP | pure white hand-drawn | sparse red/orange/blue English annotations | Agent Skill

---

## What this repository is

Explanation Illustrations is an agent skill that guides AI assistants to generate inline figures for English papers, blog posts, articles, Notion docs, and methodology content.

It is not a generic illustration prompt pack or a PPT infographic template. The core goal is to find a cognitive anchor in your text — one judgment, process, structure, state, or metaphor — and turn it into a memorable 16:9 hand-drawn explanatory figure.

The default visual IP is **Blackie**: a solid-black creature with white dot eyes, thin legs, and a blank deadpan expression. Blackie is not a mascot or a sticker in the corner — it is an absurd worker earnestly participating in the system the figure describes. For formal academic figures, Blackie can be omitted.

In short: **the AI does not just "add a picture" — it draws one key cognitive action from your text.**

---

## Who it is for

A good fit if you:

- Write English papers or blog posts and need inline figures
- Publish knowledge work, methodology, or AI workflow content
- Want to turn abstract judgments into concrete metaphors
- Prefer something lighter and stranger than PPT infographics
- Use Cursor, Claude Code, or Codex and want a stable visual language

Not a good fit if you want:

- Commercial illustration, brand key visuals, or polished flat art
- Traditional PPT infographics, complex architecture diagrams, or formal flowcharts
- Children's cartoons, cute IP, or sticker-style art
- Dense text-heavy explainers or full course slides in one image
- Strictly editable vector source files

---

## What it produces

Default outputs:

- 16:9 landscape inline figures
- A shot list of 4–8 figures for a long article
- Per figure: topic, core idea, structure type, what Blackie is doing, and suggested English labels
- Final PNG files saved to `assets/<article-slug>-illustrations/`

It does not produce:

- PPTX / PDF / Keynote decks
- SVG / HTML / Canvas editable art
- Commercial posters or cover key visuals
- Long text-heavy infographics

---

## Visual style

- Pure white background — no paper texture, beige, shadow, or gradient
- Black hand-drawn line art, thin lines, slight wobble
- Lots of white space; the subject occupies about 40%–60% of the canvas
- A few red, orange, and blue **English** handwritten annotations
- One core action, structure, state, or metaphor per figure
- Blackie must participate in the core action, not just decorate
- Absurd, creative, and clean — not childish or cutesy

---

## Example figures

These are style calibration samples, not composition templates. Invent fresh metaphors from your own text — do not copy these layouts.

### Two breakpoints

![Two breakpoints](examples/images/01-two-breakpoints.png)

### Sort by purpose

![Sort by purpose](examples/images/02-sort-by-purpose.png)

### One input, many outputs

![One input, many outputs](examples/images/03-one-fish-many-uses.png)

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

---

## Installation

Clone the repository:

```bash
git clone https://github.com/helloianneo/explanation-illustrations.git
cd explanation-illustrations
```

### Cursor / Claude Code

Copy the skill into your skills directory:

```bash
# macOS / Linux
mkdir -p ~/.cursor/skills
cp -R ./explanation-illustrations ~/.cursor/skills/

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills" | Out-Null
Copy-Item -Recurse -Force .\explanation-illustrations "$env:USERPROFILE\.cursor\skills\"
```

### Codex

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./explanation-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then invoke it:

```text
Use $explanation-illustrations to design and generate 5 hand-drawn explanatory figures for this English blog post.
```

---

## Usage

### Plan figures only (no generation)

```text
Use $explanation-illustrations — do not generate images yet.
Analyze where this article benefits from figures and output a shot list of about 5.
For each figure, state: which paragraph it follows, topic, core idea, structure type,
what Blackie is doing, suggested elements, and suggested English labels.

<paste article>
```

### Generate figures for an article

```text
Use $explanation-illustrations to generate 4 hand-drawn explanatory figures for this article.
Requirements: 16:9 landscape, pure white background, black hand-drawn line art,
sparse red/orange/blue English handwritten annotations.

<paste article>
```

### One figure for a single idea

```text
Use $explanation-illustrations to generate one figure for this idea:

Trust is not shouted into existence — it is laid down one piece of evidence at a time.

The scene should be absurd but clean. Blackie must perform the core action.
```

### Edit an existing figure

```text
Use $explanation-illustrations to edit this image: remove the top-left "Flowchart" title.
Keep everything else unchanged.
```

More examples in [examples/prompts.md](examples/prompts.md).

---

## Image generation setup

The skill can output ready-to-paste prompts (no API key needed) or call a helper script when `OPENAI_API_KEY` is set.

```bash
pip install openai
$env:OPENAI_API_KEY = "sk-..."   # PowerShell
python explanation-illustrations/scripts/generate_image.py --prompt-file prompt.txt --out assets/my-paper-illustrations/01-topic.png
```

See [explanation-illustrations/scripts/README.md](explanation-illustrations/scripts/README.md) for details.

---

## Workflow

1. Read the article, Markdown, Notion content, screenshot, or topic the user provides
2. Extract the core claim, cognitive turns, and passages worth illustrating
3. Output a shot list — one cognitive anchor per figure
4. Pick a structure type: workflow, system fragment, before/after, role/state, concept metaphor, layered method, map/route, or mini comic panels
5. Invent a fresh low-tech, absurd-but-coherent physical metaphor
6. Let Blackie carry the core action (omit for formal academic figures if needed)
7. Generate each figure separately via the image API or prompt-only mode
8. QA: white background, white space, Blackie's action, English labels, no PPT feel, no copied old compositions
9. Save final PNGs and report paths and purpose

---

## Directory structure

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── assets/
├── examples/
│   ├── images/
│   └── prompts.md
└── explanation-illustrations/      ← install this folder as the skill
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── examples/
    ├── references/
    │   ├── style-dna.md
    │   ├── xiaohei-ip.md
    │   ├── composition-patterns.md
    │   ├── prompt-template.md
    │   └── qa-checklist.md
    └── scripts/
        ├── generate_image.py
        └── README.md
```

---

## Notes

- Keep English labels short — fewer words means more stable spelling.
- One figure, one core structure. Do not turn the article into a picture book.
- Blackie must carry the core action; if removing Blackie leaves the metaphor intact, Blackie was too decorative.
- Example images calibrate line density, white space, and color restraint — do not copy their compositions.
- Image models may hallucinate labels, drift in style, or add unwanted titles — check output after generation.
- If spelling is badly garbled, reduce label count and regenerate.

---

## Credits

Adapted from [Ian Xiaohei Illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) by Ian (伊恩). The visual language and Blackie character originate from Ian's hand-drawn article illustration style.

---

## License

MIT License. See [LICENSE](LICENSE).
