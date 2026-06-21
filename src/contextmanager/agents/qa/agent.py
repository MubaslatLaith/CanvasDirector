import json

from contextmanager.agents.base_agent import BaseAgent

class QAAgent(BaseAgent):
    
    @property
    def name(self):
        return "qa"
    

    


    def run(self, question):
        response = self.complete(question)
                #f"Create an editing plan to resolve the following issue.\n\nIssue:\n{issue} \no_think"
                #)
        content = response.choices[0].message.content
        result = self._parse_json(content) 
        return result 



    def _parse_json(self, content):
        if isinstance(content, dict):
            return content
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            start = content.find("{")
            end = content.rfind("}") + 1
            if start == -1 or end == 0:
                raise ValueError(f"Task critic did not return JSON: {content}")
            return json.loads(content[start:end])

