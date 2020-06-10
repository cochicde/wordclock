from animations.AnimationBase import AnimationBase
from rpi_ws281x import Color


class BayernFlag(AnimationBase):
    
    def __init__(self, matrix_access, parameters):
        self.matrix_access = matrix_access
        self.light_blue_leds = []
        self.light_blue_leds.extend([(0, i) for i in range(3)])
        self.light_blue_leds.extend([(0, i) for i in range(6, 9)])
        
        self.light_blue_leds.extend([(1, i) for i in range(1, 4)])
        self.light_blue_leds.extend([(1, i) for i in range(7, 10)])
        
        self.light_blue_leds.extend([(2, i) for i in range(2, 5)])
        self.light_blue_leds.extend([(2, i) for i in range(8, 11)])
        
        self.light_blue_leds.extend([(3, i) for i in range(0, 2)])
        self.light_blue_leds.extend([(3, i) for i in range(5, 8)])
        
        self.light_blue_leds.extend([(4, i) for i in range(3)])
        self.light_blue_leds.extend([(4, i) for i in range(6, 9)])
        
        self.light_blue_leds.extend([(5, i) for i in range(1, 4)])
        self.light_blue_leds.extend([(5, i) for i in range(7, 10)])
        
        self.light_blue_leds.extend([(6, i) for i in range(1)])
        self.light_blue_leds.extend([(6, i) for i in range(4, 7)])
        self.light_blue_leds.extend([(6, i) for i in range(10, 11)])
        
        self.light_blue_leds.extend([(7, i) for i in range(0, 2)])
        self.light_blue_leds.extend([(7, i) for i in range(5, 8)])

        self.light_blue_leds.extend([(8, i) for i in range(3)])
        self.light_blue_leds.extend([(8, i) for i in range(6, 9)])
        
        self.light_blue_leds.extend([(9, i) for i in range(3, 6)])
        self.light_blue_leds.extend([(9, i) for i in range(9, 11)])
        
    def execute(self):
        divider = 1.9
        light_blue = Color(int(0/divider), int(153/divider), int(213/divider))
        white = Color(int(255/divider), int(255/divider), int(255/divider))
        self.matrix_access.turn_all_on(white)
        self.matrix_access.turn_on_matrix_position(self.light_blue_leds, light_blue)
        self.matrix_access.refresh()
        

