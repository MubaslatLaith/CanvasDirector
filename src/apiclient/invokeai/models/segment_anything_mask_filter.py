from enum import Enum


class SegmentAnythingMaskFilter(str, Enum):
    ALL = "all"
    HIGHEST_BOX_SCORE = "highest_box_score"
    LARGEST = "largest"

    def __str__(self) -> str:
        return str(self.value)
