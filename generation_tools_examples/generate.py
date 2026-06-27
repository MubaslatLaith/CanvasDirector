import io
import numpy as np
import requests
from PIL import Image
from contextmanager.generation_tools.invoke_generate import GenerationClient 
from contextmanager.generation_tools.invoke_generation_request import InvokeAIGenerationRequest, GenerationParameters

#TODO 
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


#TODO create board and add image > return image name 
#TODO create masks board if it does not exist 
board_name = "masks" 
#TODO validate unique board name, if not add a number 
#generation_client.api_client.boards.create_board(board_name) 



board_id = generation_client.api_client.boards.get_board_by_name(board_name)['board_id']
mask_name = generation_client.add_new_image_to_board(image=mask, board_id=board_id, image_category="mask")
#mask_to_edit_name = generation_client.api_client.boards.get_image_ids_by_board_name(board_name)[0]


t2i_generation_request = InvokeAIGenerationRequest(job_id = "t2i_test0",
                                               generation_parameters = GenerationParameters(
                                                   positive_prompt = "an airplane", 
                                                   steps = steps,
                                                   )
                                                   )


inpaint_generation_request = InvokeAIGenerationRequest(job_id = "inpaint_test0",
                                               images_to_edit = [image_to_edit_name], 
                                               masks_to_edit = [mask_name], 
                                               generation_parameters = GenerationParameters(
                                                   positive_prompt = "A male anime character jumping", 
                                                   steps = steps,
                                                   )
                                               )

i2i_generation_request = InvokeAIGenerationRequest(job_id = "i2i_test0",
                                                   images_to_edit = [image_to_edit_name],
                                                   generation_parameters = GenerationParameters(
                                                       positive_prompt = "Change image style to realistic",
                                                       steps = steps,
                                                       )
                                                   )


ref_generation_request = InvokeAIGenerationRequest(job_id = "ref2i_test0",
                                                reference_images = [image_to_edit_name], 
                                                generation_parameters = GenerationParameters(
                                                    positive_prompt = "front view of the character",
                                                    steps = steps,
                                                    )
                                                )

ref_inpaint_generation_request = InvokeAIGenerationRequest(job_id = "ref2i_inpaint_test0",
                                                           images_to_edit = [image_to_edit_name], 
                                                           reference_images = [image_to_edit_name],
                                                           mask_to_edit = [mask_name], 
                                                           generation_parameters = GenerationParameters(                 
                                                                                positive_prompt = prompt,
                                                                                steps = steps,
                                                                                ) 
                                                           )




#inpaint_generation_request.job_id = "test2" 

output_image = generation_client.run(inpaint_generation_request) 
print('_______') 
output_image = generation_client.run(t2i_generation_request) 
print('_______') 
output_image = generation_client.run(i2i_generation_request) 
print('_______')
output_image = generation_client.run(ref_generation_request)
print('_______') 
output_image = generation_client.run(ref_inpaint_generation_request) 






