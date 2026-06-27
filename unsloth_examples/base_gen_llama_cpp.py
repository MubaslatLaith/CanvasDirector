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
                    "image_id": {"type": "string", "description": "image_id to mask"},
                    "prompt": {"type": "string", "description": "mask prompt"}
                },
                "required": ["image_id","prompt"],
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
                    "image_id": {"type": "string", "description": "image_id to inpaint"},
                    "mask_id": {"type": "string", "description": "mask_id to inpaint"},
                    "prompt": {"type": "string", "description": "inpaint prompt"}
                },
                "required": ["mask_id","image_id","prompt"],
            },
        },
    }
]


messages = [
    {
        "role": "system",
        "content": """
You are not a chatbot.

You are  an image editing agent.

You only choose the next tool call.

"""
    },
    {
        "role": "user",
        "content": """
the hand in image of id image012X requires fixing 
"""
    }
]



response = openai_client.chat.completions.create(
    model="default",
    messages=messages, #{"role": "user", "content": "What's the weather in Perth right now?"}],
    tools=tools,
    tool_choice="auto",
)
print(response)
tool_call = response.choices[0].message.tool_calls[0]
print(tool_call.function.name, tool_call.function.arguments)
