import requests
import json

class InvokeAIClient:
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

    def get_boards(self):
        """Get user's boards."""
        url = f"{self.base_url}/api/v1/boards/"
        response = requests.get(url, headers=self._get_headers(),
                                params={"all": True})
        
        print("STATUS:", response.status_code)

        print("BODY:", response.text)
        response.raise_for_status()
        return response.json()

    def create_board(self, board_name):
        """Create a new board."""
        url = f"{self.base_url}/api/v1/boards/"
        response = requests.post(
            url,
            params={"board_name": board_name},
            headers=self._get_headers()
        )
        response.raise_for_status()
        return response.json()

    def logout(self):
        """Logout and clear token."""
        url = f"{self.base_url}/api/v1/auth/logout"
        response = requests.post(url, headers=self._get_headers())
        self.token = None
        return response.json()

# Usage
username = "laithmbt@gmail.com"
password = "123"
port = "9091"
base_url = f"http://localhost:{port}"

client = InvokeAIClient(base_url)

user = client.login(username, password)  #"user@example.com", "SecurePassword123")
print(f"Logged in as: {user['display_name']}")

boards = client.get_boards()
#print(f"User has {len(boards['items'])} boards")
print(f"User has {len(boards)} boards")

for board in boards:

    print(f"- {board['board_name']} ({board['board_id']}) images={board['image_count']}")



new_board = client.create_board("My New Board")
print(f"Created board: {new_board['board_name']}")

client.logout()
