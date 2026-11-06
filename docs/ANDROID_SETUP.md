# Android first-run guide

Target device: Samsung Galaxy S23 FE (Exynos 2200, 8 GB RAM). The first run is a CPU-only baseline. Do not assume Xclipse 920 GPU offload is available.

## 1. Download the model

From the Hugging Face file page, download exactly:

`Qwen3-1.7B-abliterated.Q3_K_M.gguf`

Repository: <https://huggingface.co/mradermacher/Qwen3-1.7B-abliterated-GGUF/tree/main>

The listed size is about 940 MB. Save it in Android's Download folder. Never upload this file to this GitHub repository. Keep it there for now; the first test can load directly from shared Downloads if phone storage is too tight to make a second copy.

## 2. Build the Android command-line runtime for free

This repository includes a manual GitHub Actions workflow that cross-compiles llama.cpp for Android arm64:

1. Open this repository on GitHub.
2. Open **Actions**.
3. Select **Build Android llama.cpp CLI**.
4. Press **Run workflow** and keep the default `master` ref.
5. When it finishes successfully, open the run and download the `llama-cli-android-arm64` artifact.
6. Save the ZIP in Android's Download folder.

The workflow builds the engine, not the model. It uses a standard GitHub-hosted public-repository runner; no paid GPU runner is requested.

## 3. Install Termux and prepare files

Install Termux from its official F-Droid listing or official GitHub releases. Avoid mixing Termux and add-ons installed from different sources.

In Termux:

```bash
pkg update
pkg upgrade -y
pkg install git python unzip
termux-setup-storage
mkdir -p ~/models ~/llama
```

Grant the storage permission when Android asks. Copy the model from shared Downloads into Termux's private home directory:

```bash
cp ~/storage/downloads/Qwen3-1.7B-abliterated.Q3_K_M.gguf ~/models/
```

Extract the Actions artifact ZIP. Adjust the ZIP name if the browser saved a different name:

```bash
unzip ~/storage/downloads/llama-cli-android-arm64.zip -d ~/llama
```

The artifact contains an installed `bin/` and, if needed, `lib/` directory. Locate the executable:

```bash
find ~/llama -type f -name llama-cli
```

## 4. Clone this small source repository

```bash
cd ~
git clone https://github.com/Thunder2700c/HuTao-Offline-AI.git
cd HuTao-Offline-AI
# Use the model under ~/models if you copied it. If not, use the Downloads path shown below.
python scripts/check_model.py ~/models/Qwen3-1.7B-abliterated.Q3_K_M.gguf
python -m unittest discover -s tests -v
```

## 5. Run the first conversation

Set the executable path to the path printed by `find`. Example:

```bash
export LLAMA_CLI="$HOME/llama/bin/llama-cli"
export LD_LIBRARY_PATH="$HOME/llama/lib:$HOME/llama/lib64:${LD_LIBRARY_PATH:-}"
chmod +x scripts/run_model.sh
./scripts/run_model.sh
```

If you did not copy the model into ~/models, pass its Downloads path as the first argument:
```bash
./scripts/run_model.sh ~/storage/downloads/Qwen3-1.7B-abliterated.Q3_K_M.gguf
```

If the artifact's installed directory is nested one level deeper, use that actual path. The first launch may take time to load the model. Start with a 2,048-token context; do not increase it until stability and memory use are measured.

## 6. What to test

Start with these checks, one at a time:

- Can it hold a coherent conversation for at least 10 turns?
- Does it retain the point of the conversation without repeating itself?
- Does its humour feel natural rather than inserted into every reply?
- Can it disagree without becoming hostile?
- Does it distinguish known Genshin canon from invented details?
- Does it ever emit visible `<think>` text despite thinking being disabled?

Record results in a local note. Do not paste private conversation transcripts into public issues or commits.

## Troubleshooting

- **Killed / app closes:** Android may have reclaimed Termux or the process may have exceeded available memory. Close other apps, reboot, keep context at 2,048 or lower, and retry.
- **Not enough storage:** Do not delete Genshin or personal data blindly. The engine build artifact and model both need space. Check free storage first.
- **Missing shared library:** set `LD_LIBRARY_PATH` to the artifact's `lib` directory. If no `lib` directory exists, remove that path from the variable.
- **Unknown option:** update the Android llama.cpp artifact by rerunning the workflow; its CLI flags follow the upstream revision built into that artifact.
- **Slow generation / heat:** CPU-only inference can be slow and warm the phone. Stop if the device becomes uncomfortably hot. GPU acceleration is a later, separately benchmarked task.

The native Android app is a later milestone. This CLI step verifies the model and the phone before app development adds another layer of variables.
