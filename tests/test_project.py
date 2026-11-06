from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

from hutao.prompt import build_system_prompt  # noqa: E402


class ProjectFoundationTests(unittest.TestCase):
    def test_model_manifest_points_to_selected_file(self) -> None:
        manifest = json.loads((ROOT / "config" / "model.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["upstream_model"], "mlabonne/Qwen3-1.7B-abliterated")
        self.assertEqual(manifest["quantization"], "Q3_K_M")
        self.assertEqual(manifest["file"], "Qwen3-1.7B-abliterated.Q3_K_M.gguf")

    def test_prompt_contains_character_contract_and_no_memory_default(self) -> None:
        prompt = build_system_prompt(ROOT)
        self.assertIn("Hu Tao", prompt)
        self.assertIn("Never invent canon facts", prompt)
        self.assertIn("No approved memory notes", prompt)

    def test_prompt_includes_only_explicit_memory_notes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            memory_path = Path(temp) / "memory.json"
            memory_path.write_text(
                json.dumps({
                    "schema_version": 1,
                    "entries": [
                        {"kind": "preference", "content": "The user likes concise replies."}
                    ],
                }),
                encoding="utf-8",
            )
            prompt = build_system_prompt(ROOT, memory_path)
            self.assertIn("[preference] The user likes concise replies.", prompt)

    def test_invalid_memory_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            memory_path = Path(temp) / "memory.json"
            memory_path.write_text('{"schema_version": 99, "entries": []}', encoding="utf-8")
            with self.assertRaises(ValueError):
                build_system_prompt(ROOT, memory_path)


if __name__ == "__main__":
    unittest.main()
