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
# get image_to_edit_name by board_name 
#image_to_edit_name = generation_client.api_client.boards.get_image_ids_by_board_name(current_working_image_board_name)[0]

image_to_edit_name = "eafd3ae3-2ab0-477d-80ce-13089655d595.png" 
references = [] 


#initialize the generation_client
generation_client = GenerationClient(INVOKE_URL, USERNAME, PASSWORD)

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field, ConfigDict
from PIL import Image

class GenerationMode(str, Enum):
    TXT2IMG = "txt2img"
    INPAINT = "inpaint"
    REF2IMG = "ref2img"


class GenerationParameters(BaseModel):
    steps: int 
    prompt: str

class InvokeAIGenerationRequest(BaseModel):
    job_id: str 
    mode: GenerationMode
    
    # image names in invokai 
    images_to_edit: list[str] = Field(default_factory=list)
    masks_to_edit: list[str] = Field(default_factory=list)
    reference_images: list[str] = Field(default_factory=list)
    

    parameters: GenerationParameters = Field(default_factory=GenerationParameters)



#TODO create board and add image > return image name 
board_name = "" 
#TODO validate unique board name, if not add a number 
generation_client.api_client.boards.create_board(board_name) 
board_id = generation_client.api_client.boards.get_board_by_name(board_name)['board_id']
generation_client.add_new_image_to_board(image=mask, board_id=, image_category="mask")
mask_to_edit_name = generation_client.api_client.boards.get_image_ids_by_board_name(generation_client.board_name_mask_to_
                                                                                    edit)[0]


inpaint_generation_request = InvokeAIGenerationRequest(mode = "inpaint", 
                                               images_to_edit = [image_to_edit_name], 
                                               masks_to_edit = [mask_to_edit_name], 
                                               GenerationParameters(
                                                   prompt = prompt, 
                                                   steps = steps,
                                                   )
                                               )








#inpaint_generation_request.mode = "inpaint" 
#inpaint_generation_request.





def run(generation_client, request: GenerationRequest):
    #1 reset_generation settings 
    generation_client.reset_generation_settings() 
    #2 initialize working space (board_in_mask, board_out) 
    generation_client.init_working_space(request.job_id) 
    #3 add reference images 
    for reference_image in request.reference_images:
        generation_client.assign_reference_image(reference_image) 
    #4 assign canvas raster layers (in order)
    for image_name in response.images_to_edit:
        generation_client.assign_canvas_entity(image_name = image_to_edit_name, entity_type = "raster_layer")
    #5 assign canvas mask  
    for mask_name in response.masks_to_edit:
        generation_client.assign_canvas_entity(image_name = mask_name, entity_type = "inpaint_mask")
    #6 set generation parameters 
    for parameter, value in request.parameters.model_dump(exclude_none=True).items():
            self.set_parameter(parameter, value)
    generation_client.generate() 
    # modify to return image name of output image 
    generation_client.assign_output() 
    # wait for client state update 
    with generation_client.ui_bridge.wait_client_state_saved():
        pass 



