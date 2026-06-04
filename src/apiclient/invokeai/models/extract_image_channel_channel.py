from enum import Enum


class ExtractImageChannelChannel(str, Enum):
    A = "A"
    B = "B"
    G = "G"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
