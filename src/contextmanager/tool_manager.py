class ToolManager:      
    def __init__(self):  
        self.tools = {} 
    
    def register(self, task, tool): 
        self.tools[task] = tool  

    def get(self, name):   
        if name not in self.tools:    
            raise ValueError(f"Unknown tool: {name}") 
        return self.tools[name]  
    
    def list_tools(self):  
        return list(self.tools.keys())   
    
    def run(self, task, req):  
        tool = self.get(task) 
        return tool.run(task, req)
