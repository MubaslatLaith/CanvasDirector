from enum import Enum


class IPAdapterSD15SDXLMethod(str, Enum):
    COMPOSITION = "composition"
    FULL = "full"
    STYLE = "style"
    STYLE_PRECISE = "style_precise"
    STYLE_STRONG = "style_strong"

    def __str__(self) -> str:
        return str(self.value)
