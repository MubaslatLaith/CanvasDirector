from enum import Enum


class IPAdapterRecallParameterMethodType0(str, Enum):
    COMPOSITION = "composition"
    FULL = "full"
    STYLE = "style"

    def __str__(self) -> str:
        return str(self.value)
