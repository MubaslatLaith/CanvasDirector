cd ..
mkdir cpp 
cd cpp 
python3 -m venv .venv
source /venv/main/bin/activate
export PATH="/venv/main/bin:$PATH"
source /workspace/cpp/.venv/bin/activate
pip install huggingface_hub
apt-get update
apt install -y cuda-toolkit
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
  -DBUILD_SHARED_LIBS=OFF \
  -DGGML_CUDA=ON \
  -DLLAMA_CURL=ON \
  -DCUDAToolkit_ROOT=/usr/local/cuda \
  -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc
cmake --build llama.cpp/build --config Release -j \
  --target llama-cli llama-mtmd-cli llama-server llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp/
cd .. 
cd ContextManagerV3
bash download_qwen_3.6_27b_q3.sh

