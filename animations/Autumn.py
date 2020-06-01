from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color
import time

class Autumn(AnimationBase):
    
     def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
        self.leds_on = {}
        self.odd = False
        self.cycle = 0
        self.count = 0
        self.start = False

     def execute(self):
         higest_red = 128
         color = None
         if self.count % 3 == 0:
             color = Color(higest_red, 0, 0)
         elif self.count % 3 == 1:
             color = Color(215, 107, 0)
         else:     
             color = Color(higest_red, higest_red, 0)
             
         if not self.start:
             for i in range(0, higest_red, 2):
                color = Color(i, higest_red - i, 0)
                self.matrix_access.turn_rows_on([0], color)
                self.matrix_access.turn_on_row_ranged(1, range(1, 10), color)
                self.matrix_access.turn_on_row_ranged(2, range(2, 10, 2), color)
                self.matrix_access.refresh()
                time.sleep(50/1000)
             
             new_leds = [(0, column) for column in range(self.matrix_access.columns)]
             for led in new_leds:
                 self.leds_on[led] = color
                 
             new_leds = [(1, column) for column in range(1, 10)]
             for led in new_leds:
                 self.leds_on[led] = color
                 
             new_leds = [(2, column) for column in range(2, 10, 2)]
             for led in new_leds:
                 self.leds_on[led] = color
                 
             self.start = True
        
         for key in self.leds_on.keys():
             self.matrix_access.turn_on_matrix_position([key], self.leds_on[key])
             
         columns = range(self.cycle, 11 - self.cycle, 2) if self.odd else range(self.cycle + 1, 11 - self.cycle, 2)
         for row in range(3, 10 - self.cycle):
            self.matrix_access.turn_on_row_ranged(row, columns, color)
            self.matrix_access.refresh()
            time.sleep(300/1000)
            if row != 10 - self.cycle - 1:
                self.matrix_access.turn_on_row_ranged(row, columns, 0)
                self.matrix_access.refresh()
                time.sleep(300/1000)
            else:
                for column in columns:
                    self.leds_on[(10 - self.cycle -1, column)] = color
                
        
         if self.odd:
            self.cycle += 1    
         self.odd = not self.odd
         
         self.count += 1
         
         if self.cycle == 4:
             self.cycle = 0
             self.leds_on = {}
             odd = False
             self.start = False
             self.count = 0
