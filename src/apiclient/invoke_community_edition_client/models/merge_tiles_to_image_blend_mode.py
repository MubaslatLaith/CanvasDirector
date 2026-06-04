from enum import Enum


class MergeTilesToImageBlendMode(str, Enum):
    LINEAR = "Linear"
    SEAM = "Seam"

    def __str__(self) -> str:
        return str(self.value)
