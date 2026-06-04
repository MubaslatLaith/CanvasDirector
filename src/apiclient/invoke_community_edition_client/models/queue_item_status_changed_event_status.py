from enum import Enum


class QueueItemStatusChangedEventStatus(str, Enum):
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
