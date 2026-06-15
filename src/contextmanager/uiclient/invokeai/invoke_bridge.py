class InvokeUIBridge:
    def __init__(self, page):
        self.page = page
        
        self.parameters = {} 
        self.parameters['positive_prompt'] = 'setPositivePrompt'  
        self.parameters['steps'] = 'setSteps'    


    def login(self):
        pass 
    
    def delete_all_ref_images(self):
        return self.page.evaluate( "window.__invokeBridge.image.deleteAllGlobalReferenceImages()")
            
    def canvas_discard_all(self):
        return self.page.evaluate("window.__invokeBridge.stagingArea.discardAll()")


    def reset_generation_settings(self):
        self.page.evaluate("window.__invokeBridge.params.resetGenerationSettings()")

    def create_global_reference_image_from_image_name(self, image_name):
        return self.page.evaluate(
                "imageName => window.__invokeBridge.image.createGlobalReferenceImageFromImageName(imageName)",
                image_name,
                )

    def reset_canvas(self):
        return self.page.evaluate("window.__invokeBridge.image.resetCanvas()") 
    
    def save_selected_to_gallery(self, board_id):
        return self.page.evaluate("boardId => window.__invokeBridge.stagingArea.saveSelectedToGallery(boardId)", board_id)
    def create_canvas_entity_from_image_name(self, type_, image_name):
        return self.page.evaluate(
        """
        async ({ imageName, layerType }) => {
        await window.__invokeBridge.image.createNewCanvasEntityFromImageName(
        imageName,
        layerType
        );
        }
        """,
        {
            "imageName": image_name,
            "layerType": type_
            }
        )

    def canvas_canAcceptSelected(self):
        return self.page.evaluate("window.__invokeBridge.stagingArea.canAcceptSelected()")
    
    def canvas_acceptSelected(self):
        return self.page.evaluate("window.__invokeBridge.stagingArea.acceptSelected()")

    def invoke(self):
        if self.page.evaluate("window.__invokeBridge.queue.isDisabled()"):
            raise RuntimeError("Cannot invoke")
        
        self.page.evaluate("window.__invokeBridge.queue.invoke()")
        
        #while (self.page.evaluate("window.__invokeBridge.queue.isLoading()")):
        while (not self.canvas_canAcceptSelected()):
            print('Invoking')
        print ('invoke complete') 



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


