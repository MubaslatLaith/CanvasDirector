from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage
from contextmanager.uiclient.invokeai.login_page import LoginPage
from contextmanager.uiclient.invokeai.generate_page import GeneratePage
from contextmanager.uiclient.invokeai.canvas_page import CanvasPage
from contextmanager.uiclient.invokeai.upscaling_page import UpscalingPage




INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword" 




def main():
    snapshot_path = Path("ui_snapshots/base_page_snapshot.json")

    with sync_playwright() as p:
        #init 
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        #login 
        login_page = LoginPage(page)
        login_page.select_page(INVOKE_URL)
        login_page.deselect_remember_me()
        login_page.login(USERNAME, PASSWORD) 
        login_successful = login_page.validate_login()   

        #canvas_page = CanvasPage(page)
        
        #canvas_page.select_page()


        #TODO add the following methods 
        #1 init image_to_edit_board (if it does not exist) 
        #2 assign image to edit: move image to image_to_edit_board
        #3 assign mask to edit: generate and upload mask to image_to_edit_board (upload as an asset) 
        
        
        #1 init image_to_edit_board (if it does not exist)
        #2 assign image to edit / for now assigned manually (manually placed in image_to_edit_board) 
        #3 assign mask to edit / for now assigned manually (manually placed in image_to_edit_board assets)
        
        
        generate_page = GeneratePage(page) 
        canvas_page = CanvasPage(page)
        
        generate_page.select_page() 
        board_name = "image_to_edit_board"
        generate_page.select_board(board_name)
        #TODO select board: image_to_edit 
        canvas_page.select_page() 
        #TODO go to edit mode (click edit) - No need 

        #TODO select board - images 
        #TODO right click - as raster layer
        #TODO delete empty mask 


        #TODO select board - assets 
        #TODO select mask asset  - No need (automatically selected by prev step) 
        #TODO right click 

        

        """
        edit_prompt = "fix hands"
        canvas_page.update_prompt(prompt = edit_prompt)

        
        invoke = generate_page.page.get_by_role("button", name="Invoke", exact=True)
        
        canvas_page.screenshot_page("generator_page_after_update_prompt.png")        
        canvas_page.wait_until_dom_stable() 
    
        browser.close()
        """

if __name__ == "__main__":
    main()
