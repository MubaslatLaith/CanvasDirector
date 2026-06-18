
from contextmanager.agents.test.agent import TestAgent
from contextmanager.agents.openai_tool import OpenAITool



async def dummy_function():
    pass


def main():

    agent = TestAgent(
        base_url="http://localhost:8000/v1",
        api_key="dummy",
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
    

if __name__ == "__main__":
    main()
