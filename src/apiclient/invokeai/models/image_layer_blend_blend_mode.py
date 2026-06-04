from enum import Enum


class ImageLayerBlendBlendMode(str, Enum):
    COLOR = "Color"
    COLOR_BURN = "Color Burn"
    COLOR_DODGE = "Color Dodge"
    DARKEN_ONLY = "Darken Only"
    DARKEN_ONLY_EAL = "Darken Only (EAL)"
    DIFFERENCE = "Difference"
    DIVIDE = "Divide"
    HARD_LIGHT = "Hard Light"
    HUE = "Hue"
    LIGHTEN_ONLY = "Lighten Only"
    LIGHTEN_ONLY_EAL = "Lighten Only (EAL)"
    LINEAR_BURN = "Linear Burn"
    LINEAR_DODGE_ADD = "Linear Dodge (Add)"
    LINEAR_LIGHT = "Linear Light"
    LUMINOSITY = "Luminosity"
    MULTIPLY = "Multiply"
    NORMAL = "Normal"
    OVERLAY = "Overlay"
    SATURATION = "Saturation"
    SCREEN = "Screen"
    SOFT_LIGHT = "Soft Light"
    SUBTRACT = "Subtract"
    VIVID_LIGHT = "Vivid Light"

    def __str__(self) -> str:
        return str(self.value)
