# Roadmap

## Stage 0 — model and device validation (current)

- [x] Pin an upstream pretrained model and a reproducible GGUF filename.
- [x] Create local model integrity checks.
- [x] Create a prompt assembly layer with local-only memory notes.
- [ ] Build an Android arm64 llama.cpp CLI artifact using GitHub Actions.
- [ ] Run the Q3_K_M model on the target phone and record actual RAM, speed, heat, and stability.
- [ ] Evaluate short and multi-turn dialogue before any fine-tuning.

## Stage 1 — reliable character layer

- Add a source-tracked canon fact base with explicit provenance.
- Separate character traits, world knowledge, uncertainty, and project-specific story choices.
- Build a regression set for voice, canon accuracy, natural dialogue, disagreement, boundaries, and repetition.
- Compare base model outputs with prompt-only outputs; keep only changes that improve measured results.

## Stage 2 — private memory

- Store explicit, user-approved memory locally.
- Add review, edit, export, and delete controls.
- Keep conversation history separate from long-term memory.
- No automatic training on private conversations and no cloud sync by default.

## Stage 3 — native Android app

- Use the official llama.cpp Android binding as the inference reference.
- Build a Kotlin UI with local model selection, chat streaming, stop generation, context management, and memory controls.
- Keep model files outside the APK and allow the user to select a GGUF from shared storage.
- Test arm64 CPU baseline first; investigate Vulkan/Xclipse only if the driver path is demonstrably supported.

## Stage 4 — adaptation and training

- Audit training-data provenance, licence, and suitability before use.
- Build a source-separated, deduplicated, human-reviewed dialogue corpus.
- Consider parameter-efficient character adaptation only after baseline evaluation and only with datasets whose terms permit the intended use.
- Never train on user conversations unless the user opts in to a clearly described, reversible data-export process.
- Compare checkpoints against the fixed evaluation set; reject adaptations that damage reasoning, coherence, or character consistency.

## Release gates

A release requires: reproducible model provenance, licence review, no private data in training artifacts, documented memory behaviour, repeatable evaluation, and an Android install/test path. Model size alone is not a quality metric.
