from enum import Enum


class ConvertImageModeMode(str, Enum):
    CMYK = "CMYK"
    F = "F"
    HSV = "HSV"
    I = "I"
    L = "L"
    LAB = "LAB"
    RGB = "RGB"
    RGBA = "RGBA"
    YCBCR = "YCbCr"

    def __str__(self) -> str:
        return str(self.value)
