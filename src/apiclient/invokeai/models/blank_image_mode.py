from enum import Enum


class BlankImageMode(str, Enum):
    RGB = "RGB"
    RGBA = "RGBA"

    def __str__(self) -> str:
        return str(self.value)
