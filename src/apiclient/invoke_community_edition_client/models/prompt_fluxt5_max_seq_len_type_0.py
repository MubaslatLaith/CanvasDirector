from enum import IntEnum


class PromptFLUXT5MaxSeqLenType0(IntEnum):
    VALUE_256 = 256
    VALUE_512 = 512

    def __str__(self) -> str:
        return str(self.value)
