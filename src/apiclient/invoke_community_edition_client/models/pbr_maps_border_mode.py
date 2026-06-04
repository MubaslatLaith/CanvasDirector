from enum import Enum


class PBRMapsBorderMode(str, Enum):
    MIRROR = "mirror"
    NONE = "none"
    REPLICATE = "replicate"
    SEAMLESS = "seamless"

    def __str__(self) -> str:
        return str(self.value)
