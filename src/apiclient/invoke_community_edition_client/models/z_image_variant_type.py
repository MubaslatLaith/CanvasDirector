from enum import Enum


class ZImageVariantType(str, Enum):
    TURBO = "turbo"
    ZBASE = "zbase"

    def __str__(self) -> str:
        return str(self.value)
