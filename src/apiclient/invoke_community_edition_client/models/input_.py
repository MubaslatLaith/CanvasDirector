from enum import Enum


class Input(str, Enum):
    ANY = "any"
    CONNECTION = "connection"
    DIRECT = "direct"

    def __str__(self) -> str:
        return str(self.value)
