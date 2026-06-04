from enum import Enum


class SaveImageGalleryFileExportFileFormat(str, Enum):
    JPG = "jpg"
    PNG = "png"
    WEBP = "webp"

    def __str__(self) -> str:
        return str(self.value)
