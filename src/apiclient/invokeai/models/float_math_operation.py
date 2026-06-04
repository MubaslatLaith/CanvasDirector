from enum import Enum


class FloatMathOperation(str, Enum):
    ABS = "ABS"
    ADD = "ADD"
    DIV = "DIV"
    EXP = "EXP"
    MAX = "MAX"
    MIN = "MIN"
    MUL = "MUL"
    SQRT = "SQRT"
    SUB = "SUB"

    def __str__(self) -> str:
        return str(self.value)
