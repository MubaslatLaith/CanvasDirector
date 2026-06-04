from enum import Enum


class OpenAIImageGenerationInputFidelityType0(str, Enum):
    HIGH = "high"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
