import os
from openai import OpenAI

LLM_URL = "http://localhost:8888/v1"
API_KEY = "sk-unsloth-48e3c7859e4b03619ad0247c4f54c117"

client = OpenAI(
    base_url= LLM_URL,
    api_key= API_KEY,
)


response = client.chat.completions.create(
    model="unsloth/Qwen3.5-9B-GGUF (Q8)", #"default",                               # the name you gave the model in unsloth or default
    messages=[
        {"role": "user", "content": "Give me two facts about Paris"}
    ],
    stream = True,
)


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
#print(response)
#print(response.choices[0].message.content)


