import time 
from pathlib import Path
import json
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def select_page(self):
        raise NotImplementedError("Each page stub should implement select_page().")

    def get_buttons(self):
        return self.page.get_by_role("button").all()

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

    def get_elements_snapshot(self):
        return {
            "buttons": [self.get_element_info(button) for button in self.get_buttons()],
            "text_boxes": [self.get_element_info(text_box) for text_box in self.get_text_boxes()],
            "sliders": [self.get_element_info(slider) for slider in self.get_sliders()],
            "checkboxes": [self.get_element_info(checkbox) for checkbox in self.get_checkboxes()],
            "upload_inputs": [self.get_element_info(upload_input) for upload_input in self.get_upload_inputs()],
            "selects": [self.get_element_info(select) for select in self.get_selects()],
        }

    def save_elements_snapshot(self, output_path):
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(self.get_elements_snapshot(), indent=2), encoding="utf-8")

    def get_element_info(self, element):
        return element.evaluate("""
            e => ({
                tag: e.tagName,
                role: e.getAttribute("role"),
                type: e.getAttribute("type"),
                id: e.getAttribute("id"),
                name: e.getAttribute("name"),
                aria_label: e.getAttribute("aria-label"),
                aria_labelledby: e.getAttribute("aria-labelledby"),
                placeholder: e.getAttribute("placeholder"),
                title: e.getAttribute("title"),
                test_id: e.getAttribute("data-testid"),
                text: e.innerText,
                text_content: e.textContent,
                value: e.value ?? null,
                checked: e.checked ?? null,
                disabled: e.disabled ?? null,
                class_name: e.className,
            })
        """)
   
    
    def print_elements_summary(self):
        snapshot = self.get_elements_snapshot()

        identifier_fields = [
            "aria_label",
            "placeholder",
            "name",
            "text",
            "id",
        ]

        for element_type, elements in snapshot.items():
            for element in elements:
                identifier = "<unnamed>"
                identifier_type = "unknown"

                for field in identifier_fields:
                    value = element.get(field)

                    if value:
                        identifier = value
                        identifier_type = field
                        break

                print(
                    f"[{element_type}] "
                    f"{identifier} "
                    f"({identifier_type})"
                )

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
