# Data, consent, and privacy policy

## Default privacy behaviour

- All prompts, memory notes, and conversation records are local to the device.
- No network request is required for inference after the model and runtime are installed.
- This repository must not contain private conversation logs, private memory exports, or user identifiers.
- Private user conversations are not training data by default.
- A user must explicitly opt in before a proposed export or training-data contribution. Consent must state what will be copied, where it will go, and whether the copy can be deleted.

## Training-data admission rules

Before any dataset is added, record:

- Exact dataset name, version, source URL, download date, and file hashes.
- Original authorship/provenance (human-written, synthetic, or model-generated).
- Licence and any non-commercial, share-alike, attribution, or redistribution restrictions.
- Which fields are retained and which are excluded.
- Deduplication, personal-data filtering, and train/validation/test split methodology.

Do not silently mix non-commercial sources into a model intended for commercial distribution. Do not describe model-generated or teacher-generated text as human-authored. Do not add scraped dialogue whose rights and provenance are unclear.

## Hu Tao character data

- Use game canon as a source only when the source can be identified and reviewed.
- Label fan interpretation and project fiction separately from canon.
- Do not invent missing biographical details to fill a training example.
- Do not use user-written roleplay or private chats as training examples without explicit permission.

## Model and code licences

The current GGUF repository displays Apache-2.0. Preserve upstream notices and verify the source model card, quantization repository, and any subsequent dataset licences before redistributing weights or publishing adapted weights. The application code's licence does not override model or dataset licences.
