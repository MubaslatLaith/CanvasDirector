from enum import Enum


class ModelFormat(str, Enum):
    BNB_QUANTIZED_INT8B = "bnb_quantized_int8b"
    BNB_QUANTIZED_NF4B = "bnb_quantized_nf4b"
    CHECKPOINT = "checkpoint"
    DIFFUSERS = "diffusers"
    EMBEDDING_FILE = "embedding_file"
    EMBEDDING_FOLDER = "embedding_folder"
    EXTERNAL_API = "external_api"
    GGUF_QUANTIZED = "gguf_quantized"
    INVOKEAI = "invokeai"
    LYCORIS = "lycoris"
    OLIVE = "olive"
    OMI = "omi"
    ONNX = "onnx"
    QWEN3_ENCODER = "qwen3_encoder"
    QWEN_VL_ENCODER = "qwen_vl_encoder"
    T5_ENCODER = "t5_encoder"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
