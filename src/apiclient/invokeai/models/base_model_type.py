from enum import Enum


class BaseModelType(str, Enum):
    ANIMA = "anima"
    ANY = "any"
    COGVIEW4 = "cogview4"
    EXTERNAL = "external"
    FLUX = "flux"
    FLUX2 = "flux2"
    QWEN_IMAGE = "qwen-image"
    SDXL = "sdxl"
    SDXL_REFINER = "sdxl-refiner"
    SD_1 = "sd-1"
    SD_2 = "sd-2"
    SD_3 = "sd-3"
    UNKNOWN = "unknown"
    Z_IMAGE = "z-image"

    def __str__(self) -> str:
        return str(self.value)
