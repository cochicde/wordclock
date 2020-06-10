

class Matrix():
    
    def __init__(self, led_strip, parameters):
        self.rows = int(parameters.get("rows", 10))
        self.columns = int(parameters.get("columns", 11))
        self.points = int(parameters.get("points", 4))
        self.led_strip = led_strip