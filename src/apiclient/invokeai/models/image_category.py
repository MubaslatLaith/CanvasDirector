from enum import Enum


class ImageCategory(str, Enum):
    CONTROL = "control"
    GENERAL = "general"
    MASK = "mask"
    OTHER = "other"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
