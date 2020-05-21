import os
import importlib
from animations.AnimationBase import AnimationBase 

def load_modules(path, module, matrix, parameters_global):
    load_modules_recursiv(path, module)
    
    name_and_classes = {cls.__name__ : cls for cls in AnimationBase.__subclasses__()}
    name_and_executables = {}
    for name in name_and_classes:
        array_of_parameters = parameters_global.get(name, {})
        class_parameters = {}
        for parameter in array_of_parameters:
            class_parameters[parameter[0]] = parameter[1]
        
        name_and_executables[name] = name_and_classes[name](matrix, class_parameters)
        
    return name_and_executables

def load_modules_recursiv(path, module):  
    for root, directories, files in os.walk(os.path.abspath(path)):
        for file in files:
            try:
                importlib.import_module(module + "." + file.split(".")[0])
            except:
                continue
                    
        for directory in directories:  
            if directory != "__pycache__":
                load_modules_recursiv(path + directory, module + "." + directory)        