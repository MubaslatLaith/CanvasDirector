from enum import Enum


class SubModelType(str, Enum):
    SAFETY_CHECKER = "safety_checker"
    SCHEDULER = "scheduler"
    TEXT_ENCODER = "text_encoder"
    TEXT_ENCODER_2 = "text_encoder_2"
    TEXT_ENCODER_3 = "text_encoder_3"
    TOKENIZER = "tokenizer"
    TOKENIZER_2 = "tokenizer_2"
    TOKENIZER_3 = "tokenizer_3"
    TRANSFORMER = "transformer"
    UNET = "unet"
    VAE = "vae"
    VAE_DECODER = "vae_decoder"
    VAE_ENCODER = "vae_encoder"

    def __str__(self) -> str:
        return str(self.value)
