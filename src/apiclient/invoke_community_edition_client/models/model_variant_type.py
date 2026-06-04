from enum import Enum


class ModelVariantType(str, Enum):
    DEPTH = "depth"
    INPAINT = "inpaint"
    NORMAL = "normal"

    def __str__(self) -> str:
        return str(self.value)
