
import asyncio

from contextmanager.agents.executor.agent import ExecutorAgent
from contextmanager.agents.openai_tool import OpenAITool


async def inpaint(image_id, mask_id, prompt):
    print(f"image_id={image_id}")
    print(f"mask_id={mask_id}")
    print(f"prompt={prompt}")

    return {
        "image_id": "edited_image_001"
    }


async def main():
    base_url = "http://127.0.0.1:8001/v1"
    api_key = "sk-no-key-required"


    agent = ExecutorAgent(
        base_url=base_url,
        api_key=api_key,
    )

    tool = OpenAITool(
        name="inpaint",
        description="inpaint an image",
        function=inpaint,
    )

    tool.add_parameter(
        "image_id",
        "string",
        "image id",
    )

    tool.add_parameter(
        "mask_id",
        "string",
        "mask id",
    )

    tool.add_parameter(
        "prompt",
        "string",
        "inpaint prompt",
    )

    agent.register_tool(tool)

    result = await tool.function(
        image_id="asjdlak",
        mask_id="oiasdoajs",
        prompt="aoisdoakwmd",
    )
    

    print("direct tool call")
    print(result)

    print("executor tool call") 
    result = await agent.run("in image asjdlak, the had mask is oiasdoajs, prompt fix hand")#Inpaint image asjdlak with mask oiasdoajs and prompt aoisdoakwmd")
    print(result)




if __name__ == "__main__":
    asyncio.run(main())
