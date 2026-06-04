from enum import Enum


class ModelSourceType(str, Enum):
    EXTERNAL = "external"
    HF_REPO_ID = "hf_repo_id"
    PATH = "path"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
