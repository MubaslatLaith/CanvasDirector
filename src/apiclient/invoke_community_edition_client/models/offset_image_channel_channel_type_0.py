from enum import Enum


class OffsetImageChannelChannelType0(str, Enum):
    ALPHA_RGBA = "Alpha (RGBA)"
    A_LAB = "A (LAB)"
    BLACK_CMYK = "Black (CMYK)"
    BLUE_RGBA = "Blue (RGBA)"
    B_LAB = "B (LAB)"
    CB_YCBCR = "Cb (YCbCr)"
    CR_YCBCR = "Cr (YCbCr)"
    CYAN_CMYK = "Cyan (CMYK)"
    GREEN_RGBA = "Green (RGBA)"
    HUE_HSV = "Hue (HSV)"
    LUMINOSITY_LAB = "Luminosity (LAB)"
    MAGENTA_CMYK = "Magenta (CMYK)"
    RED_RGBA = "Red (RGBA)"
    SATURATION_HSV = "Saturation (HSV)"
    VALUE_HSV = "Value (HSV)"
    YELLOW_CMYK = "Yellow (CMYK)"
    Y_YCBCR = "Y (YCbCr)"

    def __str__(self) -> str:
        return str(self.value)
