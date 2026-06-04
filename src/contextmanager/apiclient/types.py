from dataclasses import dataclass
from typing import Any


@dataclass
class APIResponse:
    status_code: int
    data: Any
    headers: dict[str, str]


@dataclass
class APIError:
    status_code: int
    message: str
    details: Any | None = None
