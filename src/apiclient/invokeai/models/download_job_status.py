from enum import Enum


class DownloadJobStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    ERROR = "error"
    PAUSED = "paused"
    RUNNING = "running"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
