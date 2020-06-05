from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color
from utils.RainbowColors import get_color_from_row


class PrideFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
            
    def execute(self):
        for row in range(self.matrix_access.rows): 
            self.matrix_access.turn_rows_on([row], get_color_from_row(row))
            self.matrix_access.refresh()