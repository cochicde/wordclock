'''
Created on Apr 24, 2020

@author: cabral
'''

import time
from wordclock import SpanishBoard
from wordclock.LEDAccess import LEDAccess
from wordclock.BoardWord import BoardWord

import datetime

TEST = False
STEP_TEST = True



def print_clock(words_and_points):
    string_to_print = ""
    for word in words_and_points[0]:
        string_to_print += str(word) + " "
        
    if(words_and_points[1] != 0):
        string_to_print += " + " + str(words_and_points[1])    
    
    print(string_to_print) 

if __name__ == '__main__':
    board = SpanishBoard()
    ledAccess = LEDAccess()
    
    debug_time = datetime.datetime.now()
    try:
        
        while(True):
            
            if TEST:
                wordsAndPoints = board.get_words_and_points_from_time(debug_time)
            else:
                wordsAndPoints = board.get_words_and_points_from_time(datetime.datetime.now().time())
          
            ledAccess.turn_all_off()
            for word in wordsAndPoints[0]:
                for i in range(len(word.word)):
                    ledAccess.turn_on_matrix_position([(word.row, word.column + i)])
            
            
            for points in range(wordsAndPoints[1]):
                ledAccess.turn_on_point([points])
                   
            ledAccess.refresh()
            
            if TEST:
                if(STEP_TEST):
                    input("Press enter to add a minute")
                else:
                    time.sleep(200 / 1000.0)
                
                debug_time = debug_time + datetime.timedelta(minutes=1)
                print_clock(wordsAndPoints)
            else:    
                sleeptime = 60 - datetime.datetime.utcnow().second
                time.sleep(sleeptime)
                
    except KeyboardInterrupt:
        ledAccess.turn_all_off()
        ledAccess.refresh()
