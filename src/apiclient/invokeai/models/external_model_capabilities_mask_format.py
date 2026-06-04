from enum import Enum


class ExternalModelCapabilitiesMaskFormat(str, Enum):
    ALPHA = "alpha"
    BINARY = "binary"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
