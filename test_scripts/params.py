from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage
from contextmanager.uiclient.invokeai.login_page import LoginPage
from contextmanager.uiclient.invokeai.generate_page import GeneratePage
from contextmanager.uiclient.invokeai.canvas_page import CanvasPage
from contextmanager.uiclient.invokeai.upscaling_page import UpscalingPage




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
        
        #canvas_page.select_board("image_to_edit_board") 

        import time

        start = time.perf_counter()




        #canvas_page.page.evaluate("window.__invokeBridge.createNewCanvasEntityFromSelectedImage('raster_layer')")
        
        #canvas_page.page.evaluate("window.__invokeBridge.createNewCanvasEntityFromSelectedImage('raster_layer')")
        #canvas_page.page.on("console", lambda msg: print(msg.text))
        
        with page.expect_request_finished( 
                                          lambda r: "client_state" in r.url and r.method in ("POST", "PUT"),
                                          timeout=20000,
                        ):
            #canvas_page.page.evaluate("window.__invokeBridge.createNewCanvasEntityFromSelectedImage('raster_layer')")
            page.evaluate("window.__invokeBridge.params.setPositivePrompt('a cat wearing sunglasXXXX')")
            params = page.evaluate("window.__invokeBridge.params.get()")

            print(params["positivePrompt"])
        
        elapsed = time.perf_counter() - start
        #canvas_page.select_board("image_to_edit_board") 
        #canvas_page.select_board("Uncategorized")
        #print("before =", before)

        #print("after  =", after)
        
        print(f"client_state request finished in {elapsed:.3f}s")


if __name__ == "__main__":
    main()
