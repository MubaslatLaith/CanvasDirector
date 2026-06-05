# scripts/test_invoke_login.py

from playwright.sync_api import sync_playwright


INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword"

class UIElement:
    LOGIN_FIELD_USER = "Email"
    LOGIN_FIELD_PASSWORD = "Password"
    LOGIN_BUTTON = "Sign In"
    LOGIN_REMEMBER_ME = "Remember me for 7 days"

import time

def wait_until_dom_stable(page, stable_for=1.0, timeout=30):
    start = time.time()
    last_html = page.content()
    last_change = time.time()

    while time.time() - start < timeout:
        time.sleep(0.25)

        html = page.content()

        if html != last_html:
            last_html = html
            last_change = time.time()

        if time.time() - last_change >= stable_for:
            return

    raise TimeoutError("DOM never stabilized")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        print(f"Opening {INVOKE_URL}")
        page.goto(INVOKE_URL, wait_until="networkidle")

        page.get_by_label(UIElement.LOGIN_FIELD_USER).fill(USERNAME)
        page.get_by_label(UIElement.LOGIN_FIELD_PASSWORD).fill(PASSWORD)
        

        screenshot_path_before = "login_before.png"
        page.screenshot(path=screenshot_path_before, full_page=True)
        
        page.get_by_label(UIElement.LOGIN_REMEMBER_ME).uncheck(force = True)

        page.get_by_role("button", name=UIElement.LOGIN_BUTTON).click()

        page.wait_for_load_state("networkidle")

        print("Current URL:", page.url)
        print("Page title:", page.title())

        #if "login" in page.url.lower():
        #    print("LOGIN FAILED")
        #else:
        #    print("LOGIN SUCCEEDED")
        
        wait_until_dom_stable(page)


        try:
            page.get_by_label(UIElement.LOGIN_FIELD_PASSWORD).wait_for(state="hidden", timeout=10000)
            print("Login succeeded")
        except TimeoutError:
            print("Still on login screen")

        screenshot_path = "invoke_login.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Saved screenshot to {screenshot_path}")

        browser.close()


if __name__ == "__main__":
    main()
