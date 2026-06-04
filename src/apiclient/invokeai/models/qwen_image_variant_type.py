from enum import Enum


class QwenImageVariantType(str, Enum):
    EDIT = "edit"
    GENERATE = "generate"

    def __str__(self) -> str:
        return str(self.value)
