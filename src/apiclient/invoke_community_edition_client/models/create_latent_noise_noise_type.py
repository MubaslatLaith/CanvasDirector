from enum import Enum


class CreateLatentNoiseNoiseType(str, Enum):
    ANIMA = "Anima"
    COGVIEW4 = "CogView4"
    FLUX = "FLUX"
    FLUX_2 = "FLUX.2"
    SD = "SD"
    SD3 = "SD3"
    Z_IMAGE = "Z-Image"

    def __str__(self) -> str:
        return str(self.value)
