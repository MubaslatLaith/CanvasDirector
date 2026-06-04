from enum import Enum


class UIComponent(str, Enum):
    NONE = "none"
    SLIDER = "slider"
    TEXTAREA = "textarea"

    def __str__(self) -> str:
        return str(self.value)
