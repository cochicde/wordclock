
import os
import importlib

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