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
       
        
        generate_page = GeneratePage(page) 
        
        #generate_page.page.evaluate("window.__invokeBridge.addRasterLayer()")
        """
        page = generate_page.page 
        page.get_by_role("button", name="Canvas", exact=True).click()
        page.wait_for_function("() => window.__invokeBridge !== undefined")
        print(page.evaluate("window.__invokeBridge.getManagerRepr()"))
        page.evaluate("window.__invokeBridge.addRasterLayer()")
        """
        page = generate_page.page 
        before = page.evaluate("window.__invokeBridge.getCanvasState().rasterLayers.entities.length")
        print("before:", before)

        page.evaluate("window.__invokeBridge.addRasterLayer()")

        after = page.evaluate("window.__invokeBridge.getCanvasState().rasterLayers.entities.length")
        print("after:", after)

        state = page.evaluate("window.__invokeBridge.getCanvasState().rasterLayers.entities")
        print(state)



if __name__ == "__main__":
    main()
