

import json

from contextmanager.agents.base_agent import BaseAgent


class ExecutorAgent(BaseAgent):

    @property
    def name(self):
        return "executor"

    async def run(self, command):
        response = self.complete(command)

        tool_calls = response.choices[0].message.tool_calls

        if not tool_calls:
            return {
                "success": False,
                "error": "No tool call returned",
                "response": response.choices[0].message.content,
            }
        
        tool_call = tool_calls[0]
        
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if tool_name not in self.tools:
            return {
                "success": False,
                "error": f"Tool not registered: {tool_name}",
                "arguments": arguments,
            }




        tool = self.tools[tool_name]
        result = await tool.function(**arguments)

        return {
            "success": True,
            "tool": tool_name,
            "arguments": arguments,
            "result": result,
        } 



