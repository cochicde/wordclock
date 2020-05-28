from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color

class HeartBig(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        numbers = parameters.get("color", "255 0 0")
        numbers = numbers.strip().split(" ")
        self.color = Color(int(numbers[0]), int(numbers[1]), int(numbers[2])) 
        self.matrix_access = matrix_access

    def execute(self):
        self.matrix_access.turn_on_row_ranged(0, [2, 3, 7 ,8], self.color)
        self.matrix_access.turn_on_row_ranged(1, [1, 2, 3, 4, 6, 7 , 8, 9], self.color)
        self.matrix_access.turn_on_row_ranged(2, range(11), self.color)
        self.matrix_access.turn_on_row_ranged(3, range(11), self.color)
        self.matrix_access.turn_on_row_ranged(4, range(11), self.color)
        self.matrix_access.turn_on_row_ranged(5, range(1,10), self.color)
        self.matrix_access.turn_on_row_ranged(6, range(2,9), self.color)
        self.matrix_access.turn_on_row_ranged(7, range(3,8), self.color)
        self.matrix_access.turn_on_row_ranged(8, range(4,7), self.color)
        self.matrix_access.turn_on_row_ranged(9, range(5,6), self.color)
        self.matrix_access.refresh()