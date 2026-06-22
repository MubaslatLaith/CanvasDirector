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


board_name = "test0" 
images_in_board = generation_client.api_client.boards.get_image_ids_by_board_name(board_name) 
valid_mask_url = generation_client.api_client.images.get_image_url(image_name = images_in_board[0]) 
response = requests.get(valid_mask_url, headers=generation_client.api_client._get_headers()) 
valid_mask = Image.open(io.BytesIO(response.content))

valid_mask.load()

print("format:", valid_mask.format)

print("mode:", valid_mask.mode)

print("size:", valid_mask.size)

print("bands:", valid_mask.getbands())

arr = np.array(valid_mask)

print("shape:", arr.shape)

print("dtype:", arr.dtype)

if valid_mask.mode == "L":

    print("unique:", np.unique(arr)[:50])

    print("min/max:", arr.min(), arr.max())

    print("white ratio:", (arr > 127).sum() / arr.size)

elif valid_mask.mode == "RGBA":

    alpha = arr[:, :, 3]

    rgb = arr[:, :, :3]

    print("rgb min/max:", rgb.min(), rgb.max())

    print("alpha unique:", np.unique(alpha)[:50])

    print("alpha min/max:", alpha.min(), alpha.max())

    print("alpha white ratio:", (alpha > 127).sum() / alpha.size)


