from enum import Enum


class MetadataToIntegerLabel(str, Enum):
    CFG_SCALE_END_STEP = "cfg_scale_end_step"
    CFG_SCALE_START_STEP = "cfg_scale_start_step"
    CLIP_SKIP = "clip_skip"
    HEIGHT = "height"
    SEED = "seed"
    STEPS = "steps"
    VALUE_0 = "* CUSTOM LABEL *"
    WIDTH = "width"

    def __str__(self) -> str:
        return str(self.value)
