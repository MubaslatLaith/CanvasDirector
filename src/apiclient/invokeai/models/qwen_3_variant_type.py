from enum import Enum


class Qwen3VariantType(str, Enum):
    QWEN3_06B = "qwen3_06b"
    QWEN3_4B = "qwen3_4b"
    QWEN3_8B = "qwen3_8b"

    def __str__(self) -> str:
        return str(self.value)
