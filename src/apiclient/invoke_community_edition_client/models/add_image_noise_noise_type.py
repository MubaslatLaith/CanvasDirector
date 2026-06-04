from enum import Enum


class AddImageNoiseNoiseType(str, Enum):
    GAUSSIAN = "gaussian"
    SALT_AND_PEPPER = "salt_and_pepper"

    def __str__(self) -> str:
        return str(self.value)
