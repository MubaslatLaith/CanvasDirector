from enum import Enum


class AlibabaCloudDashScopeImageGenerationMode(str, Enum):
    IMG2IMG = "img2img"
    INPAINT = "inpaint"
    TXT2IMG = "txt2img"

    def __str__(self) -> str:
        return str(self.value)
