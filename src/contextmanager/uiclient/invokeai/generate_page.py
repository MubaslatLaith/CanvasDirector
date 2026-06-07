from contextmanager.uiclient.invokeai.base_page import BasePage


class GeneratePage(BasePage):
    PAGE_BUTTON = "Generate"
    INVOKE_BUTTON = "Invoke" 
    PROMPT_TEXT_BOX = "prompt"
    
    def update_prompt(self, prompt):
        prompt_box = self.page.locator(f"textarea[name='{self.PROMPT_TEXT_BOX}']")
        prompt_box.click()
        prompt_box.press("Control+A")
        prompt_box.press("Backspace")
        prompt_box.type(prompt)

    def select_board(self, board_name):
        pass 


    def invoke(self):
        self.page.get_by_role("button", name=self.INVOKE_BUTTON, exact=True).click()
