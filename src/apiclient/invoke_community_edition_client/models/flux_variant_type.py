from enum import Enum


class FluxVariantType(str, Enum):
    DEV = "dev"
    DEV_FILL = "dev_fill"
    SCHNELL = "schnell"

    def __str__(self) -> str:
        return str(self.value)
