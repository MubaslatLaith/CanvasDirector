import io
import base64
from transformers import Sam3Processor, Sam3Model
import torch
from PIL import Image
import requests
import numpy as np 


class SAM3Tool:
    name = "sam3"     
    
    def __init__(self, device):
        self.device = device

    def load(self):
        self.model = Sam3Model.from_pretrained("facebook/sam3").to(self.device)
        self.processor = Sam3Processor.from_pretrained("facebook/sam3")

    def run(self, task, req):
        #image_url = "http://images.cocodataset.org/val2017/000000077595.jpg"
        #image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")
        image_bytes = base64.b64decode(req.image_base64)
        image = Image.open(io.BytesIO(image_bytes))
        # Segment using text prompt
        inputs = self.processor(images=image, text=req.prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Post-process results 
        results = self.processor.post_process_instance_segmentation(   
                outputs,  
                threshold = req.threshold, 
                mask_threshold = req.mask_threshold,   
                target_sizes=inputs.get("original_sizes").tolist() 
                )[0]
        


        #encode_masks?
        encoded_masks = [] 
        for mask in results["masks"]:   
            mask_np = mask.detach().cpu().numpy()  
            # convert bool/float mask to uint8 image   
            mask_np = (mask_np > 0).astype(np.uint8) * 255  
            mask_image = Image.fromarray(mask_np)  
            buffer = io.BytesIO()  
            mask_image.save(buffer, format="PNG")   
            encoded_mask = base64.b64encode(  
                    buffer.getvalue()   
                    ).decode("utf-8")   
            encoded_masks.append(encoded_mask)




        
        return {
                "num_masks": len(results["masks"]),   
                "scores": results["scores"].detach().cpu().tolist(),  
                "boxes": results["boxes"].detach().cpu().tolist(), 
                "masks": encoded_masks, #results['masks'].detach().cpu().tolist(),
                }



        print("prompt:", repr(req.prompt))

        print("image:", image.size, image.mode)

        print("original_sizes:", inputs.get("original_sizes"))

        print("num masks:", len(results["masks"]))

        print("scores:", results["scores"])

        print("boxes:", results["boxes"])

        return results 
