from enum import Enum


class CreateGradientMaskCoherenceMode(str, Enum):
    BOX_BLUR = "Box Blur"
    GAUSSIAN_BLUR = "Gaussian Blur"
    STAGED = "Staged"

    def __str__(self) -> str:
        return str(self.value)
