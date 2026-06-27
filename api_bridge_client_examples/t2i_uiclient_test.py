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


        generate_page = GeneratePage(page) 
        canvas_page = CanvasPage(page)
        upscaling_page = UpscalingPage(page)

        generate_page.select_page()
        """
        #inspect button candidates of name / TODO move to base_page 
        buttons = generate_page.page.get_by_role("button", name="Invoke")

        count = buttons.count()

        for i in range(count):
            button = buttons.nth(i)

            print(f"Button {i}")
            print("Text:", button.inner_text())
            print("Aria label:", button.get_attribute("aria-label"))
            print("Title:", button.get_attribute("title"))
            print("HTML:", button.evaluate("e => e.outerHTML"))
            print()
        """
        #generate_page_buttons = generate_page.get_buttons() 
        #import pdb; pdb.set_trace()

        invoke = generate_page.page.get_by_role("button", name="Invoke", exact=True)
        print(invoke.get_attribute("data-testid"))
        import pdb;pdb.set_trace() 
        
        generate_page.update_prompt(prompt="a male anime character jumping") #"125as11111") 
        generate_page.screenshot_page("generator_page_after_update_prompt.png")        
        generate_page.invoke() 
        generate_page.wait_until_dom_stable() 
        generate_page.screenshot_page("generator_page_after_gen.png")
    
        #print(generate_page.page.content()) 

        page = generate_page.page
        print("Textboxes:", page.get_by_role("textbox").count())
        for i in range(page.get_by_role("textbox").count()):
            textbox = page.get_by_role("textbox").nth(i)
            print(i, textbox.evaluate("e => e.outerHTML"))





        #canvas_page.select_page() 
        #upscaling_page.select_page() 

        browser.close()


if __name__ == "__main__":
    main()
