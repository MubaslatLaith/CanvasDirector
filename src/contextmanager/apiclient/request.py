import requests

from contextmanager.apiclient.types import APIResponse


class RequestClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None,
    ) -> APIResponse:

        response = requests.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            headers=headers,
            params=params,
            json=json,
        )

        response.raise_for_status()

        try:
            data = response.json()
        except Exception:
            data = response.text

        return APIResponse(
            status_code=response.status_code,
            data=data,
            headers=dict(response.headers),
        )
