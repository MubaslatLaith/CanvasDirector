import asyncio


from contextmanager.agents.quality_critic.agent import QualityCriticAgent
from contextmanager.agents.openai_tool import OpenAITool

from contextmanager.apiclient.invokeai.client import InvokeAIClient

async def main():
    base_url = "http://127.0.0.1:8001/v1"
    api_key = "sk-no-key-required"


    agent = QualityCriticAgent(
        base_url=base_url,
        api_key=api_key,
    )
    
    # get input output urls 
    INVOKE_URL = "http://127.0.0.1:9091"
    USERNAME = "email@email.email"
    PASSWORD = "weakpassword"

    api_client = InvokeAIClient(INVOKE_URL)
    user = api_client.login(USERNAME, PASSWORD)

    print ('t2i output image') 
    output_board_name = "In Board"
    output_image_name = api_client.boards.get_image_ids_by_board_name (output_board_name)
    print('output image')
    print(output_image_name)
    i= 0
    output_image_url = api_client.images.get_image_url(output_image_name[i])
    print (output_image_url) 

    result = agent.run(output_image = output_image_url)
    #result = agent.run("in image asjdlak, the had mask is oiasdoajs, prompt fix hand")#Inpaint image asjdlak with mask oiasdoajs and prompt aoisdoakwmd")
    print(result)




if __name__ == "__main__":
    asyncio.run(main())

