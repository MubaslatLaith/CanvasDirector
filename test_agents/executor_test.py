#from contextmanager.agents.base_agent import BaseAgent






from openai import OpenAI
import json
openai_client = OpenAI(
    base_url = "http://127.0.0.1:8001/v1",
    api_key = "sk-no-key-required",
)



tools = [
    {
        "type": "function",
        "function": {
            "name": "segment",
            "description": "returns mask_id for the mask which highlights the area determined by mask_prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "image_id": {
                        "type": "string",
                        "description": "image_id to mask"
                    },
                    "prompt": {
                        "type": "string",
                        "description": "mask prompt"
                    }
                },
                "required": ["image_id", "prompt"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "txt2img",
            "description": "generate a new image from a text prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "generation prompt"
                    }
                },
                "required": ["prompt"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "inpaint",
            "description": "generate masked region in an image based on a prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "image_id": {
                        "type": "string",
                        "description": "image_id to inpaint"
                    },
                    "mask_id": {
                        "type": "string",
                        "description": "mask_id to inpaint"
                    },
                    "prompt": {
                        "type": "string",
                        "description": "inpaint prompt"
                    }
                },
                "required": ["image_id", "mask_id", "prompt"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ref2image",
            "description": "generate a new image from a text prompt while conditioning on up to 5 reference images",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "generation prompt"
                    },
                    "reference_image_ids": {
                        "type": "array",
                        "description": "list of up to 5 reference image ids",
                        "items": {
                            "type": "string"
                        },
                        "maxItems": 5
                    }
                },
                "required": ["prompt", "reference_image_ids"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "crop_masked",
            "description": "crop the region defined by a mask and return a new image_id containing only the masked area",
            "parameters": {
                "type": "object",
                "properties": {
                    "image_id": {
                        "type": "string",
                        "description": "source image_id"
                    },
                    "mask_id": {
                        "type": "string",
                        "description": "mask defining the crop region"
                    }
                },
                "required": ["image_id", "mask_id"],
            },
        },
    }
]


system_prompt = """
You are an image editing planner.

Your job is to solve the user's request by calling the available tools.

Available tools:

- segment
- txt2img
- inpaint
- ref2image
- crop_masked

Rules:

- Call tools instead of describing what should happen.
- Never output JSON plans.
- Never explain your reasoning.
- Never describe tool calls in text.
- If a region must be edited, first obtain a mask using segment. Then use inpainting using a second function call. Assume mask exists following the call for the segment method and assign an arbitrary id for the inpaint call 
- Use inpaint only when a mask exists.
- Use txt2img when creating a new image from scratch.
- Use ref2image when one or more reference images are provided.
- Use crop_masked only when the user wants an object extracted or isolated.
- Perform all necessary tool calls to complete the request.
- After the final tool call, provide a brief completion message.

You are an executor, not a planner document generator.
""" 



def test(scenario, openai_client):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": scenario 
        }
    ]



    response = openai_client.chat.completions.create(
        model="default",
        messages=messages, #{"role": "user", "content": "What's the weather in Perth right now?"}],
        tools=tools,
        tool_choice="auto",
    )
    #print(response)
    tool_calls = response.choices[0].message.tool_calls

    if tool_calls is None:
    # No tool call
        print(response.choices[0].message.content)
        return 
    for i in range (len(response.choices[0].message.tool_calls)):
        tool_call = response.choices[0].message.tool_calls[i]
        print(tool_call.function.name, tool_call.function.arguments)
    
    print ('_______________')

s1 = "Create a futuristic city at night."
s2 = "Fix the hands in image_123" 
s3 = "Remove the backpack from image_123" 
s4 = "Extract the shirt from image_123"
s5 = "Generate a product shot using reference images ref1 and ref2" 
s6 = "Replace the shirt in image_2812 with a black leather jacket, the shirt mask has the id zb182" 
s7 = "Make the dog wear sunglasses" 


s =  s1
print(s)
test(s, openai_client)

s =  s2
print(s)
test(s, openai_client)

s =  s3
print(s)
test(s, openai_client)


s =  s4
print(s)
test(s, openai_client)

s =  s5
print(s)
test(s, openai_client)

s =  s6
print(s)
test(s, openai_client)


s =  s7
print(s)
test(s, openai_client)


