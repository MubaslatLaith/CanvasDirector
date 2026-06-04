from enum import Enum


class DepthAnythingDepthEstimationModelSize(str, Enum):
    BASE = "base"
    LARGE = "large"
    SMALL = "small"
    SMALL_V2 = "small_v2"

    def __str__(self) -> str:
        return str(self.value)
