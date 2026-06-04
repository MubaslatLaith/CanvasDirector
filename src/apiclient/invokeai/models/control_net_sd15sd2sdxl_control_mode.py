from enum import Enum


class ControlNetSD15SD2SDXLControlMode(str, Enum):
    BALANCED = "balanced"
    MORE_CONTROL = "more_control"
    MORE_PROMPT = "more_prompt"
    UNBALANCED = "unbalanced"

    def __str__(self) -> str:
        return str(self.value)
