from enum import Enum


class BoardVisibility(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"
    SHARED = "shared"

    def __str__(self) -> str:
        return str(self.value)
