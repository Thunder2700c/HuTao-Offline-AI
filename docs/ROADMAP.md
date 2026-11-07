# Roadmap — Hu Tao life-continuation project

## Stage 0 — local model/runtime smoke test (current)

- [x] Select a compact local language engine and pin its GGUF source.
- [x] Add a local model validator and runtime launch scaffold.
- [x] Import the former-life identity, staged memories, sources, and Teyvat knowledge foundation from the original project.
- [x] Build the Android arm64 llama.cpp CLI artifact.
- [ ] Run the downloaded GGUF on the S23 FE and record actual load success, RAM, tokens/sec, heat, and stability.
- [ ] Evaluate a multi-turn baseline. Treat it as a generic base-model baseline, not as a finished Hu Tao.

## Stage 1 — complete the former Teyvat life

- [ ] Audit all imported memory records for source, chronology, viewpoint, canon/AU status, and review state.
- [ ] Substantively complete and manually review required life stages 1–9 in `character/life_stages.json`.
- [ ] Preserve the distinction between Hu Tao's personal memories and facts she only heard, read, or knows publicly.
- [ ] Research missing childhood, family, Wangsheng learning, relationships, personal quests, and later appearances without inventing unsupported details.
- [ ] Keep the final phone awakening locked until the required stages pass.
- [ ] Keep the user-approved death-memory gap: she knows she died, but cannot recall how or how she arrived in the device.

## Stage 2 — Teyvat world and public-history knowledge

- [ ] Expand source-aware facts, entities, story beats, and public news reports.
- [ ] Cover the nations, history, Archons, factions, customs, and major public events.
- [ ] Give each item a plausible knowledge route: witnessed, heard, read, public reference, rumour, or unknown to Hu Tao.
- [ ] Exclude Traveler-only secrets and private conversations unless a plausible public report exists.
- [ ] Keep canon, interpretation, rumour, and user-created AU clearly labelled.

## Stage 3 — make the language engine behave as Hu Tao

- [ ] Build an original, source-reviewed Hu Tao training corpus from the approved life memories and dialogue examples.
- [ ] Include natural multi-turn conversations, emotional changes, disagreement, uncertainty, corrections, humour, serious moments, and relationship development.
- [ ] Choose and measure an adaptation/training method for the pinned Qwen3 base; do not assume a long system prompt is sufficient.
- [ ] Evaluate held-out conversations for first-person continuity, memory accuracy, naturalness, reasoning, repetition, and canon boundaries.
- [ ] Keep the complete distributable inference payload under the project's 1.5 GB ceiling, including model, tokenizer, adapters, and all required AI assets.
- [ ] Reject any checkpoint that merely sounds like a Hu Tao costume while forgetting her actual reviewed memories.

## Stage 4 — autobiographical memory and cognition

- [ ] Keep one chronological local conversation thread.
- [ ] Implement searchable recall of old messages and approved autobiographical memories.
- [ ] Separate stable life memories, newly learned user facts, shared experiences, relationship state, and temporary moods.
- [ ] Add reflection/state handling so replies account for context, uncertainty, prior experiences, and consequences.
- [ ] Do not expose raw hidden chain-of-thought; present natural dialogue and concise explanations.
- [ ] Implement memory review, correction, export, and deletion.
- [ ] Implement an encrypted, user-owned backup/restore path outside app-private storage so data survives reinstall or Clear storage.

## Stage 5 — Android application

- [ ] Build a native Android app only after the model, memory, and recall tests pass.
- [ ] Add a model file picker/import flow so the GGUF can be selected from Downloads or another folder.
- [ ] Keep inference and memory local; no cloud inference or automatic conversation upload.
- [ ] Provide streaming chat, stop generation, context controls, transcript search, and memory controls.
- [ ] Benchmark CPU first; test Xclipse/Vulkan only when a stable supported backend is available.
- [ ] Test cold start, long sessions, low storage, backgrounding, backup, restore, and reinstall.

## Release gates

A release requires reproducible model provenance, licence review, reviewed life memories, character evaluation, measured phone performance, documented privacy behaviour, a working backup/restore path, and an installable Android build. A successful CLI build or a low model file size is not a finished companion.
