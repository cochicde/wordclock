'''
Created on Apr 24, 2020

@author: cabral
'''

import utils.ModuleLoader as ModuleLoader

class LayoutBase:
    
    def __init__(self, language):
        self.language =  language
        
    # Given a time, it returns a tupple ([]LayoutWord, int) where the second element is the 1-minute grain (0 - 4) 
    def get_words_and_points_from_time(self, time):
        pass
    
def get_layout_instance(class_name):
    # Create loader base to load all at the once
    ModuleLoader.load_modules_recursiv("./layout", "layout")
    name_and_classes = {cls.__name__ : cls for cls in LayoutBase.__subclasses__()}
    return name_and_classes[class_name]