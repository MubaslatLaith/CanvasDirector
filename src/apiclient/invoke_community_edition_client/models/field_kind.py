from enum import Enum


class FieldKind(str, Enum):
    INPUT = "input"
    INTERNAL = "internal"
    NODE_ATTRIBUTE = "node_attribute"
    OUTPUT = "output"

    def __str__(self) -> str:
        return str(self.value)
