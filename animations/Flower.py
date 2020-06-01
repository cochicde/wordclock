from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color

class Flower(AnimationBase):
    
     def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access

     def execute(self):
        light_pink = Color(234, 120, 156)
        dark_pink = Color(221, 15, 90)
        yellow = Color(255, 255, 0)
        green = Color(147, 197, 48)
        
        self.matrix_access.turn_on_matrix_position([(0, 5), (4, 5)], light_pink)
        self.matrix_access.turn_on_row_ranged(1, [4, 5, 6], light_pink)
        self.matrix_access.turn_on_matrix_position([(2, 3), (2, 4), (2, 6), (2, 7)], light_pink)
        self.matrix_access.turn_on_row_ranged(3, [4, 5, 6], light_pink)
        
        self.matrix_access.turn_on_matrix_position([(2, 5)], yellow)
        
        self.matrix_access.turn_on_matrix_position([(0, 4), (0, 6)], dark_pink)
        self.matrix_access.turn_on_matrix_position([(1, 3), (1, 7)], dark_pink)
        self.matrix_access.turn_on_matrix_position([(3, 3), (3, 7)], dark_pink)
        self.matrix_access.turn_on_matrix_position([(4, 4), (4, 6)], dark_pink)
        
        self.matrix_access.turn_on_column_ranged(5, range(5, 10), green)
        self.matrix_access.turn_on_matrix_position([(7, 6), (8, 4)], green)
        
        self.matrix_access.refresh()