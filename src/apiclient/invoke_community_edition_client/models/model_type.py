from enum import Enum


class ModelType(str, Enum):
    CLIP_EMBED = "clip_embed"
    CLIP_VISION = "clip_vision"
    CONTROLNET = "controlnet"
    CONTROL_LORA = "control_lora"
    EMBEDDING = "embedding"
    EXTERNAL_IMAGE_GENERATOR = "external_image_generator"
    FLUX_REDUX = "flux_redux"
    IP_ADAPTER = "ip_adapter"
    LLAVA_ONEVISION = "llava_onevision"
    LORA = "lora"
    MAIN = "main"
    ONNX = "onnx"
    QWEN3_ENCODER = "qwen3_encoder"
    QWEN_VL_ENCODER = "qwen_vl_encoder"
    SIGLIP = "siglip"
    SPANDREL_IMAGE_TO_IMAGE = "spandrel_image_to_image"
    T2I_ADAPTER = "t2i_adapter"
    T5_ENCODER = "t5_encoder"
    TEXT_LLM = "text_llm"
    UNKNOWN = "unknown"
    VAE = "vae"

    def __str__(self) -> str:
        return str(self.value)
