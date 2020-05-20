'''
Created on Apr 24, 2020

@author: cabral
'''

import atexit
import time
from wordclock import SpanishBoard
from wordclock.LedStripHorizontal1 import LedStripHorizontal1
from wordclock.BoardWord import BoardWord
from wordclock.MatrixOperations import MatrixOperations

#For flag
from rpi_ws281x import Color


import datetime

TEST = False
STEP_TEST = True

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
    
def set_heart_big(led_access):
    color = Color(255, 0, 0)
    
    led_access.turn_on_row_ranged(0, [2, 3, 7 ,8], color)
    led_access.turn_on_row_ranged(1, [1, 2, 3, 4, 6, 7 , 8, 9], color)
    led_access.turn_on_row_ranged(2, range(11), color)
    led_access.turn_on_row_ranged(3, range(11), color)
    led_access.turn_on_row_ranged(4, range(11), color)
    led_access.turn_on_row_ranged(5, range(1,10), color)
    led_access.turn_on_row_ranged(6, range(2,9), color)
    led_access.turn_on_row_ranged(7, range(3,8), color)
    led_access.turn_on_row_ranged(8, range(4,7), color)
    led_access.turn_on_row_ranged(9, range(5,6), color)
    led_access.refresh()
    
def set_heart_small(led_access):
    color = Color(255, 0, 0) # mediumvioletred     #C71585
  
    led_access.turn_on_row_ranged(2, [2, 3, 4, 6, 7 ,8], color)
    led_access.turn_on_row_ranged(3, range(1, 10), color)
    led_access.turn_on_row_ranged(4, range(1, 10), color)
    led_access.turn_on_row_ranged(5, range(2,9), color)
    led_access.turn_on_row_ranged(6, range(3,8), color)
    led_access.turn_on_row_ranged(7, range(4,7), color)
    led_access.turn_on_row_ranged(8, range(5,6), color)
    led_access.refresh()

if __name__ == '__main__':
    board = SpanishBoard()
    led_strip = LedStripHorizontal1({})
    matrix = MatrixOperations(led_strip, {})
    
    atexit.register(clean_all, led_strip)
    
    debug_time = datetime.datetime.now()
        
    while(True):
        
        set_paraguay_flag(matrix)
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
        
