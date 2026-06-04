from enum import Enum


class Classification(str, Enum):
    BETA = "beta"
    DEPRECATED = "deprecated"
    INTERNAL = "internal"
    PROTOTYPE = "prototype"
    SPECIAL = "special"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
