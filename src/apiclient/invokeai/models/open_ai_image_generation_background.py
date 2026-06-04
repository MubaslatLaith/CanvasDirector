from enum import Enum


class OpenAIImageGenerationBackground(str, Enum):
    AUTO = "auto"
    OPAQUE = "opaque"
    TRANSPARENT = "transparent"

    def __str__(self) -> str:
        return str(self.value)
