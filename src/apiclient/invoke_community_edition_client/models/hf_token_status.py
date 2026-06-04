from enum import Enum


class HFTokenStatus(str, Enum):
    INVALID = "invalid"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
