from enum import Enum


class ExternalModelPanelControlName(str, Enum):
    DIMENSIONS = "dimensions"
    REFERENCE_IMAGES = "reference_images"
    SEED = "seed"

    def __str__(self) -> str:
        return str(self.value)
