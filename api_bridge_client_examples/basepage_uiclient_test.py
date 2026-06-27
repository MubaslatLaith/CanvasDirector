from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage


INVOKE_URL = "http://127.0.0.1:9091"

def main():
    snapshot_path = Path("ui_snapshots/base_page_snapshot.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(INVOKE_URL)
        #page.wait_for_load_state("domcontentloaded")

        base_page = BasePage(page)
        base_page.wait_until_dom_stable()
        #snapshot = base_page.get_elements_snapshot()
        base_page.print_elements_summary()




        #print("Textboxes:", page.get_by_role("textbox").count())
        #base_page.save_elements_snapshot(snapshot_path)
        #print(snapshot)
        #print(f"Saved snapshot to {snapshot_path}")

        browser.close()


if __name__ == "__main__":
    main()
