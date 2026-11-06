"""Build a local-only system prompt from project files and approved memory notes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _read_memory(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    try:
        payload: Any = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read memory file {path}: {exc}") from exc

    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise ValueError("Memory file must be an object with schema_version=1.")
    entries = payload.get("entries", [])
    if not isinstance(entries, list):
        raise ValueError("Memory 'entries' must be a list.")

    clean: list[dict[str, str]] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError(f"Memory entry {index} must be an object.")
        kind = entry.get("kind", "note")
        content = entry.get("content")
        if not isinstance(kind, str) or not isinstance(content, str) or not content.strip():
            raise ValueError(f"Memory entry {index} needs non-empty string kind and content.")
        clean.append({"kind": kind.strip()[:40], "content": content.strip()[:1200]})
    return clean[-20:]


def build_system_prompt(
    root: Path,
    memory_path: Path | None = None,
) -> str:
    """Return the complete system prompt. Does not read or write chat history."""
    root = root.resolve()
    persona_path = root / "persona" / "hu_tao.md"
    template_path = root / "prompts" / "system.md"
    memory_path = memory_path or (root / "data" / "memory.json")

    persona = persona_path.read_text(encoding="utf-8").strip()
    template = template_path.read_text(encoding="utf-8")
    memories = _read_memory(memory_path)

    if memories:
        memory_block = "\n".join(
            f"- [{item['kind']}] {item['content']}" for item in memories
        )
    else:
        memory_block = "- No approved memory notes have been added yet."

    result = template.replace("{{CHARACTER_PROFILE}}", persona)
    result = result.replace("{{MEMORY_BLOCK}}", memory_block)
    if "{{CHARACTER_PROFILE}}" in result or "{{MEMORY_BLOCK}}" in result:
        raise ValueError("A required prompt placeholder was not replaced.")
    return result.strip() + "\n"
