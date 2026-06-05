import os

from contextmanager.apiclient.invokeai.client import InvokeAIClient


def main():
    email = "email@email.email"
    password = "weakpassword" 
    port = "9091"
    base_url = f"http://localhost:{port}" 
    


    client = InvokeAIClient(base_url)
    user = client.login(email, password)







if __name__ == "__main__":
    main()
