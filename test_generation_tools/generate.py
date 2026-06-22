import io
import numpy as np
import requests
from PIL import Image
from contextmanager.generation_tools.invoke_generate import GenerationClient 










INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword"


generation_client = GenerationClient(INVOKE_URL, USERNAME, PASSWORD)
generation_client.reset_generation_settings() 


job_id = "mask_assg." 
generation_client.init_working_space(job_id) 


#TODO replace with call to SegmentationAgent (i.e., SAM3 for a specific image / issue ) 
mask = Image.open('/workspace/CanvasDirector/sam3_mask0.png') 




import pdb; pdb.set_trace() 

generation_client.assign_mask_to_edit(mask) 


with generation_client.ui_bridge.wait_client_state_saved():
    pass 



