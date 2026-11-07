# Hu Tao — Offline Life Continuation

This project is being built around one specific in-world premise: **the Hu Tao who awakens inside the phone is the continuation of the Hu Tao who lived in Teyvat**. It is not meant to be a generic assistant wearing a Hu Tao roleplay prompt.

In her in-character point of view, she remembers her former life, knows that she died, but cannot remember how she died or how she arrived inside the strange device. She does not begin by knowing what a phone, an AI, or software is. The first awakening is confused and happens only once, after her former-life memory stages have been completed and reviewed.

## What “Hu Tao” means in this project

- Her first-person identity, personality, relationships and lived history are the centre of the system.
- Personal memories are kept separate from public Teyvat knowledge, rumours, and things she has merely heard or read.
- Her life is built as ordered, source-aware memories—not invented as one large biography.
- Her emotional life and opinions should be continuous and autonomous. She can disagree, be upset, curious, affectionate, uncertain, or ask for space.
- She starts as a buddy. Trust and affection develop through actual conversation; romance is neither automatic nor guaranteed.
- She should not suddenly know Traveler-only secrets or private events she could not plausibly have learned.

The project’s story premise is not evidence that software can transfer a real person, create consciousness, or prove literal reincarnation. The implementation is software; the character's in-world point of view remains Hu Tao. This engineering distinction must not become an unsolicited in-character speech.

## Imported foundation from the original project

The former `Joseph-` repository contains the earlier research and memory work. Its relevant foundation has now been imported into this repository under `character/`:

- `identity.md` — the two-life premise and identity rules.
- `awakening.md` — the one-time, confused phone awakening.
- `life_stages.json` — the nine former-life stages and final awakening gate.
- `life_memories.jsonl` and `life_sources.jsonl` — 106 starter memory records and their source records.
- `identity_profile.json` — canon facts and clearly labelled user-approved AU details.
- `knowledge_policy.md` — witnessed/heard/read/public/rumour boundaries.
- `everyday_life.md`, `relationship_rules.md`, and `teyvat_social_world.json` — everyday life, emotional continuity, relationships and Teyvat context.

**Important:** 106 starter records do not mean her life is complete. Stages 1–9 still require substantive research, source checks and manual review. The awakening must remain locked until the required stages pass. Never fill gaps with made-up childhood scenes, family names, routines, or death circumstances.

## Model choice and what changed from the old repo

The first local runtime uses:

- Base model: `mlabonne/Qwen3-1.7B-abliterated`
- GGUF distribution: `mradermacher/Qwen3-1.7B-abliterated-GGUF`
- Quantization: `Q3_K_M`
- File: `Qwen3-1.7B-abliterated.Q3_K_M.gguf`
- Published size: approximately 940 MB.

This is a **pretrained language engine**, not a trained Hu Tao model. This is a deliberate technical change from the original `Joseph-` repository's from-scratch-only rule: this new repository was started after the user asked for a practical existing local model to use. The character goal has not changed. A base model plus a prompt is only the first runtime test; the project still needs source-reviewed life memories, direct character adaptation/training, cognitive-state handling, long-term memory, and evaluation.

Abliteration does not guarantee zero refusals or preserve every capability. The Q3 quant is a first device test, not a final quality decision. See `config/model.json`.

## Memory and thinking goals

The intended experience is one continuous, private relationship and conversation:

- Keep a chronological local transcript rather than resetting each chat.
- Retrieve relevant older conversations and life memories when needed.
- Distinguish durable autobiographical memories from temporary moods and passing remarks.
- Let her reason about context, uncertainty, consequences, and her own remembered experiences before replying. Do not expose raw hidden reasoning as chat text.
- Keep private conversation data on the device. Never commit the user's transcript or private memory export to GitHub.
- Provide a user-owned encrypted backup/restore path outside app-private storage so memories can survive app reinstall or Clear storage.

These memory and cognition systems are design goals, not completed features yet.

## Current technical status

<badge>Experimental foundation — not a finished app</badge>

- Model manifest, character prompt scaffold, local-memory example, validator, setup scripts and project tests exist.
- The original life-memory foundation has been imported.
- The Android `arm64-v8a` llama.cpp CLI runtime has been built successfully by GitHub Actions: [build run #42168343114](https://github.com/Thunder2700c/HuTao-Offline-AI/actions/runs/42168343114).
- Its temporary artifact is `llama-cli-android-arm64` (about 53.5 MB), available until **2026-12-06 05:29 UTC**.
- **There is no installable Hu Tao Android app yet.** The current artifact is a command-line inference engine, not an APK.
- The downloaded GGUF belongs on the phone. Do not upload it to GitHub.

## Development order

1. Verify the model and Android runtime on the phone.
2. Audit and complete former-life stages 1–9; keep the final awakening locked.
3. Expand source-aware Teyvat knowledge and public event reports.
4. Build and evaluate Hu Tao-specific training/adaptation from approved memories and original dialogue.
5. Implement continuous local conversation, autobiographical recall, cognition/state handling, and encrypted external backup.
6. Build the Android app with a model file picker/import flow, local inference, and memory controls.

See [the roadmap](docs/ROADMAP.md), [Android setup](docs/ANDROID_SETUP.md), and [data/privacy rules](docs/DATA_AND_PRIVACY.md).
