import io
import base64
from typing import Literal
import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextmanager.perception_tools.sam3 import SAM3Tool 
from contextmanager.perception_tools.requests.segment import SegmentRequest
from contextmanager.tool_manager import ToolManager
from contextmanager.tool import Tool 
# t2i 
# ref2i 
# inpaint 
# get depth 
# get pose 
# detect object 

offload = True 
device = "cuda"

#TODO modify here for what tasks to define, tools to load 
sam_3_tool = SAM3Tool(device)

TOOLS = []
TOOLS.append(Tool(task = 'segment', processor = sam_3_tool))




app = FastAPI(title="Tool Manager API")
manager = ToolManager() 

@app.on_event("startup")
def startup():
    # register all tools 
    for i in range(len(TOOLS)): 
        TOOLS[i].processor.load() 
        manager.register(TOOLS[i].task, TOOLS[i].processor) 

# TODO update for info to get from API 
@app.get("/")
def root():
    out = {} 
    out['status'] = 'running'
    out['tools'] = [TOOLS[i].task for i in range(len(TOOLS))]  
    return out 



@app.post("/segment")
def segment(req: SegmentRequest):
    result = manager.run("segment", req)
    
    out = result 
    return out 



if __name__ == "__main__":
    uvicorn.run(
            "tools_app:app",
            host = "0.0.0.0",
            port = 8000,
            reload = False
            )
