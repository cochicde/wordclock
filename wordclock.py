'''
Created on Apr 24, 2020

@author: cabral
'''

import time
import signal
import sys

from layout.LayoutBase import get_layout_instance
from wiring.WiringBase import get_wiring_instance
from utils.MatrixOperations import MatrixOperations
from config.ConfigParser import ConfigParser
from utils import ModuleLoader
from scheduler.Scheduler import Scheduler
#from web.backend.Backend import Backend

import datetime

exit_params = []

# default values
DEFAULT_LAYOUT = "LayoutSpanish"
DEFAULT_WIRING = "WiringHorizontal1"

def clean_all(signalNumber, frame):
    print('Bye. Signal Received:', signalNumber)
    exit_params[0].turn_all_off()
    exit_params[0].refresh()
    sys.exit()

if __name__ == '__main__':
    
    #Load modules
    ModuleLoader.load_modules("animations")
    ModuleLoader.load_modules("layout")
    ModuleLoader.load_modules("wiring")
    
    # Get the configurations
    parser = ConfigParser("config/default.conf")
    parameters_global = parser.parse()
    
    # Get the language layout
    wordclock_params = parameters_global.get("wordclock", {})
    board = get_layout_instance(wordclock_params.get("language", DEFAULT_LAYOUT))()
    
    # Get the type of led strip    
    strip_name = wordclock_params.get("strip", DEFAULT_WIRING)
    led_strip = get_wiring_instance(strip_name)(parameters_global.get(strip_name, {}))
    
    
    # Load the matrix
    matrix = MatrixOperations(led_strip, parameters_global.get("matrix", {}))
    
    signal.signal(signal.SIGTERM, clean_all)
    signal.signal(signal.SIGINT, clean_all)
    exit_params.append(led_strip)
    
    scheduler = Scheduler(matrix, parameters_global)
    
    #backend = Backend(matrix)
        
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
        
        sleeptime = freq if freq != -1 else 60 - datetime.datetime.utcnow().second 
        time.sleep(sleeptime)
        
