# Image generation helper

Claude Code has no built-in image generator, so this skill creates the actual
PNGs with a small helper script. If you do not configure an API key, the skill
falls back to **prompt-only mode** and just gives you ready-to-paste prompts.

## Default backend: OpenAI `gpt-image-1`

1. Install the client:

   ```bash
   pip install openai
   ```

2. Set your key (PowerShell):

   ```powershell
   $env:OPENAI_API_KEY = "sk-..."
   ```

   Or persist it with `setx OPENAI_API_KEY "sk-..."` (new terminals only).

3. Generate one image per call:

   ```bash
   python scripts/generate_image.py --prompt-file prompt.txt --out assets/my-article-illustrations/01-topic.png
   ```

## Options

| Flag / env       | Default       | Notes                                   |
| ---------------- | ------------- | --------------------------------------- |
| `--prompt-file`  | —             | File with the full prompt.              |
| `--prompt`       | —             | Inline prompt (alternative to file).    |
| `--out`          | —             | Output PNG path (dirs auto-created).    |
| `--size` / `IMAGE_SIZE` | `1536x1024` | Landscape 16:9-ish.               |
| `--model` / `IMAGE_MODEL` | `gpt-image-1` | Image model.                  |

## Exit codes

- `0` — image written to `--out`.
- `2` — no API key or missing `openai` package → the skill should fall back to
  prompt-only mode (show the prompt, do not fail the task).
- `1` — generation error.

## Using a different backend

To use Google Gemini image generation, Stability, Replicate, or a local model,
replace the `client.images.generate(...)` block in `generate_image.py` with that
provider's call and keep the same CLI (`--prompt-file` / `--prompt` / `--out`).
The skill only depends on the script's interface and exit codes, not on OpenAI
specifically.
