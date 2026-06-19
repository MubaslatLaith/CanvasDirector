import json
from contextmanager.agents.base_agent import BaseAgent 

class TaskCritic(BaseAgent):

    @property
    def name(self):
        return "task_critic" 
    
    async def run(self, input_images, output_image, user_request):
        user_content = self.build_user_content(input_images, output_image, user_request) 
        response = self.complete(user_content, temperature = 0) 
        content = response.choices[0].message.content
        return self._parse_json(content)


    def build_user_content(self, input_images, output_image, user_request): 
        user_request_content = [{
                            "type": "text",
                            "text": f"user request: {user_request}",
                        }]

        # TODO build input images message 
        base64images = True 
        input_images_content.append(
                        {
                            "type": "text",
                            "text": f"input images:",
                        }) 
        
        for image in input_images: 
            if base64images: 
                url = f"data:image/png;base64,{image}"
            else: 
                url = image 
            input_images_content.append( {
                "type": "image_url",
                "image_url": {
                    "url": url 
                    }
                }
                                        )


        output_image_content = [] 
        # TODO build output image message  
        output_image_content.append(
                        {
                            "type": "text",
                            "text": f"output image:",
                        })
        if base64images:
            url = f"data:image/png;base64,{image}" 
        else:
            url = output_image 
        output_image_content.append( {
                "type": "image_url",
                "image_url": {
                    "url": url
                    }
                }


        user_content = user_request_content + input_images_content + output_image_content 
        return user_content


    def _parse_json(self, content):
        if isinstance(content, dict):
            return content

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            start = content.find("{")
            end = content.rfind("}") + 1

            if start == -1 or end == 0:
                raise ValueError(f"Task critic did not return JSON: {content}")

            return json.loads(content[start:end])
