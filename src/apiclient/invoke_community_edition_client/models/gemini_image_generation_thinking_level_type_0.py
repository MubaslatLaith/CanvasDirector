from enum import Enum


class GeminiImageGenerationThinkingLevelType0(str, Enum):
    HIGH = "high"
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
