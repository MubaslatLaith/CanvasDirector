from typing import Any
from contextmanager.apiclient.request import RequestClient


class Boards:
    def __init__(self, request_client: RequestClient, auth_header_provider):
        self._request_client = request_client
        self._auth_header_provider = auth_header_provider


    def get_image_ids_by_board_name (self, board_name):
        """ assumes a single image per board"""
        board = self.get_board_by_name(board_name)
        board_id = board['board_id']
        image_names = self.list_board_image_names(board_id).data
        return image_names

    def create_board(self, board_name: str):
        return self._request_client.post("/api/v1/boards/", params={"board_name": board_name}, headers=self._auth_header_provider())

    def list_boards(self, all: bool = True, offset: int | None = None, limit: int | None = None):
        params = {"all": all}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._request_client.get("/api/v1/boards/", headers=self._auth_header_provider(), params=params)
    

    def get_board(self, board_id: str):
        return self._request_client.get(f"/api/v1/boards/{board_id}", headers=self._auth_header_provider())
    
    
    def get_board_by_name(self, board_name):
        response = self.list_boards(all=True)
        for board in response.data:
            if board["board_name"] == board_name:
                return board
        return None

    def update_board(
        self,
        board_id: str,
        board_name: str | None = None,
        archived: bool | None = None,
    ) -> dict[str, Any]:
        raise NotImplementedError
    
    def delete_board_by_name(self, board_name): 
        board = self.get_board_by_name(board_name)
        board_id = board['board_id']
        self.delete_board(board_id) 

    def delete_board(self, board_id: str) -> dict[str, Any] | None:
        return self._request_client.delete(f"/api/v1/boards/{board_id}", headers=self._auth_header_provider())
        #raise NotImplementedError

    def list_board_image_names(self, board_id: str):
        return self._request_client.get(f"/api/v1/boards/{board_id}/image_names", headers=self._auth_header_provider())
    
    def add_image_to_board(self, board_id: str, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def remove_image_from_board(self, board_id: str, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def add_images_to_board(self, board_id: str, image_names: list[str]) -> dict[str, Any]:
        raise NotImplementedError

    def remove_images_from_board(self, board_id: str, image_names: list[str]) -> dict[str, Any]:
        raise NotImplementedError
