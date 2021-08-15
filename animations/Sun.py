from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color
import importlib

class Sun(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
   
        
        filter_name = parameters.get("filter", "")
        if filter_name != "":
            self.filter = importlib.import_module("animations.filters." + filter_name) 
        else:
            self.filter = self
            numbers = parameters.get("color", "255 255 0")
            numbers = numbers.strip().split(" ")
            self.color = Color(int(numbers[0]), int(numbers[1]), int(numbers[2])) 
        
        
        self.matrix_access = matrix_access
        self.leds = []
        for row in [0, 5, 10]:
            self.leds.append((0, row))
            self.leds.append((8, row))
            
        for row in [1, 9]:
            self.leds.append((1, row))
            self.leds.append((7, row))
            
        for row in range(4, 7):
            self.leds.append((2, row))
            self.leds.append((6, row))
            
        for row in range(3, 8):
            self.leds.append((3, row))
            self.leds.append((5, row))
            
        for row in [0, 1, 3, 4, 5, 6, 7, 9, 10]:
            self.leds.append((4, row))

    def get_color_from_row(self, row):
        return self.color

    def execute(self):
        
        for led in self.leds:
            self.matrix_access.turn_on_matrix_position([led], self.filter.get_color_from_row(led[0]))
                
        self.matrix_access.refresh()
