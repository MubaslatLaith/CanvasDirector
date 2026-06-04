from enum import Enum


class WorkflowRecordOrderBy(str, Enum):
    CREATED_AT = "created_at"
    IS_PUBLIC = "is_public"
    NAME = "name"
    OPENED_AT = "opened_at"
    UPDATED_AT = "updated_at"

    def __str__(self) -> str:
        return str(self.value)
