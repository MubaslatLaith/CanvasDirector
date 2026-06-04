from enum import Enum


class MetadataToVAELabel(str, Enum):
    VAE = "vae"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
