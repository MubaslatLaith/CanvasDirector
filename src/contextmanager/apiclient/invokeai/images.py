

class Images:
    def __init__(self, request_client: RequestClient, auth_header_provider):
        self._request_client = request_client
        self._auth_header_provider = auth_header_provider

    def upload_image(self, image_path: str, board_id: str | None = None) -> dict[str, Any]:
        raise NotImplementedError

    def create_image_upload_entry(self, image_name: str, board_id: str | None = None) -> dict[str, Any]:
        raise NotImplementedError

    def list_images(self, offset: int = 0, limit: int = 50) -> list[dict[str, Any]]:
        raise NotImplementedError

    def get_image(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def get_images_by_names(self, image_names: list[str]) -> list[dict[str, Any]]:
        raise NotImplementedError

    def get_image_names(self, offset: int = 0, limit: int = 50) -> list[str]:
        raise NotImplementedError

    def get_image_metadata(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def get_image_workflow(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def get_image_urls(self, image_name: str) -> dict[str, Any]:
        raise NotImplementedError

    def get_full_image(self, image_name: str) -> bytes:
        raise NotImplementedError

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
