from enum import Enum


class IPAdapterRecallParameterImageInfluenceType0(str, Enum):
    HIGH = "high"
    HIGHEST = "highest"
    LOW = "low"
    LOWEST = "lowest"
    MEDIUM = "medium"

    def __str__(self) -> str:
        return str(self.value)
