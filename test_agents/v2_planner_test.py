import asyncio


from contextmanager.agents.quality_critic.agent import QualityCriticAgent
from contextmanager.agents.planner.agent import PlannerAgent
from contextmanager.agents.openai_tool import OpenAITool

from contextmanager.apiclient.invokeai.client import InvokeAIClient

class GenerationState:
    def __init__ (self, user_prompt, user_supplied_ref_images=[]):    
        self.user_prompt = user_prompt
        self.user_supplied_ref_imaged = self.user_supplied_ref_images
        if len(user_supplied_ref_images == 0):    
            self.curr_available_modes = ["textToImage"] 
        else:    
            self.curr_available_modes = ["referenceToImage"] 
            if self._edit_can_be_localized(self.user_prompt):
                self.curr_available_modes += ["inpaint", "inpaint_with_referenceToImage"]

    def _edit_can_be_localized(self, prompt):
        system_prompt = "can edit be localized?" 
        #investigate prompt(i.e., edit is restricted to a specific region or object in an image) 
        #investigate image (i.e., mask can be obtained)
    
    :
        




async def main():
    base_url = "http://127.0.0.1:8001/v1"
    api_key = "sk-no-key-required"

   planner_agent = PlannerAgent(
            base_url=base_url,
            api_key=api_key,
            )
    
       
    
        

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

