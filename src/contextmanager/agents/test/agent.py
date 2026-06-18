
from contextmanager.agents.base_agent import BaseAgent

class TestAgent(BaseAgent):
    @property
    def name(self):
        return "test"

    async def run(self, state):
        pass

