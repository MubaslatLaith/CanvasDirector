import requests

from contextmanager.apiclient.types import APIResponse


class RequestClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
    

    def get(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request("POST", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request("DELETE", endpoint, **kwargs)

    def request(
        self,
        method: str,
        endpoint: str,
        *,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None,
        data: dict | None = None,
        files: dict | None = None
    ) -> APIResponse:

        response = requests.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            headers=headers,
            params=params,
            json=json,
            data=data,
            files=files,
            )
        
        print(response.status_code)
        print(response.text)
        #print(response.url)

        response.raise_for_status()

        try:
            data = response.json()
        except Exception:
            content_type = response.headers.get("content-type", "")
            if content_type.startswith("image/"):
                data = response.content
            else:
                data = response.text

        return APIResponse(
            status_code=response.status_code,
            data=data,
            headers=dict(response.headers),
        )
