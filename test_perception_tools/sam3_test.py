import io
import requests 
import base64 

def segment(image_url, prompt, threshold, mask_threshold, base_tools_url): 
    task = 'segment'
    url = f'{base_tools_url}/{task}'
    payload = {
                "prompt": prompt, 
                "image_url": image_url,
                "threshold": threshold,
                "mask_threshold": mask_threshold
                }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    segments = response.json()
    return segments 
