from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class MoroccoFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
            
    def execute(self):
        red = Color(193, 39, 45)
        green = Color(0, 98, 51)
        self.matrix_access.turn_rows_on(range(self.matrix_access.rows), red)
        
        self.matrix_access.turn_on_matrix_position([(3, 5)], green)
        self.matrix_access.turn_on_row_ranged(4, range(3, 8), green)
        self.matrix_access.turn_on_row_ranged(5, range(4, 7), green)
        self.matrix_access.turn_on_row_ranged(6, [3, 7], green)
        
        
        self.matrix_access.refresh()