class InvokeUIBridge:
    def __init__(self, page):
        self.page = page
        
        self.parameters = {} 
        self.parameters['positive_prompt'] = 'setPositivePrompt'  
        self.parameters['steps'] = 'setSteps'    
    def login(self):
        pass 
    
    def wait_client_state_saved(self, timeout: int = 20000):
        return self.page.expect_request_finished(lambda r: "client_state" in r.url and r.method in ("POST", "PUT"), timeout=timeout)

    def get_params(self):
        return self.page.evaluate("window.__invokeBridge.params.get()") 
    
    def set_parameter(self, parameter, value):
        return self.page.evaluate(f'v => window.__invokeBridge.params.{self.parameters[parameter]}(v)', value)

    def create_canvas_entity_from_selected_image(self, type_: str = "raster_layer"):
        return self.page.evaluate(
        """
        async (type_) => {
        return await window.__invokeBridge.image.createNewCanvasEntityFromSelectedImage(type_);
        }
        """,
        type_, 
        )
        
        #self.page.evaluate(f'window.__invokeBridge.image.createNewCanvasEntityFromSelectedImage({type})')


