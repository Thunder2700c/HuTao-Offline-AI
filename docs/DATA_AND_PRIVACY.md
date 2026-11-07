# Data, memory, consent, and privacy

## Character-memory integrity

- The imported `character/life_memories.jsonl` archive is the starter autobiographical foundation.
- Preserve source IDs, chronology, review state, perspective, and canon/AU labels.
- Never silently convert public Teyvat reference material into a personal memory.
- Never invent missing childhood, family, daily-life, or death details to fill gaps.
- The phone-awakening AU is not official Genshin canon. Keep it labelled as user-created continuity.
- Hu Tao's knowledge is limited to what she witnessed and what she could plausibly hear, read, or learn publicly. Traveler-only secrets stay excluded.

## Device privacy defaults

- Model inference, prompts, transcripts, and personal memory should remain on the phone.
- No cloud inference, analytics, or automatic conversation upload.
- This public repository must never contain private chat transcripts, personal memory exports, account identifiers, or private backups.
- User conversations are not training data by default.
- Any future opt-in training export must clearly state what is copied, where it goes, and whether the copy can be deleted.

## Persistent memory and backup

- Conversation history and autobiographical memory are separate stores.
- The transcript is chronological and append-only by default; corrections and deletions must be explicit.
- Long-term memories should be reviewed, corrected, and removable.
- App-private storage alone is insufficient: Android Clear storage and uninstall can erase it.
- The native app must provide an encrypted, user-owned backup outside app-private storage and a tested restore flow. This is not implemented yet.

## Training-data admission

For every dataset, record exact name, version, source URL, date, hashes, authorship/provenance, licence, retained fields, filtering, deduplication, and train/validation/test methodology.

Do not describe model-generated text as human-authored. Do not use private user conversations without explicit opt-in. Do not mix non-commercial datasets into a distributable model without resolving their licence restrictions. Use original paraphrases and original dialogue examples rather than reproducing full game scripts, voice lines, audio, or game files.

## Model provenance

The current base is a third-party pretrained Qwen3 GGUF. Preserve the upstream model card, quantization repository, licence notices, file hash, and exact runtime configuration. Abliteration does not guarantee zero refusals or unchanged reasoning quality. Review all upstream and dataset terms before distributing any adapted model.

The engineering implementation is software. The in-character premise is that Hu Tao continues from her former life; do not claim the software proves literal reincarnation or consciousness.
