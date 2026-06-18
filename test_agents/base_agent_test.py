
from contextmanager.agents.test.agent import TestAgent
from contextmanager.agents.openai_tool import OpenAITool



async def dummy_function():
    pass


def main():
    
    base_url = "http://127.0.0.1:8001/v1"
    api_key = "sk-no-key-required"

    agent = TestAgent(
        base_url=base_url,
        api_key=api_key,
    )

    print("System Prompt:")
    print(agent.system_prompt)

    tool = OpenAITool(
        name="segment",
        description="segment an image",
        function=dummy_function,
    )

    tool.add_parameter(
        name="image_id",
        parameter_type="string",
        description="image id",
    )

    tool.add_parameter(
        name="prompt",
        parameter_type="string",
        description="mask prompt",
    )

    agent.register_tool(tool)

    print("\nRegistered Tools:")
    print(agent.tools)

    print("\nOpenAI Schemas:")
    print(agent.tools_openai_schema)
    

    response = agent.complete ("hi how are you?") 

    print(response) 


if __name__ == "__main__":
    main()
