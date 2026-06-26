from enum import Enum
from typing import Any
from pydantic import BaseModel, Field, ConfigDict
from PIL import Image


class GenerationParameters(BaseModel):
    steps: int
    positive_prompt: str

    
class InvokeAIGenerationRequest(BaseModel):
    job_id: str
    
    # image names in invokai 
    images_to_edit: list[str] = Field(default_factory=list)
    masks_to_edit: list[str] = Field(default_factory=list)
    reference_images: list[str] = Field(default_factory=list)
    
    generation_parameters: GenerationParameters = Field(default_factory=GenerationParameters)


