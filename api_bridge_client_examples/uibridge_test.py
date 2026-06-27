from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage
from contextmanager.uiclient.invokeai.login_page import LoginPage
from contextmanager.uiclient.invokeai.generate_page import GeneratePage
from contextmanager.uiclient.invokeai.canvas_page import CanvasPage
from contextmanager.uiclient.invokeai.upscaling_page import UpscalingPage


from contextmanager.uiclient.invokeai.invoke_bridge import InvokeUIBridge



#INVOKE_URL = "http://localhost:5173" #
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
