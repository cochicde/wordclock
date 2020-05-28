import os
import importlib

def load_modules(module, path=None):
    if path == None:
        path = "./" + module
    
    for root, directories, files in os.walk(os.path.abspath(path)):
        for file in files:
            try:
                importlib.import_module(module + "." + file.split(".")[0])
            except:
                continue
                    
        for directory in directories:  
            if directory != "__pycache__":
                load_modules(module + "." + directory, path + "/" + directory)