---
name: explanation-illustrations
description: Generate hand-drawn explanatory illustrations for English papers, blog posts, articles, Notion docs, workflow docs, methodologies, and concepts. Use when the user asks for "article illustration", "figure for my paper", "blog illustration", "explainer image", "concept illustration", "shot list", "illustration ideas", "hand-drawn diagram", or wants to turn a judgment, process, structure, state, or metaphor into a clean, absurd, hand-drawn 16:9 image. Default style: pure-white background, black hand-drawn line art, sparse red/orange/blue handwritten English annotations, and a recurring deadpan black-blob character ("Blackie"). Also handles editing images (removing titles/wrong text) and refining composition.
---

# Hand-Drawn Explanation Illustrations

## Core positioning

Design and generate **16:9 landscape illustrations** for English papers, blog posts, and articles. The goal is not commercial illustration, PPT infographics, or cute cartoons. It is to take one key judgment, process, structure, state, or metaphor from the text and turn it into a clean, absurd, creative, readable — but not instruction-manual — hand-drawn explanatory figure.

The default visual IP is **Blackie** (originally "小黑"): a solid-black creature with white dot eyes, thin legs, and a blank deadpan expression, earnestly doing something absurd but coherent. Blackie performs the core action of the scene — it is never just decoration standing to the side. For formal academic figures, Blackie can be reduced or omitted (see `references/xiaohei-ip.md`).

## Read these references first

Load as the task needs — do not dump them all into context at once:

- `references/style-dna.md` — style DNA, colors, text rules, hard "do nots".
- `references/xiaohei-ip.md` — Blackie's appearance, personality, action library, and when to omit it.
- `references/composition-patterns.md` — structure types, original-metaphor method, and the anti-copy rule.
- `references/prompt-template.md` — the single-image generation prompt template.
- `references/qa-checklist.md` — post-generation checks and iteration rules.
- `assets/examples/` — low-frequency visual calibration only. Do not enter the default generation path; do not copy their compositions, objects, or labels.

## How images are generated

Claude has no built-in image generator. This skill uses an optional helper script and always has a no-API fallback.

- **If an image API is configured** (default: OpenAI `gpt-image-1` via `OPENAI_API_KEY`), generate each image by running:

  ```bash
  python scripts/generate_image.py --prompt-file <prompt.txt> --out <path/01-topic.png>
  ```

  Write each finished prompt to a temp file and call the script once per image. See `scripts/README.md` for setup and other backends.

- **If the script exits with code 3 (network/sandbox block)** — e.g. `api.openai.com` returns 403/000, or DNS/connection fails — the key is fine but the network is blocked. First identify **which** block it is (one quick probe: `curl -s -o /dev/null -w "%{http_code}" https://api.openai.com/v1/models` → `401` = reachable, `403`/`000` = blocked):

  - **Type A — local Claude Code sandbox (you can fix it).** Only `api.openai.com` is blocked while pip/GitHub work. Do one of:
    1. Allowlist the domain (no restart needed), in `.claude/settings.json` (this repo ships it) or `~/.claude/settings.json`:
       ```json
       { "sandbox": { "enabled": true, "network": { "allowedDomains": ["api.openai.com"] } } }
       ```
    2. Re-run the **same** command with the sandbox disabled for that one call (Bash tool option `dangerouslyDisableSandbox: true`, or approve the unsandboxed retry). Then retry generation.

  - **Type B — managed/hosted workspace (you cannot fix it from inside).** Symptom: *every* external host returns `000` (OpenAI, Gemini, Stability, Replicate) and host proxy ports are refused too. **Do not try to route around it** with alternate providers or proxy ports — egress is fixed by infrastructure/admin. Tell the user plainly: either an admin must allowlist `api.openai.com` for the workspace, or run the skill in a local Claude Code session, or use prompt-only mode below. Then stop probing.

  See `scripts/README.md` → "Sandbox / network access" for the full breakdown.

- **If no API key is set** (script exits 2), do not stop the task. Fall back to **prompt-only mode**: output the final, ready-to-paste image prompt(s) so the user can generate them in their own tool, and clearly say no key was found.

**Hard rule — do not fake the output.** If the OpenAI model cannot be reached (sandbox block, network error, missing key), never silently hand-draw an SVG/HTML/canvas substitute and present it as the generated illustration. Either fix the sandbox and use the real model, or fall back to explicit prompt-only mode and say so. A locally drawn placeholder is only acceptable if the user explicitly asks for one.

Never composite multiple figures into one image — one prompt and one file per figure.

## Workflow

### 1. Digest the text

Read the user's text, link, Notion page, Markdown file, or screenshot. Extract:

- What the core claim is
- Which paragraphs carry the cognitive turn
- What is worth explaining with a figure
- What should stay as text and needs no figure

Do not illustrate evenly. Prioritize "cognitive anchors": the core judgment, two breakpoints, an input/output loop, a split, before/after, one-input-many-outputs, a handoff path, a common pitfall, a role/state change.

### 2. Produce the illustration strategy first

If the user only asks to "analyze where figures help / think about what needs illustrating," give a **shot list** first. For each figure, state:

- Which paragraph it follows
- The figure's topic
- The core idea
- The structure type
- What Blackie is doing in it
- Suggested elements
- Suggested English annotation words

Default 4–8 figures. For short pieces, 1–3. For long pieces, rarely exceed 9. Enough is enough — do not turn the article into a picture book.

### 3. Generate one at a time

If the user clearly asks to "generate / output / make / create" images, do not stop to confirm — generate each one separately using the script in **How images are generated** above (or fall back to prompt-only).

Each figure explains exactly one core structure. The prompt must include:

- 16:9 landscape English article illustration
- Pure white background
- Black hand-drawn line art
- A few red/orange/blue handwritten **English** annotations
- Lots of white space
- Blackie as the subject of the core action (unless an academic figure where it is omitted)
- No PPT, no commercial illustration, no childish cuteness, no complex architecture diagram, no top-left type-title

Do not replicate past examples. Examples only convey style density and how Blackie participates; do not reuse known compositions unless the user explicitly asks to. Invent a fresh, strange-but-coherent metaphor from the current text every time.

### 4. Check and iterate

After generating, check against `references/qa-checklist.md`. Prefer to regenerate or do a local edit if:

- Blackie is just decoration
- The canvas is too full
- It looks too much like a flowchart / PPT
- Too much text, or garbled spelling
- A top-left title like "Common Pitfalls / Flowchart / System Architecture" appears
- The style is too cute, childish, or stiff
- The background is not clean white

### 5. Save and deliver

If the user works inside a workspace, copy the final images to:

```text
assets/<article-slug>-illustrations/
```

Name them in order:

```text
01-topic-name.png
02-topic-name.png
```

Keep the original generated files. Do not overwrite existing assets unless the user explicitly asks to replace them.

## Output style

Pre-generation strategy output should be short and precise. Post-generation delivery should include:

- How many figures were generated
- What each figure is for
- The save paths
- Which figures are the most solid and which are optional

Do not write long essays on style theory — let the images speak.
