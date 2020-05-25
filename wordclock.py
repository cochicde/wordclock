'''
Created on Apr 24, 2020

@author: cabral
'''

import atexit
import time

from layout.LayoutBase import get_layout_instance
from wiring.WiringBase import get_wiring_instance
from wiring.WiringHorizontal1 import WiringHorizontal1
from utils.MatrixOperations import MatrixOperations
from config.ConfigParser import ConfigParser
import animations.AnimationsLoader as AnimationsLoader
from Scheduler import Scheduler

import datetime

def clean_all(led_strip):
    led_strip.turn_all_off()
    led_strip.refresh()

if __name__ == '__main__':
    
    #Call config parser
    #Look for key called wordclock which should have an array of tupples whose first parameter
    #would be the name of the variable and the other value would be the parameter
    
    parser = ConfigParser("config/default.conf")
    
    parameters_global = parser.parse()
    
    board = get_layout_instance(parameters_global["wordclock"]["language"])()
    led_strip = get_wiring_instance(parameters_global["wordclock"]["strip"])(parameters_global.get(parameters_global["wordclock"]["strip"], {}))
    
    
    matrix = MatrixOperations(led_strip, {})
    
    #Load modules
    name_and_executables = AnimationsLoader.load_animations("./animations/", "animations", matrix, parameters_global)
 
    atexit.register(clean_all, led_strip)
    scheduler = Scheduler(name_and_executables, parameters_global["scheduler"])
        
    while(True):
        
        led_strip.turn_all_off()
        freq = scheduler.execute()

        wordsAndPoints = board.get_words_and_points_from_time(datetime.datetime.now().time())
      
        led_strip.turn_all_off()
        for word in wordsAndPoints[0]:
            for i in range(len(word.word)):
                matrix.turn_on_matrix_position([(word.row, word.column + i)])
        
        
        for points in range(wordsAndPoints[1]):
            matrix.turn_on_point([points])
               
        matrix.refresh()
        
        #sleeptime = 60 - datetime.datetime.utcnow().second
        sleeptime = freq
        time.sleep(sleeptime)
        
