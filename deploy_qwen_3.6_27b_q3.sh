source /venv/main/bin/activate
export PATH="/venv/main/bin:$PATH"
source /workspace/cpp/.venv/bin/activate


/workspace/cpp/llama.cpp/build/bin/llama-server \
  --model /workspace/Qwen3.6-27B-GGUF/Qwen3.6-27B-Q3_K_S.gguf \
  --mmproj /workspace/Qwen3.6-27B-GGUF/mmproj-F16.gguf \
  --alias "unsloth/Qwen3.6-27B-GGUF" \
  --threads -1 \
  --n-gpu-layers 999 \
  --prio 3 \
  --min-p 0.01 \
  --ctx-size 16384 \
  --port 8001 \
  --jinja \
  --image-min-tokens 1024
