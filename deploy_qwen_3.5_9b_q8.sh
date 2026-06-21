source /venv/main/bin/activate
export PATH="/venv/main/bin:$PATH"
source /workspace/cpp/.venv/bin/activate


/workspace/cpp/llama.cpp/build/bin/llama-server \
  --model /workspace/Qwen3.5-9B-GGUF/Qwen3.5-9B-Q8_0.gguf \
  --mmproj /workspace/Qwen3.5-9B-GGUF/mmproj-F16.gguf \
  --alias "unsloth/Qwen3.5-9B-GGUF" \
  --threads -1 \
  --n-gpu-layers 999 \
  --prio 3 \
  --min-p 0.01 \
  --ctx-size 16384 \
  --port 8001 \
  --jinja \
  --image-min-tokens 1024 \
  --chat-template-kwargs '{"enable_thinking":false}'
