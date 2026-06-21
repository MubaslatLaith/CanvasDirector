
from pydantic import BaseModel
class SegmentRequest(BaseModel):     
    prompt: str  
    #image_base64: str
    image_url: str
    box: list[float] | None = None
    threshold: float =  0.5
    mask_threshold: float =  0.5
