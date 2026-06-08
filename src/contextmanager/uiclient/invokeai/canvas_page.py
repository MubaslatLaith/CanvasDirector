from contextmanager.uiclient.invokeai.base_page import BasePage


class CanvasPage(BasePage):
    PAGE_BUTTON = "Canvas"
    INVOKE_BUTTON = "Invoke"
    PROMPT_TEXT_BOX = "prompt"
    

    #BOARD CATEGORIES
    BOARD_TAB_IMAGES = "images-tab"
    BOARD_TAB_ASSETS = "assets-tab" 

    #Board image context menu actions 
    NEW_CANVAS_FROM_IMAGE = "New Canvas from Image" 
    NEW_LAYER_FROM_IMAGE = "New Layer from Image" 

    #Board image new canvas - context sub menu actions 
    AS_RASTER_LAYER = "As Raster Layer"
    
    #Board image new layer - context sub menu actions 
    RASTER_LAYER = "Raster Layer" 
    INPAINT_MASK = "Inpaint Mask" 


    def update_prompt(self, prompt):
        prompt_box = self.page.locator(f"textarea[name='{self.PROMPT_TEXT_BOX}']")
        prompt_box.click()
        prompt_box.press("Control+A")
        prompt_box.press("Backspace")
        prompt_box.type(prompt)
    
    def new_canvas_from_board_image_as_raster(self, board_name): 
        self.op_over_selected_board_image(
                board_name, 
                board_tab = self.BOARD_TAB_IMAGES, 
                context_menu_op = self.NEW_CANVAS_FROM_IMAGE, 
                context_sub_menu_op = self.AS_RASTER_LAYER
                )

    
    def new_layer_from_board_asset_as_inpaint_mask(self, board_name):
        self.op_over_selected_board_image(
                board_name, 
                board_tab = self.BOARD_TAB_ASSETS,
                context_menu_op = self.NEW_LAYER_FROM_IMAGE, 
                context_sub_menu_op = self.INPAINT_MASK
                )
    

    def op_over_selected_board_image(self, board_name, board_tab, context_menu_op, context_sub_menu_op=None):
        self.select_board(board_name)

        self.page.get_by_test_id(board_tab).click() #"images-tab").click()
        self.page.wait_for_timeout(500)
        tab = self.page.get_by_test_id(board_tab)  #"images-tab")

        board_panel = tab.locator("xpath=ancestor::div[contains(@class, 'dv-view') and contains(@class, 'visible')][1]")
        self.screenshot_page("debug5.png")  
        
        self.wait_until_dom_stable()
        

        images = board_panel.locator("img[src*='/thumbnail']")

        image = images.last
        image.wait_for(state="visible", timeout=10000)
        image.scroll_into_view_if_needed()
        box = image.bounding_box()
        self.page.mouse.click(
            box["x"] + box["width"] / 2,
            box["y"] + box["height"] / 2,
            button="right"
        )
        self.page.wait_for_timeout(500)

        menu_item = self.page.get_by_text(context_menu_op, exact=True).last
        menu_item.wait_for(state="attached", timeout=5000)
        menu_item.hover(force=True)

        if context_sub_menu_op is not None:
            submenu_item = self.page.get_by_text(context_sub_menu_op, exact=True).last
            submenu_item.wait_for(state="attached", timeout=5000)
            submenu_item.click(force=True)
        else:
            menu_item.click(force=True)


    def invoke(self):
        self.page.get_by_role("button", name=self.INVOKE_BUTTON, exact=True).click()
