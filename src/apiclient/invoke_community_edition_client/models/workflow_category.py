from enum import Enum


class WorkflowCategory(str, Enum):
    DEFAULT = "default"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
