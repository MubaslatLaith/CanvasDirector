from pathlib import Path
from playwright.sync_api import sync_playwright

from contextmanager.uiclient.invokeai.base_page import BasePage
from contextmanager.uiclient.invokeai.login_page import LoginPage
from contextmanager.uiclient.invokeai.generate_page import GeneratePage
from contextmanager.uiclient.invokeai.canvas_page import CanvasPage
from contextmanager.uiclient.invokeai.upscaling_page import UpscalingPage


from contextmanager.uiclient.invokeai.invoke_bridge import InvokeUIBridge
from contextmanager.apiclient.invokeai.client import InvokeAIClient
from contextmanager.generation_tools.invoke_generation_request import InvokeAIGenerationRequest 


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
        self.board_name_output = f'inpaint_output_job_{job_id}'
        
        self.clear_working_space() 

        self.api_client.boards.create_board(self.board_name_output) 

        self.board_id_output = self.api_client.boards.get_board_by_name(self.board_name_output)['board_id']


     
    def clear_working_space(self):
        try:
            self.api_client.boards.delete_board_by_name(self.board_name_output) 
        except:
            pass 


    def assign_reference_image(self, image_name):
        self.ui_bridge.create_global_reference_image_from_image_name(image_name)
    
    def assign_image_to_board(self, image_name, board_id):
        self.api_client.images.assign_image(image_name, board_id)

    def add_new_image_to_board(self, image, board_id, image_category):
        image_name = self.api_client.images.upload_pil_image(image=image, filename="image.png", board_id=board_id, image_category=image_category)
        return image_name
    
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
        


    def run(self, generation_request: InvokeAIGenerationRequest):
        #1 reset_generation settings (reset generation settings, clear canvas and  
        self.reset_generation_settings()
        #2 initialize working space (board_in_mask, board_out) 
        self.init_working_space(generation_request.job_id)
        #3 add reference images 
        for reference_image in generation_request.reference_images:
            self.assign_reference_image(reference_image)
        #4 assign canvas raster layers (in order)
        for base_image_name in generation_request.images_to_edit:
            self.assign_canvas_entity(image_name = base_image_name, entity_type = "raster_layer")
        #5 assign canvas mask  
        for mask_name in generation_request.masks_to_edit:
            self.assign_canvas_entity(image_name = mask_name, entity_type = "inpaint_mask")
        #6 set generation parameters 
        for parameter, value in generation_request.generation_parameters.model_dump(exclude_none=True).items():
            self.set_generation_parameter(parameter, value)
        self.generate()
        #7 save output to gallery
        # TODO modify to return image name of output image 
        self.assign_output()
        #8 wait for client state update 
        with self.ui_bridge.wait_client_state_saved():
            pass
        output_image_name = self.api_client.boards.get_image_ids_by_board_name(self.board_name_output)[0]
        return output_image_name 


