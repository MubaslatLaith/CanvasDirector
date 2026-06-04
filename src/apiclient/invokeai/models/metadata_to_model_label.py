from enum import Enum


class MetadataToModelLabel(str, Enum):
    MODEL = "model"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
