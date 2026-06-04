from enum import Enum


class MainModelDefaultSettingsVaePrecisionType0(str, Enum):
    FP16 = "fp16"
    FP32 = "fp32"

    def __str__(self) -> str:
        return str(self.value)
