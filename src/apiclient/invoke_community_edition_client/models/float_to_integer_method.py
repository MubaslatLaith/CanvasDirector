from enum import Enum


class FloatToIntegerMethod(str, Enum):
    CEILING = "Ceiling"
    FLOOR = "Floor"
    NEAREST = "Nearest"
    TRUNCATE = "Truncate"

    def __str__(self) -> str:
        return str(self.value)
