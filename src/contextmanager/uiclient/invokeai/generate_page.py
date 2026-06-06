from contextmanager.uiclient.invokeai.base_page import BasePage


class GeneratePage(BasePage):
    PAGE_BUTTON = "Generate"
    PROMPT_TEXT_BOX = "prompt"

    def update_prompt(self, prompt):
        self.page.locator(f"textarea[name='{self.PROMPT_TEXT_BOX}']").fill(prompt)
        value = self.page.locator(f"textarea[name='{self.PROMPT_TEXT_BOX}']").input_value()
        print("Prompt value:", value)
