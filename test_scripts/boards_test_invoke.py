import os

from contextmanager.apiclient.invokeai.client import InvokeAIClient


def main():
    email = "email@email.email"
    password = "weakpassword" 
    port = "9091"
    base_url = f"http://localhost:{port}" 
    


    client = InvokeAIClient(base_url)
    user = client.login(email, password)
    
    #create board
    created_board_0 = client.boards.create_board("api-test-board-0").data
    created_board_1 = client.boards.create_board("api-test-board-1").data

    board_id_0 = created_board_0["board_id"]
    board_id_1 = created_board_1["board_id"]
    
    
    #list boards
    boards = client.boards.list_boards().data
    print("boards:", boards)
    

    
    board = client.boards.get_board(board_id_0).data
    print("board:", board)
    

    board_with_images = "6c48ce3b-d723-4f26-a0d3-9bbbf06e58c5" #"t0"
    image_names = client.boards.list_board_image_names(board_with_images).data
    print("image_names:", image_names)


    
    #updated_board = client.boards.update_board(board_id, board_name="api-test-board-updated")
    #print("updated_board:", updated_board)
    """
    #archived_board = client.boards.update_board(board_id, archived=True)
    #print("archived_board:", archived_board)
    #unarchived_board = client.boards.update_board(board_id, archived=False)
    #print("unarchived_board:", unarchived_board)
        
    #deleted_board = client.boards.delete_board(board_id)
    #print("deleted_board:", deleted_board)

    """

if __name__ == "__main__":
    main()
