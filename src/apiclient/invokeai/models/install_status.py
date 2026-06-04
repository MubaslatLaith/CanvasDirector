from enum import Enum


class InstallStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DOWNLOADING = "downloading"
    DOWNLOADS_DONE = "downloads_done"
    ERROR = "error"
    PAUSED = "paused"
    RUNNING = "running"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
