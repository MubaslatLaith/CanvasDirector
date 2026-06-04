from enum import IntEnum


class LogLevel(IntEnum):
    VALUE_0 = 0
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_30 = 30
    VALUE_40 = 40
    VALUE_50 = 50

    def __str__(self) -> str:
        return str(self.value)
