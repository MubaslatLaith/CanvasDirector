import io
import numpy as np
import requests
from PIL import Image
from contextmanager.generation_tools.invoke_generate import GenerationClient 


class GenerationParameters:
    def __init__(self):
        prompt 


class GenerationState:
    def __init__(self):
        self.current_image_name = "" 
        self.reference_names = []
        self.current_objective = "" 
        self.issues = [] 
        self.generation_parameters 








INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword"

# current job id, used for workspace initialization/managemenet (in/out boards) 
job_id = "mask_assg."

# current image/mask TODO update current image selection
#current_working_image_board_name = "image_to_edit_board"
#TODO replace with call to SegmentationAgent (i.e., SAM3 for a specific image / issue ) 
mask = Image.open('/workspace/CanvasDirector/sam3_mask0.png')
# reference images 
reference_image_names = [] 

# generation paramters 
steps = 4
prompt = "A male anime character jumping"
image_to_edit_name = "eafd3ae3-2ab0-477d-80ce-13089655d595.png" 
references = [] 




#initialize the generation_client
generation_client = GenerationClient(INVOKE_URL, USERNAME, PASSWORD)

# current image/mask TODO update current image selection
#current_working_image_name = generation_client.api_client.boards.get_image_ids_by_board_name(current_working_image_board_name)[0]
#print(current_working_image_name)
import pdb; pdb.set_trace() 
#1 reset_generation settings 
generation_client.reset_generation_settings() 
#2 initialize working space (board_in_mask, board_in_image, board_out) 
generation_client.init_working_space(job_id) 
#3 assign mask to edit 
generation_client.assign_mask_to_edit(mask) 
mask_to_edit_name = generation_client.api_client.boards.get_image_ids_by_board_name(generation_client.board_name_mask_to_edit)[0]
#4 assign image to edit 
#generation_client.assign_image_to_edit(image_name = current_working_image_name) 
#5 assign reference images 
#for reference_image in reference_image_names: 
#    generation_client.assign_reference_image(reference_image) 



# assign canvas entity 
#image_to_edit_name = generation_client.api_client.boards.get_image_ids_by_board_name(generation_client.board_name_image_to_edit)[0]
#mask_to_edit_name = generation_client.api_client.boards.get_image_ids_by_board_name(generation_client.board_name_mask_to_edit)[0]
generation_client.assign_canvas_entity(image_name = image_to_edit_name, entity_type = "raster_layer")
generation_client.assign_canvas_entity(image_name = mask_to_edit_name, entity_type = "inpaint_mask")

#set generation parameters 
# prompt, steps, 
generation_client.set_generation_parameter(parameter = "positive_prompt", value = prompt) 
generation_client.set_generation_parameter(parameter = "steps", value = steps) 

#generate 
generation_client.generate() 
#assign generation output 
generation_client.assign_output() 



# wait for client state update 
with generation_client.ui_bridge.wait_client_state_saved():
    pass 



