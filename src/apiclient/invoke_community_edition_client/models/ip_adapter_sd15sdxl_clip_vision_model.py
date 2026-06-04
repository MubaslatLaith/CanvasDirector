from enum import Enum


class IPAdapterSD15SDXLClipVisionModel(str, Enum):
    VIT_G = "ViT-G"
    VIT_H = "ViT-H"
    VIT_L = "ViT-L"

    def __str__(self) -> str:
        return str(self.value)
