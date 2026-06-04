from enum import Enum


class ControlNetRecallParameterControlModeType0(str, Enum):
    BALANCED = "balanced"
    MORE_CONTROL = "more_control"
    MORE_PROMPT = "more_prompt"

    def __str__(self) -> str:
        return str(self.value)
