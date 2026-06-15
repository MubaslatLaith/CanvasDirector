from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage
from contextmanager.uiclient.invokeai.login_page import LoginPage
from contextmanager.uiclient.invokeai.generate_page import GeneratePage
from contextmanager.uiclient.invokeai.canvas_page import CanvasPage
from contextmanager.uiclient.invokeai.upscaling_page import UpscalingPage


from contextmanager.uiclient.invokeai.invoke_bridge import InvokeUIBridge
from contextmanager.apiclient.invokeai.client import InvokeAIClient

INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword" 

def main():
    # api client setup
    api_client = InvokeAIClient(INVOKE_URL)
    user = api_client.login(USERNAME, PASSWORD)
    
    # bridge client setup 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.screenshot_page("bridge.png")
        login_page.select_page(INVOKE_URL)
        login_page.deselect_remember_me()
        login_page.login(USERNAME, PASSWORD)
        login_successful = login_page.validate_login()
        canvas_page = CanvasPage(page)
        canvas_page.select_page()
        bridge = InvokeUIBridge(page)

    

        # start with the image in input_board_name (should contain a single image for now) 

        input_board_name = "My Board" 
        mask_path = "/workspace/invokeai/test_mask.png"  
        image_to_edit_id = api_client.boards.get_image_ids_by_board_name (input_board_name) 
        image_to_edit_id = image_to_edit_id[0] 
        print(image_to_edit_id)   

        # create job boards 

        job_id = 0 
        
        board_name_image_to_edit = f'inpaint_image_job_{job_id}' 
        board_name_mask_to_edit = f'inpaint_mask_job_{job_id}' 
        board_name_output = f'inpaint_output_job_{job_id}'

        api_client.boards.create_board(board_name_image_to_edit) 
        api_client.boards.create_board(board_name_mask_to_edit) 
        api_client.boards.create_board(board_name_output) 

        board_id_image_to_edit = api_client.boards.get_board_by_name(board_name_image_to_edit)['board_id'] 
        board_id_mask_to_edit = api_client.boards.get_board_by_name(board_name_mask_to_edit)['board_id']
        board_id_name_to_edit = api_client.boards.get_board_by_name(board_name_output)['board_id']


        # assign image to board 
        #api_client.images.assign_image(image_id = image_to_edit_id, board_id = board_id_image_to_edit)
        # upload mask to board 
        api_client.images.upload_image(image_path = mask_path, board_id = board_id_mask_to_edit, image_category = "mask") 

        
        # reset canvas
        bridge.reset_canvas() 
        
        #TODO modify to take board name
        image_name = image_to_edit_id#api_client. 
        mask_name = api_client.boards.get_image_ids_by_board_name(board_name_mask_to_edit)[0] 

        bridge.create_canvas_entity_from_image_name("raster_layer", image_name)
        bridge.create_canvas_entity_from_image_name("inpaint_mask", mask_name )


        with bridge.wait_client_state_saved():
            pass 




        return 




        

    # cleanup 
    """ 
    api_client.boards.delete_board_by_name(board_name_image_to_edit)
    api_client.boards.delete_board_by_name(board_name_mask_to_edit)
    api_client.boards.delete_board_by_name(board_name_output) 
    """


    

    image_to_edit_id = api_client.boards.get_image_ids_by_board_name (board_name_image_to_edit)
    mask_to_edit_id = api_client.boards.get_image_ids_by_board_name (board_name_mask_to_edit) 

    print(image_to_edit_id)
    print(mask_to_edit_id)



    return 
    #board = api_client.boards.get_board_by_name(board_name)
    #print(board)
    #board_id = board['board_id']
    #image_names = api_client.boards.list_board_image_names(board_id).data
   






    #print(image_names) 
    with sync_playwright() as p:











        return 
        #init 
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
         
        #login 
        login_page = LoginPage(page)
        
        login_page.screenshot_page("bridge.png")

        login_page.select_page(INVOKE_URL)
        login_page.deselect_remember_me()
        login_page.login(USERNAME, PASSWORD) 
        login_successful = login_page.validate_login()   
       
        
        canvas_page = CanvasPage(page) 
        canvas_page.select_page() 
            

        bridge = InvokeUIBridge(page)
        import time 
        #bridge.create_canvas_entity_from_selected_image("raster_layer")
        params = bridge.get_params()
        start = time.perf_counter()
        #TODO replace tab/board selection with add entity from image id
        canvas_page.page.get_by_test_id("images-tab").click()
        bridge.create_canvas_entity_from_selected_image("raster_layer") 
        canvas_page.page.get_by_test_id("assets-tab").click()
        canvas_page.wait_until_dom_stable()
        bridge.create_canvas_entity_from_selected_image("inpaint_mask") 
        bridge.set_parameter("steps", 7)


        with bridge.wait_client_state_saved():
            bridge.set_parameter("positive_prompt", "fix hand") #"a cat wearing armor")
        
        bridge.invoke() 
        
        
        with bridge.wait_client_state_saved():
            bridge.canvas_acceptSelected() 

        #with bridge.wait_client_state_saved():
        #    pass

        #with bridge.wait_client_state_saved():
        #    pass 
            #    bridge.invoke() 
            #aa = bridge.page.evaluate("window.__invokeBridge.queue.invoke()")
            #print(aa)

        #canvas_page.select_board("image_to_edit_board") 
        elapsed = time.perf_counter() - start

        print(f"client_state request finished in {elapsed:.3f}s")



if __name__ == "__main__":
    main()
