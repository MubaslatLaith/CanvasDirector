from enum import Enum


class UpdateAppGenerationSettingsRequestImageSubfolderStrategy(str, Enum):
    DATE = "date"
    FLAT = "flat"
    HASH = "hash"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
