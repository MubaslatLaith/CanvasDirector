from contextmanager.uiclient.invokeai.base_page import BasePage


class GeneratePage(BasePage):
    PAGE_BUTTON = "Generate"
    PROMPT_TEXT_BOX = "prompt"

    def update_prompt(self, prompt):
        prompt_box = self.page.locator("textarea[name='prompt']")

        prompt_box.click()

        prompt_box.press("Control+A")

        prompt_box.press("Backspace")

        prompt_box.type(prompt)
