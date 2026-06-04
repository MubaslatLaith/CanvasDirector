from enum import Enum


class FLUXControlNetResizeMode(str, Enum):
    CROP_RESIZE = "crop_resize"
    FILL_RESIZE = "fill_resize"
    JUST_RESIZE = "just_resize"
    JUST_RESIZE_SIMPLE = "just_resize_simple"

    def __str__(self) -> str:
        return str(self.value)
