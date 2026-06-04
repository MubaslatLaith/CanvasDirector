from enum import Enum


class MetadataToFloatCollectionLabel(str, Enum):
    CFG_RESCALE_MULTIPLIER = "cfg_rescale_multiplier"
    CFG_SCALE = "cfg_scale"
    GUIDANCE = "guidance"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
