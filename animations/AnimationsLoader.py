import os
import importlib
from animations.AnimationBase import AnimationBase 
import utils.ModuleLoader as ModuleLoader 

#TODO: Since only scheduled apps will run, the loading of executables should be done by the schedule somehow
def load_animations(path, module, matrix, parameters_global):
    ModuleLoader.load_modules_recursiv(path, module)
    
    name_and_classes = {cls.__name__ : cls for cls in AnimationBase.__subclasses__()}
    name_and_executables = {}
    
    # Load all classes. Some of them might not have parameters, but are in the scheduler
    for name in name_and_classes:
        array_of_parameters = parameters_global.get(name, {})
        class_parameters = {}
        for parameter in array_of_parameters:
            class_parameters[parameter[0]] = parameter[1]
        
        name_and_executables[name] = name_and_classes[name](matrix, class_parameters)
    
    
    # Check for different versions of the apps, which must have a slash
    for app_name in parameters_global.keys():
        if app_name == "scheduler" or app_name == "wordclock" or not "/" in app_name:
            continue 
        
        class_name = app_name.split("/")[0]
        array_of_parameters = parameters_global.get(app_name, {})
        app_parameters = {}
        for parameter in array_of_parameters:
            app_parameters[parameter[0]] = parameter[1]
        
        name_and_executables[app_name] = name_and_classes[class_name](matrix, app_parameters)
     
    return name_and_executables

                
                
                
                
          