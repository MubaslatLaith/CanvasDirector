import time 
from pathlib import Path
import json
from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, Error as PlaywrightError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def select_page(self):
        self.page.get_by_test_id(self.PAGE_BUTTON).click()
        self.wait_until_dom_stable()
        
    def screenshot_page(self, screenshot_path):
        self.page.screenshot(path=screenshot_path, full_page=True)  

    def get_buttons(self):
        result = []

        for button in self.page.get_by_role("button").all():
            result.append({
                "text": button.inner_text(),
                "aria_label": button.get_attribute("aria-label"),
                "title": button.get_attribute("title"),
                "id": button.get_attribute("id"),
                "name": button.get_attribute("name"),
            })

        return result

    def get_text_boxes(self):
        return self.page.get_by_role("textbox").all()

    def get_sliders(self):
        return self.page.get_by_role("slider").all()

    def get_checkboxes(self):
        return self.page.get_by_role("checkbox").all()

    def get_upload_inputs(self):
        return self.page.locator("input[type='file']").all()

    def get_selects(self):
        return self.page.locator("select").all()

        

    def wait_until_dom_stable(self, stable_ms=1000, poll_ms=250, timeout_ms=15000):
        deadline = time.time() + timeout_ms / 1000
        last_html = None
        stable_since = None

        while time.time() < deadline:
            try:
                html = self.page.evaluate("document.documentElement.outerHTML")
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
