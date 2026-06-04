from enum import Enum


class MetadataToStringCollectionLabel(str, Enum):
    NEGATIVE_PROMPT = "negative_prompt"
    NEGATIVE_STYLE_PROMPT = "negative_style_prompt"
    POSITIVE_PROMPT = "positive_prompt"
    POSITIVE_STYLE_PROMPT = "positive_style_prompt"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
