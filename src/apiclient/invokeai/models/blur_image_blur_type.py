from enum import Enum


class BlurImageBlurType(str, Enum):
    BOX = "box"
    GAUSSIAN = "gaussian"

    def __str__(self) -> str:
        return str(self.value)
