import os

from contextmanager.apiclient.invokeai.client import InvokeAIClient


def main():
    email = "email@email.email"
    password = "weakpassword" 
    port = "9091"
    base_url = f"http://localhost:{port}" 
    


    client = InvokeAIClient(base_url)
    user = client.login(email, password)
    
    boards = client.boards.list_boards(all=True)
    print(board)
    import pdb; pdb.set_trace()
    #create board

    board_with_images = "6c48ce3b-d723-4f26-a0d3-9bbbf06e58c5" #"t0"
    image_names = client.boards.list_board_image_names(board_with_images).data
    print("image_names:", image_names)
    
    images = client.images.get_images_by_names(image_names).data
    print("images:", images)


    image = client.images.get_full_image(image_names[0]).data
    print("image_bytes_length:", len(image))


    

if __name__ == "__main__":
    main()
