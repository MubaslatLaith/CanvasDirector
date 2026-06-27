class GenerationState:
    def __init__ (self, user_prompt, user_supplied_ref_images=[]):
        self.user_prompt = user_prompt 
        self.user_supplied_ref_imaged = user_supplied_ref_images 

        self.prev_step = None 
        self.curr_step = None 
        
    def _checkout_current_step(self):
        pass 
    

    def _can_edit_be_localized(self, edit_prompt):
        if self.prev_step == None:
            return False
        
        self.mask = self.get_mask(self.prev_step, edit_prompt)

        if self.mask == None:
            return False 
        





