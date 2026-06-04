from enum import Enum


class SegmentAnythingModelType0(str, Enum):
    SEGMENT_ANYTHING_2_BASE = "segment-anything-2-base"
    SEGMENT_ANYTHING_2_LARGE = "segment-anything-2-large"
    SEGMENT_ANYTHING_2_SMALL = "segment-anything-2-small"
    SEGMENT_ANYTHING_2_TINY = "segment-anything-2-tiny"
    SEGMENT_ANYTHING_BASE = "segment-anything-base"
    SEGMENT_ANYTHING_HUGE = "segment-anything-huge"
    SEGMENT_ANYTHING_LARGE = "segment-anything-large"

    def __str__(self) -> str:
        return str(self.value)
