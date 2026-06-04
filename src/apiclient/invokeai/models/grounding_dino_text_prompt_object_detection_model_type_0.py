from enum import Enum


class GroundingDINOTextPromptObjectDetectionModelType0(str, Enum):
    GROUNDING_DINO_BASE = "grounding-dino-base"
    GROUNDING_DINO_TINY = "grounding-dino-tiny"

    def __str__(self) -> str:
        return str(self.value)
