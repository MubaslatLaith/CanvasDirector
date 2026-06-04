import requests
import json
from contextmanager.apiclient.base import BackendClient


class InvokeAIClient(BackendClient):
    def __init__(self, base_url="http://localhost:9090"):
        self.base_url = base_url
        self.token = None

    def login(self, email, password, remember_me=False):
        """Authenticate and store token."""
        url = f"{self.base_url}/api/v1/auth/login"
        payload = {
            "email": email,
            "password": password,
            "remember_me": remember_me
        }

        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()
        self.token = data["token"]
        return data["user"]

    def _get_headers(self):
        """Get headers with authentication token."""
        if not self.token:
            raise Exception("Not authenticated. Call login() first.")

        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

