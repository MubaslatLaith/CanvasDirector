from enum import Enum


class MetadataToBoolLabel(str, Enum):
    SEAMLESS_X = "seamless_x"
    SEAMLESS_Y = "seamless_y"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
