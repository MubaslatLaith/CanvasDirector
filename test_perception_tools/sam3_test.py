import io
import requests 

import asyncio
from contextmanager.apiclient.invokeai.client import InvokeAIClient


def segment(image_url, prompt, threshold, mask_threshold, base_tools_url, headers): #, headers):
    task = 'segment'
    url = f'{base_tools_url}/{task}'
    payload = {
                "prompt": prompt, 
                "image_url": image_url,
                "threshold": threshold,
                "mask_threshold": mask_threshold,
                "headers": headers, 
                }

    response = requests.post(url, json=payload) #, #headers = headers)
    response.raise_for_status()
    segments = response.json()
    return segments 

async def main():
    INVOKE_URL = "http://127.0.0.1:9091"
    USERNAME = "email@email.email"
    PASSWORD = "weakpassword"


    api_client = InvokeAIClient(INVOKE_URL)
    user = api_client.login(USERNAME, PASSWORD)



    print ('t2i output image') 
    output_board_name = "image_to_edit_board" 
    #output_board_name = "In Board"
    output_image_name = api_client.boards.get_image_ids_by_board_name (output_board_name)
    print('output image')
    print(output_image_name)
    
    i=0
    output_image_url = api_client.images.get_image_url(output_image_name[i])
    print (output_image_url) 
    #output_image_url = f"https://{output_image_url}"



    segmentation_prompt = "hand" 
    base_tools_url = "http://0.0.0.0:8000"
    segmentation_output = segment(image_url = output_image_url, prompt = segmentation_prompt, threshold = 0.7, mask_threshold = 0.7, base_tools_url=base_tools_url, headers = api_client._get_headers()) 
    import pdb; pdb.set_trace() 
    

    boxes = segmentation_output['boxes'] 
    masks = segmentation_output['masks'] 


    









if __name__ == "__main__":
    asyncio.run(main())
