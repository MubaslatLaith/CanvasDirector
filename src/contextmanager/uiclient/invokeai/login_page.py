from contextmanager.uiclient.invokeai.base_page import BasePage
from playwright.sync_api import TimeoutError


class LoginPage(BasePage):
    LOGIN_FIELD_USER = "Email"
    LOGIN_FIELD_PASSWORD = "Password"
    LOGIN_BUTTON = "Sign In"
    LOGIN_REMEMBER_ME = "Remember me for 7 days"

    def select_page(self, invoke_url):
        self.page.goto(invoke_url, wait_until="networkidle")
        self.wait_until_dom_stable()
    
    def deselect_remember_me(self):
        self.page.get_by_label(self.LOGIN_REMEMBER_ME).uncheck(force=True)
    
    def login(self, username, password):
        self.page.get_by_label(self.LOGIN_FIELD_USER).fill(username)
        self.page.get_by_label(self.LOGIN_FIELD_PASSWORD).fill(password)
        self.deselect_remember_me()
        self.page.get_by_role("button", name=self.LOGIN_BUTTON).click()
        self.wait_until_dom_stable()
        
    def validate_login(self, screenshot_path="invoke_login.png"):
        try:
            self.page.get_by_label(self.LOGIN_FIELD_PASSWORD).wait_for(
                state="hidden",
                timeout=10000,
            )

            login_succeeded = True
            print("login successful")
        except TimeoutError:
            login_succeeded = False
            print ("login failed")

        self.page.screenshot(path=screenshot_path, full_page=True)

        return login_succeeded

