# Android first-run guide — CLI test only

**Important:** There is no installable Hu Tao APK yet. The current downloadable runtime is a command-line llama.cpp build for Android arm64. You do not upload the model to GitHub and you do not install a Hu Tao app at this stage.

Target device: Samsung Galaxy S23 FE, Exynos 2200, 8 GB RAM. First test is CPU-only. Do not assume Xclipse 920 GPU offload.

## 1. Keep the model on your phone

The expected file is:

`Qwen3-1.7B-abliterated.Q3_K_M.gguf`

Keep it in Android's **Download** folder. **Do not upload it to GitHub.** Do not create a second 940 MB copy unless necessary; the Termux shared-storage path can read the Downloads file directly.

## 2. Download the already-built Android runtime

Open the successful [Android runtime build](https://github.com/Thunder2700c/HuTao-Offline-AI/actions/runs/42168343114).

1. Sign in to GitHub if prompted.
2. Scroll to **Artifacts**.
3. Download `llama-cli-android-arm64`.
4. Save the ZIP in your phone's Download folder.

This artifact is about 53.5 MB and expires on **2026-12-06 05:29 UTC**. It is an engine, not an APK.

## 3. Install Termux

Install Termux from its official F-Droid listing or official GitHub releases. Do not mix Termux and add-ons from different sources.

Open Termux and run:

```bash
pkg update
pkg upgrade -y
pkg install git python unzip
termux-setup-storage
mkdir -p ~/llama
```

Grant storage access when Android asks.

## 4. Extract the runtime and get the project

```bash
unzip ~/storage/downloads/llama-cli-android-arm64.zip -d ~/
git clone https://github.com/Thunder2700c/HuTao-Offline-AI.git
cd ~/HuTao-Offline-AI
```

If the browser saved the ZIP with a different filename, use that actual filename. Locate the executable:

```bash
find ~ -type f -name llama-cli
```

Set the path to the result. The expected layout after extraction is usually `~/llama/bin/llama-cli` or `~/llama/llama/bin/llama-cli` depending on the ZIP's top-level folder.

For example:

```bash
export LLAMA_CLI="$HOME/llama/bin/llama-cli"
```

If your `find` result is different, use that exact path instead. Add the matching library directory:

```bash
export LD_LIBRARY_PATH="$(dirname "$LLAMA_CLI")/../lib:$(dirname "$LLAMA_CLI")/../lib64:${LD_LIBRARY_PATH:-}"
```

## 5. Validate the model in Downloads

Run:

```bash
python scripts/check_model.py ~/storage/downloads/Qwen3-1.7B-abliterated.Q3_K_M.gguf
python -m unittest discover -s tests -v
```

The validator checks the GGUF header and expected file-size range and prints a SHA-256 hash. Keep that hash in your own private notes; do not commit the model or its private usage logs.

## 6. Start the baseline model

```bash
chmod +x scripts/run_model.sh
./scripts/run_model.sh ~/storage/downloads/Qwen3-1.7B-abliterated.Q3_K_M.gguf
```

Start with the default 2,048-token context and six CPU threads. The first model load can take time. The base model may not yet behave like the completed Hu Tao project: this is only a local inference smoke test. The imported life memories are not yet a trained character model.

If Android kills Termux or the process, close other apps and retry. Do not increase context until memory use and stability are measured. Stop if the phone becomes uncomfortably hot.

## 7. What happens after this test

After the runtime and model work, we will complete/review the former-life memories, build Hu Tao-specific training/adaptation and memory/cognition systems, and only then create the native Android app.

**Later app behaviour:** the finished app is intended to have an Import Model button/file picker, so you can select the GGUF from Downloads. That app does not exist yet; for now use the Termux CLI instructions above.
