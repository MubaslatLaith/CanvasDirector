class OpenAITool:
    def __init__(self, name, description, function):
        self.name = name
        self.description = description
        self.function = function

        self.properties = {}
        self.required = []

    def add_parameter(
        self,
        name,
        parameter_type,
        description,
        required=True,
    ):
        self.properties[name] = {
            "type": parameter_type,
            "description": description,
        }

        if required:
            self.required.append(name)

    @property
    def schema(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": self.properties,
                    "required": self.required,
                },
            },
        }
    
    #async def execute(self, arguments):
    #    return await self.function(**arguments)
