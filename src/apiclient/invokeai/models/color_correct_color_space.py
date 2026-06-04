from enum import Enum


class ColorCorrectColorSpace(str, Enum):
    RGB = "RGB"
    YCBCR = "YCbCr"
    YCBCR_CHROMA = "YCbCr-Chroma"
    YCBCR_LUMA = "YCbCr-Luma"

    def __str__(self) -> str:
        return str(self.value)
