from enum import Enum


class BoardRecordOrderBy(str, Enum):
    BOARD_NAME = "board_name"
    CREATED_AT = "created_at"

    def __str__(self) -> str:
        return str(self.value)
