#!/usr/bin/env python3
"""Render the character prompt plus explicitly approved local memory notes."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from hutao.prompt import build_system_prompt  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "tmp" / "system_prompt.txt")
    parser.add_argument("--memory", type=Path, default=ROOT / "data" / "memory.json")
    args = parser.parse_args()

    try:
        prompt = build_system_prompt(ROOT, args.memory.expanduser())
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    output = args.output.expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(prompt, encoding="utf-8")
    print(f"System prompt written locally to: {output}")
    print(f"Prompt length: {len(prompt):,} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
