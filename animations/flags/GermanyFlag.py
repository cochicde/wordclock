from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class GermanyFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
            
    def execute(self):
        #max_value = 64
        #TODO: make the flag dependant of the rows/columns. Achtung the yellow in the middle
        self.matrix_access.turn_rows_on(range(3), Color(0, 0, 0))
        self.matrix_access.turn_rows_on(range(4, 7), Color(221, 0, 0))
        self.matrix_access.turn_rows_on(range(7, 10), Color(255, 206, 0))
        self.matrix_access.refresh()