from enum import Enum


class IntegerMathOperation(str, Enum):
    ABS = "ABS"
    ADD = "ADD"
    DIV = "DIV"
    EXP = "EXP"
    MAX = "MAX"
    MIN = "MIN"
    MOD = "MOD"
    MUL = "MUL"
    SUB = "SUB"

    def __str__(self) -> str:
        return str(self.value)
