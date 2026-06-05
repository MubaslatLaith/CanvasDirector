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

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError
import time

def wait_until_dom_stable(page, stable_ms=1000, poll_ms=250, timeout_ms=15000):
    deadline = time.time() + timeout_ms / 1000
    last_html = None
    stable_since = None

    while time.time() < deadline:
        try:
            html = page.evaluate("document.documentElement.outerHTML")
        except PlaywrightError:
            stable_since = None
            last_html = None
            time.sleep(poll_ms / 1000)
            continue

        if html == last_html:
            if stable_since is None:
                stable_since = time.time()
            if (time.time() - stable_since) * 1000 >= stable_ms:
                return
        else:
            last_html = html
            stable_since = None

        time.sleep(poll_ms / 1000)

    raise PlaywrightTimeoutError("DOM did not stabilize")

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
