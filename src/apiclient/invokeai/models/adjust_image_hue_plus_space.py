from enum import Enum


class AdjustImageHuePlusSpace(str, Enum):
    HSV_HSL_RGB = "HSV / HSL / RGB"
    OKHSL = "Okhsl"
    OKHSV = "Okhsv"
    VALUE_3 = "*Oklch / Oklab"
    VALUE_4 = "*LCh / CIELab"
    VALUE_5 = "*UPLab (w/CIELab_to_UPLab.icc)"

    def __str__(self) -> str:
        return str(self.value)
