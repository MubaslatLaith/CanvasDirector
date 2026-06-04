from enum import Enum


class Flux2VariantType(str, Enum):
    KLEIN_4B = "klein_4b"
    KLEIN_4B_BASE = "klein_4b_base"
    KLEIN_9B = "klein_9b"
    KLEIN_9B_BASE = "klein_9b_base"

    def __str__(self) -> str:
        return str(self.value)
