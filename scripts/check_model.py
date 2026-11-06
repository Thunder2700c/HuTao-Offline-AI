#!/usr/bin/env python3
"""Validate the expected local GGUF file without uploading or modifying it."""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

EXPECTED_NAME = "Qwen3-1.7B-abliterated.Q3_K_M.gguf"
MIN_BYTES = 800 * 1024 * 1024
MAX_BYTES = 1100 * 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path, help="Path to the downloaded GGUF file")
    args = parser.parse_args()
    path = args.model.expanduser()

    if not path.is_file():
        print(f"ERROR: model file not found: {path}", file=sys.stderr)
        return 2
    if path.name != EXPECTED_NAME:
        print(f"WARNING: expected filename {EXPECTED_NAME!r}; got {path.name!r}")
    size = path.stat().st_size
    if size < MIN_BYTES or size > MAX_BYTES:
        print(
            f"ERROR: file size {size:,} bytes is outside the expected Q3_K_M range "
            f"({MIN_BYTES:,}–{MAX_BYTES:,} bytes). Re-check the selected file.",
            file=sys.stderr,
        )
        return 3
    with path.open("rb") as handle:
        magic = handle.read(4)
    if magic != b"GGUF":
        print("ERROR: file does not begin with the GGUF magic bytes.", file=sys.stderr)
        return 4

    print("GGUF header: valid")
    print(f"File: {path}")
    print(f"Size: {size:,} bytes ({size / (1024 * 1024):.1f} MiB)")
    print(f"SHA-256: {sha256_file(path)}")
    print("Keep this hash with your local model record; do not upload the model to GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
