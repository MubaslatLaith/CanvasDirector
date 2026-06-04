import os

from contextmanager.apiclient.invokeai.client import InvokeAIClient


def main():
    email = "laithmbt@gmail.com"
    password = "123" 
    port = "9091"
    base_url = f"http://localhost:{port}" 
    


    client = InvokeAIClient(base_url)

    user = client.login(email, password)


    print("Login successful")
    print(f"Display Name: {user.get('display_name')}")
    print(f"Email: {user.get('email')}")

    headers = client._get_headers()

    print("\nAuth header generated successfully")
    print(f"Authorization: {headers['Authorization'][:25]}...")


if __name__ == "__main__":
    main()
