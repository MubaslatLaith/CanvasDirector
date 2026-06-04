import requests
import json
from contextmanager.apiclient.request import RequestClient
from contextmanager.apiclient.base import BackendClient
from contextmanager.apiclient.invokeai.boards import Boards
from contextmanager.apiclient.invokeai.images import Images



class InvokeAIClient(BackendClient):
    def __init__(self, base_url="http://localhost:9090"):
        self.base_url = base_url
        self.token = None
        self.request_client = RequestClient(base_url)
        self.boards = Boards(request_client=self.request_client, auth_header_provider=self._get_headers)
        self.images = Images(request_client=self.request_client, auth_header_provider=self._get_headers)

    def login(self, email, password, remember_me=False):
        response = self.request_client.request(
            "POST",
            "/api/v1/auth/login",
            json={
                "email": email,
                "password": password,
                "remember_me": remember_me,
            },
        )
        self.token = response.data["token"]
        return response.data["user"]



    def _get_headers(self):
        """Get headers with authentication token."""
        if not self.token:
            raise Exception("Not authenticated. Call login() first.")

        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

