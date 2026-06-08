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
- `3` — network/sandbox block (the key is fine, but `api.openai.com` is unreachable).
  See "Sandbox / network access" below — fix it and re-run, don't fake the output.
- `1` — other generation error.

## Sandbox / network access (important)

If the script exits `3`, the API host is unreachable. There are **two different
kinds of block** — they have different fixes, so identify which one you're in.

### Type A — local Claude Code sandbox (you CAN fix this)

Local Claude Code runs Bash in a sandbox that routes outbound traffic through an
allowlist proxy you control via `settings.json`. By default `api.openai.com` is not
allowed, so the proxy returns `403`. Fix it **either** way:

1. **Allowlist the domain (recommended, persistent).** Add to your settings
   (this repo already ships exactly this — keep it):

   ```json
   {
     "sandbox": {
       "enabled": true,
       "network": { "allowedDomains": ["api.openai.com"] }
     }
   }
   ```

   Settings reload live — no restart needed. Entries are bare hostnames (no scheme,
   port, or wildcard). Put it in `~/.claude/settings.json` (all projects),
   `.claude/settings.json` (this project, shared), or `.claude/settings.local.json`
   (personal, gitignored). You can also run `/sandbox` in-session. Verify with:
   `curl -s -o /dev/null -w "%{http_code}\n" https://api.openai.com/v1/models`
   → `401` means reachable (good); `000`/`403` means still blocked.

2. **Disable the sandbox for the one call.** Run the same command with the Bash tool
   option `dangerouslyDisableSandbox: true` (or approve the unsandboxed retry).

For a non-OpenAI backend, allowlist that provider's host instead
(e.g. `generativelanguage.googleapis.com` for Gemini).

### Type B — managed / hosted workspace (you CANNOT fix this from inside)

In a hosted or enterprise workspace (e.g. a Cowork/cloud sandbox), egress is locked
to a fixed allowlist (pip, GitHub, etc.) enforced by **infrastructure / managed
settings**, above anything user `settings.json` can change. Symptom: *every* external
host returns `000` — OpenAI, the image blob host, Gemini, Stability, Replicate — and
the host proxy ports are refused too.

**Do not try to route around it** (random proxy ports, alternate providers). It is an
environment/admin setting. The only fixes are:

- Ask whoever administers the workspace to add `api.openai.com` to the allowed
  egress domains (managed settings), **or**
- Run the skill in a local Claude Code session where you control the sandbox
  (Type A above), **or**
- Fall back to **prompt-only mode**: hand the user the ready-to-paste prompt and let
  them generate in ChatGPT / their own tool.

Never substitute a locally drawn SVG/canvas image as if it were the generated figure.

## Using a different backend

To use Google Gemini image generation, Stability, Replicate, or a local model,
replace the `client.images.generate(...)` block in `generate_image.py` with that
provider's call and keep the same CLI (`--prompt-file` / `--prompt` / `--out`).
The skill only depends on the script's interface and exit codes, not on OpenAI
specifically.
