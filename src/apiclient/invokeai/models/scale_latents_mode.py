from enum import Enum


class ScaleLatentsMode(str, Enum):
    AREA = "area"
    BICUBIC = "bicubic"
    BILINEAR = "bilinear"
    LINEAR = "linear"
    NEAREST = "nearest"
    NEAREST_EXACT = "nearest-exact"
    TRILINEAR = "trilinear"

    def __str__(self) -> str:
        return str(self.value)
