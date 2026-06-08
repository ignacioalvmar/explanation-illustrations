#!/usr/bin/env python3
"""Generate one hand-drawn explanation illustration from a text prompt.

Backend: OpenAI Images API (gpt-image-1) by default. This is the optional
"actually create the PNG" step for the explanation-illustrations skill. If no
API key is configured, the skill should fall back to prompt-only mode instead
of calling this script.

Usage:
    python generate_image.py --prompt-file prompt.txt --out 01-topic.png
    python generate_image.py --prompt "..."          --out 01-topic.png

Environment:
    OPENAI_API_KEY   required (for the default OpenAI backend)
    IMAGE_MODEL      optional, default "gpt-image-1"
    IMAGE_SIZE       optional, default "1536x1024" (16:9-ish landscape)

Exit codes:
    0  image written
    2  no API key / missing dependency  -> caller should fall back to prompt-only
    1  generation error
"""

import argparse
import base64
import os
import sys


def eprint(*args):
    print(*args, file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--prompt", help="Prompt text passed inline.")
    src.add_argument("--prompt-file", help="Path to a file containing the prompt.")
    parser.add_argument("--out", required=True, help="Output PNG path.")
    parser.add_argument(
        "--size",
        default=os.environ.get("IMAGE_SIZE", "1536x1024"),
        help="Image size, default 1536x1024 (landscape).",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("IMAGE_MODEL", "gpt-image-1"),
        help="Image model, default gpt-image-1.",
    )
    parser.add_argument(
        "--key-file",
        default=os.environ.get("OPENAI_API_KEY_FILE"),
        help="Path to a file containing the API key (secret-safe alternative to "
        "the OPENAI_API_KEY env var; keep it gitignored).",
    )
    args = parser.parse_args()

    if args.prompt_file:
        with open(args.prompt_file, "r", encoding="utf-8") as fh:
            prompt = fh.read().strip()
    else:
        prompt = args.prompt.strip()

    if not prompt:
        eprint("Error: empty prompt.")
        return 1

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key and args.key_file:
        try:
            with open(args.key_file, "r", encoding="utf-8") as fh:
                api_key = fh.read().strip()
        except OSError as exc:
            eprint(f"Could not read --key-file {args.key_file!r}: {exc}")
            return 2
    if not api_key:
        eprint(
            "No API key found (set OPENAI_API_KEY, or pass --key-file / "
            "OPENAI_API_KEY_FILE pointing at a file with the key). "
            "Fall back to prompt-only mode: show the prompt to the user instead "
            "of generating."
        )
        return 2

    try:
        from openai import OpenAI
    except ImportError:
        eprint(
            "The 'openai' package is not installed. Run: pip install openai\n"
            "Or fall back to prompt-only mode."
        )
        return 2

    client = OpenAI(api_key=api_key)

    try:
        result = client.images.generate(
            model=args.model,
            prompt=prompt,
            size=args.size,
            n=1,
        )
    except Exception as exc:  # noqa: BLE001 - surface any API error to the caller
        msg = str(exc).lower()
        sandbox_signals = (
            "403",
            "forbidden",
            "proxy",
            "connection",
            "name resolution",
            "temporary failure",
            "getaddrinfo",
            "ssl",
            "timed out",
            "connect",
        )
        if any(s in msg for s in sandbox_signals):
            eprint(
                "Image generation failed with what looks like a NETWORK/SANDBOX block, "
                "not an API problem.\n"
                f"  Underlying error: {exc}\n\n"
                "The Claude Code sandbox proxies outbound network through an allowlist, and "
                "api.openai.com must be on it. Fix it ONE of these ways:\n"
                "  1) Add this to .claude/settings.json (then re-run; no restart needed):\n"
                '       { \"sandbox\": { \"enabled\": true, '
                '\"network\": { \"allowedDomains\": [\"api.openai.com\"] } } }\n'
                "  2) Re-run this exact command with the sandbox disabled for this one call "
                "(Bash tool option dangerouslyDisableSandbox=true, or approve the unsandboxed retry).\n\n"
                "Do NOT silently substitute a locally drawn SVG/canvas image. Tell the user to "
                "apply the fix above so the real OpenAI model is used."
            )
            return 3
        eprint(f"Image generation failed: {exc}")
        return 1

    b64 = result.data[0].b64_json
    if not b64:
        # Some models return a URL instead of base64; handle that too.
        url = getattr(result.data[0], "url", None)
        if not url:
            eprint("No image data returned by the API.")
            return 1
        try:
            import urllib.request

            with urllib.request.urlopen(url) as resp:  # noqa: S310 - trusted API URL
                image_bytes = resp.read()
        except Exception as exc:  # noqa: BLE001
            eprint(f"Failed to download image: {exc}")
            return 1
    else:
        image_bytes = base64.b64decode(b64)

    out_dir = os.path.dirname(os.path.abspath(args.out))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(args.out, "wb") as fh:
        fh.write(image_bytes)

    print(args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
