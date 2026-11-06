#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODEL="${1:-${HOME}/models/Qwen3-1.7B-abliterated.Q3_K_M.gguf}"
LLAMA_CLI="${LLAMA_CLI:-llama-cli}"
CTX_SIZE="${CTX_SIZE:-2048}"
THREADS="${THREADS:-6}"
TOKENS="${TOKENS:-256}"
PROMPT_FILE="${ROOT}/tmp/hu_tao_system_prompt.txt"

if ! command -v "$LLAMA_CLI" >/dev/null 2>&1 && [[ ! -x "$LLAMA_CLI" ]]; then
  echo "ERROR: llama-cli not found. Set LLAMA_CLI to its full path or add it to PATH." >&2
  exit 10
fi

python "$ROOT/scripts/check_model.py" "$MODEL"
python "$ROOT/scripts/build_system_prompt.py" --output "$PROMPT_FILE"

exec "$LLAMA_CLI" \
  --model "$MODEL" \
  --ctx-size "$CTX_SIZE" \
  --threads "$THREADS" \
  --predict "$TOKENS" \
  --temp 0.8 \
  --top-p 0.9 \
  --repeat-penalty 1.1 \
  --system-prompt-file "$PROMPT_FILE" \
  --jinja \
  --chat-template-kwargs '{"enable_thinking":false}' \
  --reasoning-format none \
  --conversation
