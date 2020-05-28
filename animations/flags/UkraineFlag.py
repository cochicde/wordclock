from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class UkraineFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
            
    def execute(self):
        self.matrix_access.turn_rows_on(range(5), Color(0, 87, 184)) 
        self.matrix_access.turn_rows_on(range(5, 10), Color(255, 215, 0))
        self.matrix_access.refresh()