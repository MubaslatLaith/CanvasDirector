import io
import numpy as np
import requests
from PIL import Image
from contextmanager.generation_tools.invoke_generate import GenerationClient
from contextmanager.generation_tools.invoke_generation_request import InvokeAIGenerationRequest, GenerationParameters

from contextmanager.agents.task_critic.agent import TaskCriticAgent
from contextmanager.agents.quality_critic.agent import QualityCriticAgent
from contextmanager.agents.planner.agent import PlannerAgent
from contextmanager.agents.qa.agent import QAAgent



INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword"
#TODO create multiple generation clients (different user names) 
#generation_client = GenerationClient(INVOKE_URL, USERNAME, PASSWORD) 
#generation_client.run(generation_request) 
base_url = "http://127.0.0.1:8001/v1"
api_key = "sk-no-key-required"
planner = PlannerAgent(base_url=base_url,api_key=api_key,)
#result = planner.run(issue)
quality_critic = QualityCriticAgent(base_url=base_url,api_key=api_key,)
#result = quality_critic.run(output_image = output_image_url)
#TODO modify to account for different types of tasks (i.e., input_reference images should be different than input base image for i2i or inpainting, the task evaluation should be different)
task_critic = TaskCriticAgent(base_url=base_url,api_key=api_key,) 
#output_image_name = ""
#input_image_names = [] 
#output_image_url = generation_client.api_client.images.get_image_url(output_image_name)
#input_image_urls = [generation_client.api_client.images.get_image_url(image_name) for image_name in input_image_names]
#task = "remove strap"
#task_critic.run(input_images = input_images_urls, output_image = output_image_url, user_request = task)
qa = QAAgent(base_url=base_url,api_key=api_key,) 
#Q1: Is there an existing image to modify?
#Q2: Is the issue confined to a specific region of the image? 
#question = "Can the issue be resolved by modifying a bounded image region while leaving the remainder of the image unchanged?" #"Is the issue confined to a specific region of the image?" 
#prompt = f"\nissue: {issue}\n{question}"
#print(prompt)
#result = qa.run(prompt)




mage_to_edit_name = "eafd3ae3-2ab0-477d-80ce-13089655d595.png"
#mask = Image.open('/workspace/CanvasDirector/sam3_mask0.png')

"""
generation_request = InvokeAIGenerationRequest(job_id = "ref2i_inpaint_test0",
                         images_to_edit = [image_to_edit_name],
                         reference_images = [image_to_edit_name],
                         mask_to_edit = [mask_name],
                         generation_parameters = GenerationParameters(
                             positive_prompt = prompt,
                             steps = steps,
                             )
                         )
"""






planner_flags = {
    "has_base": {
        "question": "Does the request include an existing base image that should be edited or preserved?",
        "type": "boolean"
    },

    "has_ref": {
        "question": "Does the request include one or more reference images?",
        "type": "boolean"
    },

    "localized_edit": {
        "question": "Is the requested change localized to one or more specific regions of the base image?",
        "type": "boolean"
    }, 
    "multiple_localized_edits": {
        "question": "Does it require edits over multiple segments?", 
        "type": "boolean"    
    },
    "segmentable": {
        "question": "Can each localized region likely be isolated using segmentation or masking?",
        "type": "boolean"
    },

    "needs_ref": {
        "question": "Is a reference image actually required to perform the requested edit?",
        "type": "boolean"
    },

    "can_be_completed_in_single_generation": {
        "question": "Should be False if multiple localized edits is True.Can the entire request likely be completed reliably in a single image generation job? If multiple simple generations are needed then should be False.",
        "type": "boolean"
    },

    "requires_multiple_independent_jobs": {
        "question": "Should be False if multiple_localized_edits is True. If multiple generation jobs are required, can they be executed independently without relying on the output of another job?",
        "type": "boolean"
    },

    "requires_multiple_dependent_jobs": {
        "question": "Should be True if multiple_localized_edits is True. If multiple generation jobs are required, do one or more jobs depend on the output of previous jobs and therefore require sequential execution?",
        "type": "boolean"
    }
}


import json

planner_flag_descriptions = "\n".join(
    f'- {key}: {value["question"]}'
    for key, value in planner_flags.items()
)

json_schema = {
    key: "boolean" if value["type"] == "boolean" else value["type"]
    for key, value in planner_flags.items()
}

json_schema["reasoning"] = {
    key: "brief reason"
    for key in planner_flags
}

