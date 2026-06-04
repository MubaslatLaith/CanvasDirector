from enum import Enum


class ResizeImageResampleMode(str, Enum):
    BICUBIC = "bicubic"
    BILINEAR = "bilinear"
    BOX = "box"
    HAMMING = "hamming"
    LANCZOS = "lanczos"
    NEAREST = "nearest"

    def __str__(self) -> str:
        return str(self.value)
