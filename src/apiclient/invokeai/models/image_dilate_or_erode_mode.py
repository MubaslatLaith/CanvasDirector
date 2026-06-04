from enum import Enum


class ImageDilateOrErodeMode(str, Enum):
    DILATE = "Dilate"
    ERODE = "Erode"

    def __str__(self) -> str:
        return str(self.value)
