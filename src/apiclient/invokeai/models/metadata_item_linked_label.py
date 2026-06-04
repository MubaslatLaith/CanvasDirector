from enum import Enum


class MetadataItemLinkedLabel(str, Enum):
    CFG_RESCALE_MULTIPLIER = "cfg_rescale_multiplier"
    CFG_SCALE = "cfg_scale"
    CFG_SCALE_END_STEP = "cfg_scale_end_step"
    CFG_SCALE_START_STEP = "cfg_scale_start_step"
    CLIP_SKIP = "clip_skip"
    GUIDANCE = "guidance"
    HEIGHT = "height"
    MODEL = "model"
    NEGATIVE_PROMPT = "negative_prompt"
    NEGATIVE_STYLE_PROMPT = "negative_style_prompt"
    POSITIVE_PROMPT = "positive_prompt"
    POSITIVE_STYLE_PROMPT = "positive_style_prompt"
    SCHEDULER = "scheduler"
    SEAMLESS_X = "seamless_x"
    SEAMLESS_Y = "seamless_y"
    SEED = "seed"
    STEPS = "steps"
    VAE = "vae"
    VALUE_0 = "* CUSTOM LABEL *"
    WIDTH = "width"

    def __str__(self) -> str:
        return str(self.value)
