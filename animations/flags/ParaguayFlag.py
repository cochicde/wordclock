from rpi_ws281x import Color
from animations.AnimationBase import AnimationBase

class ParaguayFlag(AnimationBase):
    
    def __init__(self, led_access, parameters):
        self.led_access = led_access
            
    def execute(self):
        max_value = 64
        #TODO: make the flag dependant of the rows/columns. Achtung the yellow in the middle
        self.led_access.turn_rows_on(range(3), Color(max_value, 0, 0))
        self.led_access.turn_rows_on(range(3, 7), Color(max_value, max_value, max_value))
        self.led_access.turn_rows_on(range(7, 10), Color(0, 0, max_value))
        self.led_access.turn_on_matrix_position([(4,4), (4,5), (4,6), (5,4), (5,5), (5,6)], Color(max_value, max_value, 0))
        self.led_access.refresh()