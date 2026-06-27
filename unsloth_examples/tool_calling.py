import os
from openai import OpenAI

LLM_URL = "http://localhost:8888/v1"
API_KEY = "sk-unsloth-48e3c7859e4b03619ad0247c4f54c117"


import requests

r = requests.post(
    "http://localhost:8888/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "default",
        "messages": [{"role": "user", "content": "Say hello"}],
        "stream": False,
    },
)

print(r.status_code)
print(r.headers.get("content-type"))
print(r.text[:1000])




import pdb; pdb.set_trace() 
client = OpenAI(
    base_url= LLM_URL,
    api_key= API_KEY,
)

class FunctionTool: 
    def __init__(self, type_, name, description): 
        self.TYPE = "function" 
        self.tool_dict = {} 
        self.tool_dict['type'] = self.TYPE 
        self.tool_dict[self.TYPE] = {}
        self.tool_dict[self.TYPE]['name'] = name
        self.tool_dict[self.TYPE]['description'] = description 
        self.tool_dict[self.TYPE]['parameters'] = {} 
        self.tool_dict[self.TYPE]['parameters'] ['type'] = 'object' 
        self.tool_dict[self.TYPE]['parameters']['properties'] = {} 
        self.tool_dict[self.TYPE]['parameters']['required'] = [] 
    def add_parameter(self, name, type_, description, required):
        parameter = {} 
        parameter ['type'] = type_
        parameter ['description'] = description 
        self.tool_dict[self.TYPE]['parameters']['properties'][name] = parameter
        if required: 
            self.tool_dict[self.TYPE]['parameters']['required'].append(name) 

    def to_dict(self):
        return self.tool_dict 

tool1 = FunctionTool("function", "inpaint", "inpaint a specific region of an image based on a mask and a text prompt") 
tool1.add_parameter("prompt", "string", "text prompt for the inpainting process", True) 
tool1.add_parameter("inpainting_mask", "string", "inpainting mask id", True) 
tool1.add_parameter("image", "string", "image to inpaint id", True) 



tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g. 'Paris'"},
                },
                "required": ["city"],
            },
        },
    }
]


print (tool1.to_dict())
print(tools[0])


tools.append(tool1.to_dict()) 

q = "fix hand in image of id image012X using mask212s using the inpainting tool"

messages = [
    {
        "role": "system",
        "content": """
You are not a chatbot.

You are a JSON planner for an image editing agent.

You cannot execute tools.
You only choose the next tool call.

Ignore any prior assumptions about available tools.

Available tools:
- inpaint(prompt, image_id, inpainting_mask_id)
- generate_mask(image_id, region_description_prompt)
Return only valid JSON.
No markdown.
No explanation.
No <think>.

Schema:
{
  "tool": "inpaint",
  "arguments": {
    "prompt": "string",
    "image_id": "string",
    "inpainting_mask_id": "string"
  }
}
"""
    },
    {
        "role": "user",
        "content": """
the hand in image of id image012X requires fixing 
"""
    }
]


response = client.chat.completions.create(
    model="default",
    messages=messages, #[{"role": "user", "content": q}],
    #tools=tools,
    #tool_choice="auto",
    stream = False, 
    extra_body={   # Prevents thinking tokens from forcing a stream
        "chat_template_kwargs": {
            "thinking": False
        }}
    #stream = True, 
)

import json
import re

def parse_sse_text(raw):
    parts = []

    for line in raw.splitlines():
        line = line.strip()

        if not line.startswith("data: "):
            continue

        payload = line[len("data: "):]

        if payload == "[DONE]":
            break

        try:
            obj = json.loads(payload)
        except json.JSONDecodeError:
            continue

        choices = obj.get("choices", [])
        if not choices:
            continue

        delta = choices[0].get("delta", {})
        content = delta.get("content")

        if content:
            parts.append(content)

    return "".join(parts)

out = parse_sse_text(response)
print(out)
import pdb;pdb.set_trace()

tool_call = response.choices[0].message.tool_calls[0]
print(tool_call.function.name, tool_call.function.arguments)




"""
def stream_openai_text(stream):
    full_text = ""

    for chunk in stream:
        choices = getattr(chunk, "choices", None)
        if not choices:
            continue

        delta = getattr(choices[0], "delta", None)
        if not delta:
            continue

        content = getattr(delta, "content", None)
        if not content:
            continue

        full_text += content
        print(content, end="", flush=True)

    print()
    return full_text

out = stream_openai_text(response)
"""
#print(response)
#print(response.choices[0].message.content)


