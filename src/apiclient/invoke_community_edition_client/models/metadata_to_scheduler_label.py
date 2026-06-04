from enum import Enum


class MetadataToSchedulerLabel(str, Enum):
    SCHEDULER = "scheduler"
    VALUE_0 = "* CUSTOM LABEL *"

    def __str__(self) -> str:
        return str(self.value)
