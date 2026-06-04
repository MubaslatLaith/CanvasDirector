from enum import Enum


class FLUXDenoiseDypePreset(str, Enum):
    AREA = "area"
    AUTO = "auto"
    MANUAL = "manual"
    OFF = "off"
    VALUE_4 = "4k"

    def __str__(self) -> str:
        return str(self.value)
