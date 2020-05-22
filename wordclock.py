'''
Created on Apr 24, 2020

@author: cabral
'''

import atexit
import time

from wordclock import SpanishBoard
from wordclock.LedStripHorizontal1 import LedStripHorizontal1
from wordclock.MatrixOperations import MatrixOperations
from config.ConfigParser import ConfigParser
from animations.AnimationsLoader import load_modules
from Scheduler import Scheduler

import datetime

TEST = False
STEP_TEST = True

def clean_all(led_strip):
    led_strip.turn_all_off()
    led_strip.refresh()

if __name__ == '__main__':
    
    #Call config parser
    #Look for key called wordclock which should have an array of tupples whose first parameter
    #would be the name of the variable and the other value would be the parameter
    
    parser = ConfigParser("config/default.conf")
    
    parameters_global = parser.parse()
    
    #TODO: set the board and the led_strip according ot the parameters
    board = SpanishBoard()
    led_strip = LedStripHorizontal1({})
    matrix = MatrixOperations(led_strip, {})
    
    #Load modules
    name_and_executables = load_modules("./animations/", "animations", matrix, parameters_global)
 
    atexit.register(clean_all, led_strip)
    debug_time = datetime.datetime.now()
    scheduler = Scheduler(name_and_executables, parameters_global["scheduler"])
        
    while(True):
        
       
        
        #to_execute = "ParaguayFlag"
        
        #led_strip.turn_all_off()
        #name_and_executables[to_execute].execute()
        #if to_execute != "HeartBeat":
        #    time.sleep(2)
        
        led_strip.turn_all_off()
        freq = scheduler.execute()

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
            sleeptime = freq
            time.sleep(sleeptime)
        
