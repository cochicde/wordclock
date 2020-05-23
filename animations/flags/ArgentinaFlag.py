from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class ArgentinaFlag(AnimationBase):
    
    def __init__(self, led_access, parameters):
        self.led_access = led_access
            
    def execute(self):
        self.led_access.turn_rows_on(range(3), Color(108,172,228))
        self.led_access.turn_rows_on(range(3, 7), Color(255, 255, 255))
        self.led_access.turn_rows_on(range(7, 10), Color(108, 172, 228))
        self.led_access.turn_on_matrix_position([(4,4), (4,5), (4,6), (5,4), (5,5), (5,6)], Color(255,184,28))
        self.led_access.refresh()
        
