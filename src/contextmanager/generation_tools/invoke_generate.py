from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage
from contextmanager.uiclient.invokeai.login_page import LoginPage
from contextmanager.uiclient.invokeai.generate_page import GeneratePage
from contextmanager.uiclient.invokeai.canvas_page import CanvasPage
from contextmanager.uiclient.invokeai.upscaling_page import UpscalingPage


from contextmanager.uiclient.invokeai.invoke_bridge import InvokeUIBridge
from contextmanager.apiclient.invokeai.client import InvokeAIClient


#generation_client = GenerationClient(INVOKE_URL, USERNAME, PASSWORD) 

class GenerationClient:
    def __init__ (self, INVOKE_URL, USERNAME, PASSWORD):
        self._api_client_setup(INVOKE_URL, USERNAME, PASSWORD)
        self._ui_client_setup( INVOKE_URL, USERNAME, PASSWORD)

    def _api_client_setup(self, INVOKE_URL, USERNAME, PASSWORD): 
        self.api_client = InvokeAIClient(INVOKE_URL)
        user = self.api_client.login(USERNAME, PASSWORD)
    
    def _ui_client_setup(self, INVOKE_URL, USERNAME, PASSWORD):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=True)
        self.page = browser.new_page()
        self._ui_client_login(INVOKE_URL, USERNAME, PASSWORD)
        self.go_to_canvas() 
        self.ui_bridge = InvokeUIBridge(self.page)


    def _ui_client_login(self, INVOKE_URL, USERNAME, PASSWORD):
        login_page = LoginPage(self.page)
        login_page.screenshot_page("bridge.png")
        login_page.select_page(INVOKE_URL)
        login_page.deselect_remember_me()
        login_page.login(USERNAME, PASSWORD)
        login_successful = login_page.validate_login()
        
    def go_to_canvas(self):
        canvas_page = CanvasPage(self.page)
        canvas_page.select_page()
        

    def reset_generation_settings(self):
        # reset all generation settings and delete all global references 
        self.ui_bridge.reset_generation_settings() 
        self.ui_bridge.delete_all_ref_images() 
        self.ui_bridge.reset_canvas()
    

    def init_working_space(self, job_id):
        self.board_name_image_to_edit = f'inpaint_image_job_{job_id}' 
        self.board_name_mask_to_edit = f'inpaint_mask_job_{job_id}' 
        self.board_name_output = f'inpaint_output_job_{job_id}'
        
        self.clear_working_space() 

        #self.api_client.boards.create_board(self.board_name_image_to_edit) 
        self.api_client.boards.create_board(self.board_name_mask_to_edit) 
        self.api_client.boards.create_board(self.board_name_output) 

        #self.board_id_image_to_edit = self.api_client.boards.get_board_by_name(self.board_name_image_to_edit)['board_id'] 
        self.board_id_mask_to_edit = self.api_client.boards.get_board_by_name(self.board_name_mask_to_edit)['board_id']
        self.board_id_output = self.api_client.boards.get_board_by_name(self.board_name_output)['board_id']


     
    def clear_working_space(self):
        try:
            #self.api_client.boards.delete_board_by_name(self.board_name_image_to_edit)
            self.api_client.boards.delete_board_by_name(self.board_name_mask_to_edit)
            self.api_client.boards.delete_board_by_name(self.board_name_output) 
        except:
            pass 


    def assign_reference_image(self, image_name):
        self.ui_bridge.create_global_reference_image_from_image_name(image_name)
    
    def assign_image_to_board(self, image_name, board_id):
        self.api_client.images.assign_image(image_name, board_id)
    

    #TODO return new image_name
    def add_new_image_to_board(self, image, board_id, image_category):
        self.api_client.images.upload_pil_image(image=image, filename="image.png", board_id=board_id, image_category=image_category)

    #def assign_new_image(self, image_name, board_id):
    #    self.assign_new_image_to_board(image = mask, board_id = self.board_id_mask_to_edit, image_category="image") 
    #    #self.api_client.images.assign_image(image_name, self.board_id_image_to_edit) 
    
    # TODO remove 
    #def add_new_mask (self, mask): 
    #    self.assign_new_image_to_board(image = mask, board_id = self.board_id_mask_to_edit, image_category="mask")
        #self.api_client.images.upload_pil_image(image=mask, filename="image.png", board_id=self.board_id_mask_to_edit, image_category="mask")

    def assign_canvas_entity(self, image_name, entity_type):
        """
        entity_type: "raster_layer" | "inpaint_mask" 
        """
        self.ui_bridge.create_canvas_entity_from_image_name(entity_type, image_name)
         
    def update_canvas_dim(self, x_axis, y_axis): 
        #TODO 
        pass 

    def set_generation_parameter(self, parameter, value):
        #TODO 
        #1- denoising 
        self.ui_bridge.set_parameter(parameter, value) 
    
    def select_model(self, model_name):
        #TODO 
        pass 

    def select_lora(self, lora_name):
        #TODO 
        pass 

    def get_available_parameters(self):
        #TODO 
        pass 

    def assign_output(self):
        self.ui_bridge.save_selected_to_gallery(board_id = self.board_id_output)
        self.ui_bridge.canvas_discard_all() 
        pass 

    def generate(self):
        self.ui_bridge.invoke() 
        


        """
        input_board_name = "My Board" 
        mask_path = "/workspace/invokeai/test_mask.png"  
        image_to_edit_id = api_client.boards.get_image_ids_by_board_name (input_board_name) 
        image_to_edit_id = image_to_edit_id[0] 
        print(image_to_edit_id)   
        
        


        # assign image to board 
        #api_client.images.assign_image(image_id = image_to_edit_id, board_id = board_id_image_to_edit)
        # upload mask to board 
        api_client.images.upload_image(image_path = mask_path, board_id = board_id_mask_to_edit, image_category = "mask") 

        
        
        #TODO modify to take board name
        image_name = image_to_edit_id#api_client. 
        mask_name = api_client.boards.get_image_ids_by_board_name(board_name_mask_to_edit)[0] 

        bridge.create_canvas_entity_from_image_name("raster_layer", image_name)
        bridge.create_canvas_entity_from_image_name("inpaint_mask", mask_name )
        

        bridge.set_parameter("steps", 7)
        with bridge.wait_client_state_saved():
            bridge.set_parameter("positive_prompt", "fix hand, hand should have 5 fingers and should be wide open. Hands should have correct anatomy") 

        bridge.invoke()

        #with bridge.wait_client_state_saved():
        bridge.save_selected_to_gallery(board_id = board_id_output)
        bridge.canvas_discard_all() 
        with bridge.wait_client_state_saved():
            pass 

        return 




        """     

    # cleanup 
        """ 
        """


        """

    image_to_edit_id = api_client.boards.get_image_ids_by_board_name (board_name_image_to_edit)
    mask_to_edit_id = api_client.boards.get_image_ids_by_board_name (board_name_mask_to_edit) 

    print(image_to_edit_id)
    print(mask_to_edit_id)

        """

