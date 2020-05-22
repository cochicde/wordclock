from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class UkraineFlag(AnimationBase):
    
    def __init__(self, led_access, parameters):
        self.led_access = led_access
            
    def execute(self):
        self.led_access.turn_rows_on(range(5), Color(0, 87, 184)) 
        self.led_access.turn_rows_on(range(5, 10), Color(255, 215, 0))
        self.led_access.refresh()