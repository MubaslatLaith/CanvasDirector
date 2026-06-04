from enum import Enum


class ImageToLatentsSD15SDXLColorCompensation(str, Enum):
    NONE = "None"
    SDXL = "SDXL"

    def __str__(self) -> str:
        return str(self.value)
