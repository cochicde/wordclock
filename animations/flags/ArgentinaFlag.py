from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class ArgentinaFlag(AnimationBase):
    
    def __init__(self, led_access, parameters):
        self.led_access = led_access
            
    def execute(self):
        divider = 1.5
        light_blue = Color(int(108/divider), int(172/divider), int(228/divider))
        white = Color(int(255/divider), int(255/divider), int(255/divider))
        sun_color = Color(int(255/divider), int(184/divider), int(28/divider))
        self.led_access.turn_rows_on(range(3), light_blue)
        self.led_access.turn_rows_on(range(3, 7), white)
        self.led_access.turn_rows_on(range(7, 10), light_blue)
        self.led_access.turn_on_matrix_position([(4,4), (4,5), (4,6), (5,4), (5,5), (5,6)], sun_color)
        self.led_access.refresh()
        
