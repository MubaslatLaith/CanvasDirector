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
        
        prompt = "a dog"#"a cat" 


        #login 
        login_page = LoginPage(page)
        login_page.select_page(INVOKE_URL)
        login_page.deselect_remember_me()
        login_page.login(USERNAME, PASSWORD) 
        login_successful = login_page.validate_login()   

        #t2i 
        generate_page = GeneratePage(page) 
        generate_page.select_page()
        
        generate_page.update_prompt(prompt) #"125as11111") 
        generate_page.screenshot_page("generator_page_after_update_prompt.png")        
        generate_page.invoke() 
        generate_page.wait_until_dom_stable() 
        generate_page.screenshot_page("generator_page_after_gen.png")
    
        browser.close()


if __name__ == "__main__":
    main()
