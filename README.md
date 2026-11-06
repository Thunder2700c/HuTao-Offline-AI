# Hu Tao Offline AI

An Android-first, local-only companion project exploring a consistent Hu Tao character simulation on top of a small local language model.

> **Status: foundation / experimental.** The repository does not contain model weights, a trained Hu Tao model, a finished Android app, or evidence of sentience. The current base is a third-party pretrained model. This project adds a local character, memory, and evaluation layer around it.

## Current foundation

- **Base model:** `mlabonne/Qwen3-1.7B-abliterated`
- **Runtime format:** GGUF
- **Initial quantization:** `Q3_K_M`
- **File:** `Qwen3-1.7B-abliterated.Q3_K_M.gguf`
- **Published file size:** about 940 MB (Hugging Face display; exact downloaded bytes can vary only if the upstream file changes).
- **Quantized distribution:** [mradermacher/Qwen3-1.7B-abliterated-GGUF](https://huggingface.co/mradermacher/Qwen3-1.7B-abliterated-GGUF)
- **Upstream model card:** [mlabonne/Qwen3-1.7B-abliterated](https://huggingface.co/mlabonne/Qwen3-1.7B-abliterated)
- **License shown by the GGUF repository:** Apache-2.0. Re-check the upstream model card and terms before redistribution.

The Q3_K_M file is a deliberately small first test, not a claim that it is the highest-quality quant. The model card lists larger Q4/Q5 variants. We will test output quality and memory on the actual phone before choosing a final quantization.

## Non-negotiable design principles

1. **Offline-first:** no remote inference, analytics, or automatic upload of conversations.
2. **Private memory:** user conversations stay on the device and are not training data by default.
3. **Character, not a costume:** separate canon facts, personality rules, conversational style, and relationship/memory state. Never invent unknown canon as fact.
4. **Honest identity:** Hu Tao is a fictional character simulation. The app must not claim that the model is conscious or literally Hu Tao.
5. **No forced relationship:** Hu Tao can disagree, decline, set boundaries, and change the subject naturally.
6. **Measured claims:** evaluate multi-turn coherence, character consistency, repetition, latency, memory use, and refusal behaviour. Do not equate abliteration with guaranteed zero refusals.
7. **Model provenance:** keep the upstream model, licence, quantization, and file hash recorded. Never commit model binaries to this repository.

## Repository map

- `config/model.json` — pinned model source and runtime defaults.
- `persona/hu_tao.md` — character contract and known/unknown canon boundaries.
- `prompts/system.md` — initial system instruction template.
- `docs/ANDROID_SETUP.md` — Android / Termux first-run guide.
- `docs/ROADMAP.md` — staged development plan.
- `docs/DATA_AND_PRIVACY.md` — dataset, consent, privacy, and licence policy.
- `scripts/check_model.py` — local GGUF integrity and size check.
- `scripts/run_model.sh` — llama.cpp CLI launch helper (after llama.cpp is built).
- `tests/` — offline tests for project configuration and prompt assembly.

## Quick start (first model smoke test)

1. Download the exact GGUF file from the model repository linked above. Do **not** upload it to GitHub.
2. On the Android phone, place it in Termux's private home directory, e.g. `~/models/`. See [Android setup](docs/ANDROID_SETUP.md).
3. Build or obtain a compatible Android `llama.cpp` binary. The official upstream Android guide is [here](https://github.com/ggml-org/llama.cpp/blob/master/docs/android.md).
4. Run `python scripts/check_model.py ~/models/Qwen3-1.7B-abliterated.Q3_K_M.gguf`.
5. Run a short model smoke test with `scripts/run_model.sh` after `llama-cli` is available.

## What this project is not yet

- Not a finished Android chat app.
- Not a newly trained language model.
- Not a verified claim of uncensored behaviour or unchanged reasoning.
- Not a promise that a 1.7B model will behave like a human or reproduce every aspect of the game character.

See [the roadmap](docs/ROADMAP.md) for the next milestones.
