from contextmanager.uiclient.invokeai.base_page import BasePage


class CanvasPage(BasePage):
    PAGE_BUTTON = "Canvas"
    INVOKE_BUTTON = "Invoke"
    PROMPT_TEXT_BOX = "prompt"

    def update_prompt(self, prompt):
        prompt_box = self.page.locator(f"textarea[name='{self.PROMPT_TEXT_BOX}']")
        prompt_box.click()
        prompt_box.press("Control+A")
        prompt_box.press("Backspace")
        prompt_box.type(prompt)
    
   
    def op_over_selected_board_image(self, board_name):
        self.page.get_by_role("button", name=board_name, exact=True).click()
        self.page.get_by_test_id("images-tab").click()
        self.page.wait_for_timeout(500)
        images_tab = self.page.get_by_test_id("images-tab")
        board_panel = images_tab.locator("xpath=ancestor::div[contains(@class, 'dv-view')]")
        images = board_panel.locator("img[src*='/thumbnail']")
        print("panel image count:", images.count())

        image = images.last
        image.wait_for(state="visible", timeout=10000)
        image.scroll_into_view_if_needed()
        box = image.bounding_box()
        print("image box:", box)

        self.page.mouse.click(
            box["x"] + box["width"] / 2,
            box["y"] + box["height"] / 2,
            button="right"
        )

        self.page.wait_for_timeout(500)
        print(self.page.locator("body").inner_text())

        self.page.get_by_text("New Canvas from Image", exact=True).wait_for(state="visible", timeout=5000)
        self.page.get_by_text("New Canvas from Image", exact=True).hover()

        self.page.get_by_text("As Raster Layer", exact=True).wait_for(state="visible", timeout=5000)
        self.page.get_by_text("As Raster Layer", exact=True).click()

    def invoke(self):
        self.page.get_by_role("button", name=self.INVOKE_BUTTON, exact=True).click()
