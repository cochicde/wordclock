'''
Created on Apr 24, 2020

@author: cabral
'''

import atexit
import time
import os
import importlib
from wordclock import SpanishBoard
from wordclock.LedStripHorizontal1 import LedStripHorizontal1
from wordclock.BoardWord import BoardWord
from wordclock.MatrixOperations import MatrixOperations
from config.ConfigParser import ConfigParser

#For flag
from rpi_ws281x import Color


import datetime

TEST = False
STEP_TEST = True

def load_modules(path, module):
    names = []
    imported_modules = []
    for root, directories, files in os.walk(os.path.abspath(path)):
        for file in files:
            try:
                imported_modules.append(importlib.import_module(module + "." + file.split(".")[0]))
                names.append(file.split(".")[0])
            except:
                continue
                    
        for directory in directories:  
            if directory != "__pycache__":
                new_names, new_modules = load_modules(path + directory, module + "." + directory)
                if 0 != len(new_modules): 
                    imported_modules += new_modules
                    names += new_names
            
    return names, imported_modules

def clean_all(led_strip):
    led_strip.turn_all_off()
    led_strip.refresh()
    

def print_clock(words_and_points):
    string_to_print = ""
    for word in words_and_points[0]:
        string_to_print += str(word) + " "
        
    if(words_and_points[1] != 0):
        string_to_print += " + " + str(words_and_points[1])    
    
    print(string_to_print) 
    
def set_paraguay_flag(matrix):
    max_value = 64
    matrix.turn_rows_on(range(3), Color(max_value, 0, 0))
    matrix.turn_rows_on(range(3, 7), Color(max_value, max_value, max_value))
    matrix.turn_rows_on(range(7, 10), Color(0, 0, max_value))
    matrix.turn_on_matrix_position([(4,4), (4,5), (4,6), (5,4), (5,5), (5,6)], Color(max_value, max_value, 0))
    matrix.refresh()
    
if __name__ == '__main__':
    
    #Call config parser
    #Look for key called wordclock which should have an array of tupples whose first parameter
    #would be again arrays for the name of the variable and the other value would be the parameter
    
    parser = ConfigParser(os.path.abspath("config/default.conf"))
    
    dic = parser.parse()
    names, modules = load_modules("./animations/", "animations")
    
    board = SpanishBoard()
    led_strip = LedStripHorizontal1({})
    matrix = MatrixOperations(led_strip, {})
    
    executables = []
    for i in range(len(modules)):
        parameters = dic.get(names[i], {})
        par_pretty = {}
        for parameter in parameters:
            par_pretty[str(parameter[0])] = parameter[1]
        
        class_py = getattr(modules[i], names[i])
        executables.append(class_py(matrix, par_pretty))
    
    
    atexit.register(clean_all, led_strip)
    
    debug_time = datetime.datetime.now()
        
    while(True):
        
        to_execute = 3
        
        led_strip.turn_all_off()
        executables[to_execute].execute()
        if to_execute > 0:
            time.sleep(2)
        

        if TEST:
            wordsAndPoints = board.get_words_and_points_from_time(debug_time)
        else:
            wordsAndPoints = board.get_words_and_points_from_time(datetime.datetime.now().time())
      
        led_strip.turn_all_off()
        for word in wordsAndPoints[0]:
            for i in range(len(word.word)):
                matrix.turn_on_matrix_position([(word.row, word.column + i)])
        
        
        for points in range(wordsAndPoints[1]):
            matrix.turn_on_point([points])
               
        matrix.refresh()
        
        if TEST:
            if(STEP_TEST):
                input("Press enter to add a minute")
            else:
                time.sleep(200 / 1000.0)
            
            debug_time = debug_time + datetime.timedelta(minutes=1)
            print_clock(wordsAndPoints)
        else:    
            #sleeptime = 60 - datetime.datetime.utcnow().second
            sleeptime = 10
            time.sleep(sleeptime)
        
