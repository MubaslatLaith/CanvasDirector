from enum import Enum


class FLUXDenoiseScheduler(str, Enum):
    EULER = "euler"
    HEUN = "heun"
    LCM = "lcm"

    def __str__(self) -> str:
        return str(self.value)
