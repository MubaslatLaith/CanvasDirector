from enum import Enum


class MetadataToSDXLModelLabel(str, Enum):
    MODEL = "model"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
