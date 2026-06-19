from typing import Any
from contextmanager.apiclient.request import RequestClient
from pathlib import Path

class Images:
    def __init__(self, request_client: RequestClient, auth_header_provider):
        self._request_client = request_client
        self._auth_header_provider = auth_header_provider
    
    def get_image_url(self, image_name: str) -> str:
        return f"{self._request_client.base_url.rstrip('/')}/api/v1/images/i/{image_name}/full"
    
    def assign_image(self, image_id: str, board_id: str): 
        response =  self._request_client.post("/api/v1/board_images/", json={"board_id": board_id, "image_name": image_id}, headers=self._auth_header_provider())
    
    def upload_image(self, image_path: str, board_id: str | None = None, image_category: str = "general") -> dict[str, Any]:
        params = {
                "image_category": image_category,
                "is_intermediate": False,
                }
        if board_id is not None:
            params["board_id"] = board_id
        
        headers = self._auth_header_provider()
        headers.pop("Content-Type", None)
        
        with open(image_path, "rb") as f:
            #files = {"file": f}
            files = {"file": (Path(image_path).name, f, "image/png")}
            return self._request_client.post("/api/v1/images/upload", params=params, files=files, headers=headers) 



    def create_image_upload_entry(self, image_name: str, board_id: str | None = None) -> dict[str, Any]:
        raise NotImplementedError

    def list_images(self, offset: int = 0, limit: int = 50) -> list[dict[str, Any]]:
        raise NotImplementedError

    def get_image(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def get_images_by_names(self, image_names: list[str]):
        return self._request_client.get("/api/v1/images/", headers=self._auth_header_provider(), params={"image_names": image_names}) 

    def get_image_names(self, offset: int = 0, limit: int = 50) -> list[str]:
        raise NotImplementedError

    def get_image_metadata(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def get_image_workflow(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError


    def get_full_image(self, image_name: str):
        return self._request_client.get(f"/api/v1/images/i/{image_name}/full", headers=self._auth_header_provider()) 
    
    def get_thumbnail(self, image_name: str) -> bytes:
        raise NotImplementedError

    def image_exists(self, image_name: str) -> bool:
        raise NotImplementedError

    def update_image(self, image_name: str, **kwargs) -> dict[str, Any]:
        raise NotImplementedError

    def star_images(self, image_names: list[str]) -> dict[str, Any]:
        raise NotImplementedError

    def unstar_images(self, image_names: list[str]) -> dict[str, Any]:
        raise NotImplementedError

    def delete_image(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def delete_images(self, image_names: list[str]) -> dict[str, Any]:
        raise NotImplementedError

    def delete_uncategorized_images(self) -> dict[str, Any]:
        raise NotImplementedError

    def request_bulk_download(self, image_names: list[str]) -> dict[str, Any]:
        raise NotImplementedError

    def get_bulk_download_item(self, bulk_download_item_name: str) -> bytes:
        raise NotImplementedError

    def get_intermediates_count(self) -> int:
        raise NotImplementedError

    def clear_intermediates(self) -> dict[str, Any]:
        raise NotImplementedError
