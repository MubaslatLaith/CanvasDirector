from enum import Enum


class ModelRecordOrderBy(str, Enum):
    BASE = "base"
    CREATED_AT = "created_at"
    DEFAULT = "default"
    FORMAT = "format"
    NAME = "name"
    PATH = "path"
    SIZE = "size"
    TYPE = "type"
    UPDATED_AT = "updated_at"

    def __str__(self) -> str:
        return str(self.value)
