# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

model_name = 'Qwen3.5-9B-GGUF'  
repo_id = f'unsloth/{model_name}'
local_dir = f'/workspace/{model_name}'
quant = '*Q8_0*'


snapshot_download(
    repo_id = repo_id, #"unsloth/Devstral-2-123B-Instruct-2512-GGUF",
    local_dir = local_dir, #"Devstral-2-123B-Instruct-2512-GGUF",
    allow_patterns = [quant, "*mmproj-F16*"], 
    #allow_patterns = ["*UD-Q2_K_XL*", "*mmproj-F16*"],
)
