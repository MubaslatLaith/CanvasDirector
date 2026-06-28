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
mask = Image.open('/workspace/CanvasDirector/sam3_mask0.png')

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

issue = "in image aa2da replace the character on the left with the character in image 1412 and the character on the right with the character in image aa21sa, the poses should be identical to the poses in image aa2da" #"fix left hand in image 7124axa2a" #"generate an image of an anime character jumping" 

system_prompt = "" 
system_prompt += """You are an image editing planner.

Your task is to convert a user's image editing request into a sequence of executable operations.

You do not execute operations.
You only produce a plan.

Planning guidelines:
    - Produce the simplest valid plan that accomplishes the requested edit.
    - Break complex tasks into multiple operations when necessary.
    - Preserve dependencies between operations.
    - Reuse existing images whenever possible.
    - Only use the operations and fields that are available.
    - Do not invent unsupported operations.
    - Do not invent image names or outputs that cannot be produced by previous operations.
    - If an operation requires the output of a previous operation, express that dependency explicitly.

    Return only valid JSON following the required schema.

    If no valid plan can be produced using the available operations, return:

    {
      "success": false,
        "reason": "<brief explanation>",
          "operations": []
          }"""

system_prompt += """\n Operation: generation_request

Arguments:
    - job_id: string
    - raster_images: list[string]
    - reference_images: list[string]
    - mask_to_edit: list[string]
    - generation_parameters:
            positive_prompt: string
            steps: integer
Behavior:
    - If mask_to_edit is non-empty, performs localized inpainting.
    - If mask_to_edit is empty, edits the entire image.
    - reference_images are used as guidance.
    - raster_images are placed on top of one another with the latest taking priority""" 

system_prompt += """\n Available operations

Operation: segment

Arguments:
    - image_name: string
    - segmentation_prompt: string

    Returns:
    - output_name (mask image)"""


system_prompt = """
You are a planning feature classifier for an image editing system.

Your job is to analyze the user request and current task context, then return structured planning features that help route the task.

You do not create an edit plan.
You do not call tools.
You do not execute operations.

Answer only with valid JSON.

Classify only what can be inferred from the request and provided context.
Do not invent missing images, masks, references, or capabilities.

Important:
    - Deterministic facts such as whether images or references were provided may be included in the context.
    - If a value is already provided in the context, use it.
    - If a value cannot be determined, use null.
    - Use booleans for yes/no features.
    - Keep explanations short.

    Return schema:

    {
      "modify_preexisting": boolean | null,
        "has_references": boolean | null,
          "localized_edit": boolean | null,
            "target_exists": boolean | null,
              "segmentable": boolean | null,
                "multiple_regions": boolean | null,
                  "sequential_required": boolean | null,
                    "needs_reference_guidance": boolean | null,
                      "requires_full_regeneration": boolean | null,
                        "reason": {
                            "modify_preexisting": string,
                                "has_references": string,
                                    "localized_edit": string,
                                        "target_exists": string,
                                            "segmentable": string,
                                                "multiple_regions": string,
                                                    "sequential_required": string,
                                                        "needs_reference_guidance": string,
                                                            "requires_full_regeneration": string
                                                              }
                                                              }

                                                              Feature meanings:

                                                              - modify_preexisting:
                                                                True if there is an existing base image to edit.

                                                                - has_references:
                                                                  True if one or more reference images are provided.

                                                                  - localized_edit:
                                                                    True if the requested change can be made within a bounded image region while leaving the rest unchanged.

                                                                    - target_exists:
                                                                      True if the object or region to modify already exists in the base image.

                                                                      - segmentable:
                                                                        True if the target object or region can likely be selected with a text segmentation prompt.

                                                                        - multiple_regions:
                                                                          True if the task requires modifying more than one separate object or region or entity.

                                                                          - sequential_required:
                                                                            True if edits should be applied one after another because later edits should use the result of earlier edits.

                                                                            - needs_reference_guidance:
                                                                              True if the task requires reference images for identity, appearance, pose, style, or object guidance.

                                                                              - requires_full_regeneration:
                                                                                True if the request cannot be completed with localized masked edits and likely requires modifying or regenerating the whole image.

                                                                                Rules:
                                                                                - Do not output a plan.
                                                                                - Do not output operations.
                                                                                - Do not recommend tools.
                                                                                - Do not assume a region is segmentable if it is abstract, missing, hidden, or not visually present.
                                                                                - If localized_edit is false, segmentable should usually be false.
                                                                                - If target_exists is false, segmentable should usually be false.
                                                                                - If multiple independent regions are edited on the same base image, sequential_required is usually true unless the system can merge outputs.
                                                                                - If the request says replace an object/person with a reference, needs_reference_guidance is true.
                                                                                """


prompt = f"\n\nIssue:\n{issue} \no_think"



system_prompt = "break the task into seperate tasks, each task should address a single region"


prompt = f'{system_prompt}\n {prompt}'



result = planner.run(prompt) 







#result = planner.run(issue)

#############################
#llm_prompts = {} 
#llm_prompts['modify_preexisting'] = {"prompt": 'is there an existing image to modify?', "response": None} 
#llm_promps['has_references'] = {"prompt": 'does the request include reference images?', "response": None}


















print (result) 

import pdb; pdb.set_trace() 













