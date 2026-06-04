from enum import Enum


class ClipVariantType(str, Enum):
    GIGANTIC = "gigantic"
    LARGE = "large"

    def __str__(self) -> str:
        return str(self.value)
