from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color
import time

class Winter(AnimationBase):
    
     def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
        self.leds_on = []
        self.odd = False
        self.cycle = 0
        self.start = False

     def execute(self):
         higest_color = 128
         color = Color(higest_color, higest_color, higest_color)
             
         if not self.start:
             for i in range(0, higest_color, 2):
                color = Color(higest_color, i, i)
                self.matrix_access.turn_rows_on([0], color)
                self.matrix_access.turn_on_row_ranged(1, range(1, 10), color)
                self.matrix_access.turn_on_row_ranged(2, range(2, 10, 2), color)
                self.matrix_access.refresh()
                time.sleep(50/1000)
             
             new_leds = [(0, column) for column in range(self.matrix_access.columns)]
             for led in new_leds:
                 self.leds_on.append(led)
                 
             new_leds = [(1, column) for column in range(1, 10)]
             for led in new_leds:
                 self.leds_on.append(led)
                 
             new_leds = [(2, column) for column in range(2, 10, 2)]
             for led in new_leds:
                 self.leds_on.append(led)
                 
             self.start = True
        
         self.matrix_access.turn_on_matrix_position(self.leds_on, color)
             
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
                    self.leds_on.append((10 - self.cycle -1, column))
                
        
         if self.odd:
            self.cycle += 1    
         self.odd = not self.odd
         
         if self.cycle == 4:
             self.cycle = 0
             self.leds_on = []
             odd = False
             self.start = False
