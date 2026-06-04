from enum import Enum


class FLUXReduxDownsamplingFunction(str, Enum):
    AREA = "area"
    BICUBIC = "bicubic"
    BILINEAR = "bilinear"
    NEAREST = "nearest"
    NEAREST_EXACT = "nearest-exact"

    def __str__(self) -> str:
        return str(self.value)
