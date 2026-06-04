from enum import Enum


class PromptQwenImageQuantization(str, Enum):
    INT8 = "int8"
    NF4 = "nf4"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
