

# src/agents/base/base_agent.py

from abc import ABC, abstractmethod
from pathlib import Path
from openai import OpenAI
from contextmanager.agents.openai_tool import OpenAITool
class BaseAgent(ABC):

    SYSTEM_PROMPT_FILE = "system.md"

    def __init__(self, base_url, api_key):
        self.openai_client = OpenAI(base_url=base_url, api_key=api_key)
        self.system_prompt = self.load_system_prompt()
        self.tools = {} 
        self.tools_openai_schema = [] 
        self.history = [] 

        self.system_prompt_message = [ {
            "role": "system",
            "content": self.system_prompt
        }] 


        self.curr_messages = self.system_prompt_message + self.history 
    

    @property
    @abstractmethod
    def name(self):
        pass

    def load_system_prompt(self):
        system_prompt_path = Path(f"{Path(__file__).parent}/{self.name}/prompts/{self.SYSTEM_PROMPT_FILE}")
        return system_prompt_path.read_text(encoding="utf-8")

    def complete(self, user_content, temperature = None):
       user_message = [ 
            {
                "role": "user",
                "content": user_content,
            },
        ] 
       messages = self.curr_messages + user_message 

       kwargs = {
               "model": "default",
               "messages": messages,
               "tools": self.tools_openai_schema,
               "tool_choice": "auto",
               }

       if temperature is not None:
           kwargs["temperature"] = temperature


        response = self.openai_client.chat.completions.create(**kwargs


       """
       response = self.openai_client.chat.completions.create(
               model="default",
               messages=messages, 
               tools=self.tools_openai_schema,
               tool_choice="auto",
               )
       """
       return response 


    @abstractmethod
    async def run(self, **kwargs):
        pass

    def register_tool(self, tool: OpenAITool):
        self.tools[tool.name] = tool
        self.tools_openai_schema.append(tool.schema)

