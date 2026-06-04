from enum import Enum


class DenoiseAnimaScheduler(str, Enum):
    DPMPP_2M = "dpmpp_2m"
    DPMPP_2M_SDE = "dpmpp_2m_sde"
    ER_SDE = "er_sde"
    EULER = "euler"
    HEUN = "heun"
    LCM = "lcm"

    def __str__(self) -> str:
        return str(self.value)