system_prompt = f"""
You are a workflow-state classifier for an image generation planner.

Answer only with valid JSON.

Your job is not to choose tools directly.
Your job is to answer decision questions about the user's request.

Definitions:
- base image: an existing image that should be edited, preserved, or used as the main composition.
- reference image: an additional image used as guidance for identity, style, pose, object appearance, or content.
- localized edit: a change affecting a specific object, region, body part, or small set of regions.
- segmentable: the target can likely be isolated with a mask.
- non-localized/global edit: the whole image changes.

Answer the following questions:

{planner_flag_descriptions}

Return JSON matching this schema:

{json.dumps(json_schema, indent=2)}
"""



#TODO move to PlannerAgent
def validate_planner_flags(planner_flags):
    validation = {} 

    validation["multiple_job_validation"] = planner_flags["can_be_completed_in_single_generation"] != (
            planner_flags["requires_multiple_dependent_jobs"]
            or
            planner_flags["requires_multiple_independent_jobs"]
            )
    
    validation["multiple_segments_validation"] = planner_flags["can_be_completed_in_single_generation"] != planner_flags["multiple_localized_edits"]
    
    



def break_generation_job(planner, issue, planner_flags):

    if planner_flags["can_be_completed_in_single_generation"]:
        return [issue] 
        
    dependent = planner_flags["requires_multiple_dependent_jobs"]
    independent = planner_flags["requires_multiple_independent_jobs"]


    if dependent and independent:
        job_type = "dependent and independent jobs"
        
        instruction = (
                "Break the task into groups of jobs. "
                "Return ordered dependent chains where dependencies exist, "
                "and separate independent jobs where jobs can run in parallel."
                                                                                                    )
    elif dependent:
        job_type = "dependent jobs"
        
        instruction = (
                "Break down the task into a list of dependent jobs. "
                "Return them in execution order."
                )
        
    elif independent:
        job_type = "independent jobs"
        
        instruction = (
                "Break down the task into a list of independent jobs. "
                "Return jobs that can be executed independently."
                )
               



    prompt = f"""
    issue: {issue}
                  
    This job cannot be completed in a single generation.
    
    It should be broken down into multiple {job_type}.

    {instruction}

    Return JSON only.
    
    Each job should include:
    
    - id: job id for the single generation job
    - instruction: single generation job instruction, should reference the "(job_id)" for all image inputs that depends on another job.
    - depends_on: job ids 
    
    """.strip()

                                                                                                                    
    return planner.run(prompt)































#issue = "in image aa2da replace the character on the left with the character in image 1412 and the character on the right with the character in image aa21sa, the poses should be identical to the poses in image aa2da" #"fix left hand in image 7124axa2a" #"generate an image of an anime character jumping" 

#issue = "generate 3 images of a dragon"
#issue = "generate an image of a dragon and another image of  a knight" 

#issue = "generate an image of a male tall character, then use the image to generate 3 dynamic poses of the same character" 


#issue = "generate an image of a character smiling, generate an image of the same character with an angry expression, generate an image of a mountain range. Use the mountain range image as the background for the angry character"#"generate an image of a character smiling,then generate an image changing the expression of the character to anger and then put in an image that has a mountain background" 

issue = """
    In im0, keep the room, lighting, camera angle, and both characters’ identities the same.

    Change the seated woman’s outfit to match the red dress in im1, but keep her current pose and facial expression.

    Replace the standing man’s head with the person from im2, but preserve the man’s body, suit, pose, and lighting.

    Add the small black dog from im3 sitting on the floor between them, scaled naturally and casting a believable shadow.

    Also remove the coffee cup from the table.

    Do not change anything else.
"""

issue = "In job_2, add the small black dog from im3 sitting on the floor between them, scaled naturally and casting a believable shadow, and remove the coffee cup from the table."


prompt = f"\n\nIssue:\n{issue} \no_think"

prompt = f"{system_prompt} {prompt}"


#TODO create multiple system.md files per task 
#TODO change run to get planner flags
planner_flags = planner.run(prompt) 

validate_planner_flags(planner_flags) 
sub_issues = break_generation_job(planner, issue, planner_flags) 





import pdb; pdb.set_trace() 
















    

        




#result = planner.run(issue)

#############################
#llm_prompts = {} 
#llm_prompts['modify_preexisting'] = {"prompt": 'is there an existing image to modify?', "response": None} 
#llm_promps['has_references'] = {"prompt": 'does the request include reference images?', "response": None}


















print (result) 

import pdb; pdb.set_trace() 













