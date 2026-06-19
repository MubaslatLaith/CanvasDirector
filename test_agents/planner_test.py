import asyncio


from contextmanager.agents.quality_critic.agent import QualityCriticAgent
from contextmanager.agents.planner.agent import PlannerAgent
from contextmanager.agents.openai_tool import OpenAITool

from contextmanager.apiclient.invokeai.client import InvokeAIClient



async def main():
    base_url = "http://127.0.0.1:8001/v1"
    api_key = "sk-no-key-required"

    """
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
    output_board_name = "image_to_edit_board" #
    #output_board_name = "In Board"
    output_image_name = api_client.boards.get_image_ids_by_board_name (output_board_name)
    print('output image')
    print(output_image_name)
    i= 0
    output_image_url = api_client.images.get_image_url(output_image_name[i])
    print (output_image_url) 

    result = agent.run(output_image = output_image_url)
    #result = agent.run("in image asjdlak, the had mask is oiasdoajs, prompt fix hand")#Inpaint image asjdlak with mask oiasdoajs and prompt aoisdoakwmd")
    print(result)
    """
    planner_agent = PlannerAgent(
            base_url=base_url,
            api_key=api_key,
            )
    
    #image_to_edit_board
    issues1 = ['Inconsistent shoe colors: The left shoe is white while the right shoe is light blue/grey.', "Left hand anatomy: The fingers on the character's right hand (viewer's left) appear slightly clumped and malformed.", "Right hand definition: The fingers on the character's left hand (viewer's right) are somewhat flat and lack distinct knuckle definition."]
    

    #In Board
    issues2 = ["The brown strap hanging from the backpack/belt area appears disconnected or ambiguously attached to the character's clothing.", "The character's left hand (viewer's right) has a slightly indistinct wrist connection to the arm.", 'Background buildings on the right side lack clear architectural definition and appear somewhat generic.', 'The speed lines cut off abruptly at the image borders, creating a harsh edge effect.']
    
    issues = issues1 + issues2 


    issues = []
    issues.append ("the character in the generated image has an extra button that does not match the reference images")
    issues.append ("the character hair style is different than the hair style in the reference image")
    issues.append ("the character pose does not match the pose in the reference image") 



    for i in range(len(issues)):
        print('_____')
        print(i)
        issue = issues[i]

    
        result = planner_agent.run(issue) 
        print(issue)
        print(result)
    import pdb; pdb.set_trace() 
    

if __name__ == "__main__":
    asyncio.run(main())

