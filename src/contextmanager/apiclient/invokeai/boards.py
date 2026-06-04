
from typing import Any

from contextmanager.apiclient.request import RequestClient


class Boards:
    def __init__(self, request_client: RequestClient, auth_header_provider):
        self._request_client = request_client
        self._auth_header_provider = auth_header_provider

    def create_board(self, board_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def list_boards(
        self,
        *,
        all: bool = True,
        offset: int | None = None,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError

    def get_board(self, board_id: str) -> dict[str, Any]:
        raise NotImplementedError

    def update_board(
        self,
        board_id: str,
        *,
        board_name: str | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        raise NotImplementedError

    def delete_board(self, board_id: str) -> dict[str, Any] | None:
        raise NotImplementedError

    def list_board_image_names(self, board_id: str) -> list[str]:
        raise NotImplementedError

    def add_image_to_board(self, board_id: str, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def remove_image_from_board(self, board_id: str, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def add_images_to_board(
        self,
        board_id: str,
        image_names: list[str],
    ) -> dict[str, Any]:
        raise NotImplementedError

    def remove_images_from_board(
        self,
        board_id: str,
        image_names: list[str],
    ) -> dict[str, Any]:
        raise NotImplementedError



