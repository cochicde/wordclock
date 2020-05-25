'''
Created on 26.04.2020

@author: cabral
'''

from rpi_ws281x import PixelStrip
from wiring.WiringBase import WiringBase

class WiringHorizontal1(WiringBase):
    
    def __init__(self, parameters):
        super().__init__(parameters)
        
    def coordinates_to_strip_pos(self, row, column):
        #The strip starts from the bottom
        after_first_point =  int(row < 1) #only row 0 is after the first led 
        after_second_point = int(False) # the second led is the last led in the strip
        after_third_point = int(row < 9) #only row 9 is behind the third led
        after_fourth_point = int(True) #the fourth point is the first led, so every word is after it 
        
        first_led = (9 - row) * 11  + after_first_point + after_second_point + after_third_point + after_fourth_point #The rows are inverted for the strip
        
        if(row % 2 == 0): #even rows start (column 0) is the same as the column passed as argument
            first_led += column
        else:  #odd rows start (column 0) is the the last led in the row from the strip point of view
            first_led += 11 - column - 1 
        
        return first_led
    
    def point_to_strip_pos(self, point):
        points = [(2 + 11 * 9), (3 + 11 * 10), 0, (1 + 11 * 1)]
        return points[point]
