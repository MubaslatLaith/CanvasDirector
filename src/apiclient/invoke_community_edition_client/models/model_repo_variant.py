from enum import Enum


class ModelRepoVariant(str, Enum):
    FLAX = "flax"
    FP16 = "fp16"
    FP32 = "fp32"
    ONNX = "onnx"
    OPENVINO = "openvino"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
