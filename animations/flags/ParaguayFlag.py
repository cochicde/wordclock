from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class ParaguayFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
        self.max_value = int(parameters.get("max_value", "255"))
            
    def execute(self):
        #TODO: make the flag dependant of the rows/columns. Achtung the yellow in the middle
        self.matrix_access.turn_rows_on(range(3), Color(self.max_value, 0, 0))
        self.matrix_access.turn_rows_on(range(3, 7), Color(self.max_value, self.max_value, self.max_value))
        self.matrix_access.turn_rows_on(range(7, 10), Color(0, 0, self.max_value))
        self.matrix_access.turn_on_matrix_position([(4,4), (4,5), (4,6), (5,4), (5,5), (5,6)], Color(self.max_value, self.max_value, 0))
        self.matrix_access.refresh()