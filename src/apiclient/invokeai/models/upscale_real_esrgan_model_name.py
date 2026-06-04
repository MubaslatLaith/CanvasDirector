from enum import Enum


class UpscaleRealESRGANModelName(str, Enum):
    ESRGAN_SRX4_DF2KOST_OFFICIAL_FF704C30_PTH = "ESRGAN_SRx4_DF2KOST_official-ff704c30.pth"
    REALESRGAN_X2PLUS_PTH = "RealESRGAN_x2plus.pth"
    REALESRGAN_X4PLUS_ANIME_6B_PTH = "RealESRGAN_x4plus_anime_6B.pth"
    REALESRGAN_X4PLUS_PTH = "RealESRGAN_x4plus.pth"

    def __str__(self) -> str:
        return str(self.value)
