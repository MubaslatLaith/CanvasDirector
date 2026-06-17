import os
from openai import OpenAI

LLM_URL = "http://localhost:8888/v1"
API_KEY = "none"#"sk-unsloth-48e3c7859e4b03619ad0247c4f54c117"

import json
from types import SimpleNamespace
def ns(obj):

    """Convert nested dict/list into attribute-access objects."""

    if isinstance(obj, dict):

        return SimpleNamespace(**{k: ns(v) for k, v in obj.items()})

    if isinstance(obj, list):

        return [ns(v) for v in obj]

    return obj

def parse_sse_chat_completion(raw):
    content_parts = []
    final_chunk = None

    for line in raw.splitlines():
        line = line.strip()

        if not line.startswith("data: "):
            continue

        payload = line[len("data: "):]

        if payload == "[DONE]":
            break

        obj = json.loads(payload)

        if obj.get("type") == "tool_status":
            continue

        choices = obj.get("choices", [])
        if not choices:
            continue

        choice = choices[0]
        delta = choice.get("delta", {})

        if "content" in delta:
            content_parts.append(delta["content"])

        if choice.get("finish_reason"):
            final_chunk = obj

    response_dict =  {
        "id": final_chunk.get("id") if final_chunk else None,
        "object": "chat.completion",
        "created": final_chunk.get("created") if final_chunk else None,
        "model": final_chunk.get("model") if final_chunk else None,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "".join(content_parts),
                },
                "finish_reason": final_chunk["choices"][0].get("finish_reason") if final_chunk else None,
            }
        ],
    }
    return ns(response_dict) 


client = OpenAI(
    base_url= LLM_URL,
    api_key= API_KEY,
)


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

response = client.chat.completions.create(
    model="default",
    messages=[{"role": "user", "content": "What's the weather in Perth right now?"}],
    tools=tools,
    tool_choice="auto",
)

import pdb; pdb.set_trace()
response = parse_sse_chat_completion(response)



tool_call = response.choices[0].message.tool_calls[0]

print(tool_call.function.name, tool_call.function.arguments)






"""
messages = [

    {"role": "user", "content": "Give me two facts about Paris"}

]


response = client.chat.completions.create(
    model= "unsloth/Qwen3.5-9B-GGUF", #"default",
    messages=messages, #[{"role": "user", "content": q}],
    stream = False, 
)


response = parse_sse_chat_completion(response)
"""

import pdb; pdb.set_trace() 
