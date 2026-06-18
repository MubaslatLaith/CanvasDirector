

# src/agents/base/base_agent.py

from abc import ABC, abstractmethod
from pathlib import Path


class BaseAgent(ABC):

    SYSTEM_PROMPT_FILE = "system.md"

    def __init__(self, base_url, api_key):
        self.openai_client = OpenAI(base_url, api_key)
        self.system_prompt = self.load_system_prompt()
        self.tools_schema = [] 
        self.history = [] 
        self.curr_messages = self.system_prompt + self.history 
    @property
    @abstractmethod
    def name(self):
        pass

    def load_system_prompt(self):i
        system_prompt_path = Path(f"{Path(__file__).parent.parent}/{self.name}/prompts/{self.SYSTEM_PROMPT_FILE}")
        return prompt_path.read_text(encoding="utf-8")

    async def complete(self, user_content):
       user_message = [ 
            {
                "role": "user",
                "content": user_content,
            },
        ] 

        messages = self.curr_messages + user_message 
        

        response = self.openai_client.chat.completions.create(
            model="default",
            messages=messages, 
            tools=self.tools_schema,
            tool_choice="auto",
        )
        return response 


    @abstractmethod
    async def run(self, state):
        pass

    def register_tool(self, tool: OpenAITool):
        self.tools_openai_schema.append(tool.schema)

