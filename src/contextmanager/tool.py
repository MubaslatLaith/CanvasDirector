from pydantic import BaseModel
class Tool(BaseModel):
    task: str
    processor: object
