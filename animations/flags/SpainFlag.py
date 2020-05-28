from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class SpainFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
            
    def execute(self):
        self.matrix_access.turn_rows_on(range(3), Color(170, 21, 27)) #170, 21, 27
        self.matrix_access.turn_rows_on(range(3, 7), Color(241, 191, 0))
        self.matrix_access.turn_rows_on(range(7, 10), Color(170, 21, 27))
        self.matrix_access.turn_on_matrix_position([(4,1), (4,2), (5,1), (5,2)], Color(221, 0, 0))
        self.matrix_access.refresh()
        
