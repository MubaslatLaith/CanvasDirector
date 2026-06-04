from enum import Enum


class ImageLayerBlendColorSpace(str, Enum):
    HSL_RGB = "HSL (RGB)"
    HSV_RGB = "HSV (RGB)"
    LCH_CIELAB = "LCh (CIELab)"
    LINEAR_RGB = "Linear RGB"
    OKHSL = "Okhsl"
    OKHSV = "Okhsv"
    OKLCH_OKLAB = "Oklch (Oklab)"
    RGB = "RGB"

    def __str__(self) -> str:
        return str(self.value)
