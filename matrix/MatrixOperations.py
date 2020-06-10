from rpi_ws281x import Color
import sys

CONST_OUT_OF_SCOPE = " out of scope: " # to avoid sonar from complaining

class MatrixOperations: 
    
    def __init__(self, led_strip, parameters):
        self.rows = int(parameters.get("rows", 10))
        self.columns = int(parameters.get("columns", 11))
        self.points = int(parameters.get("points", 4))
        self.led_strip = led_strip

    #Coordinates is a tupple (row, column)
    def turn_on_matrix_position(self, coordinates, color = Color(255, 255, 255)):
        for coordinate in coordinates:
            if coordinate[0] >= self.rows or coordinate[1] >= self.columns:
                sys.exit("[turn_on_matrix_position] Coordinates: (" + str(coordinate[0]) + ", " + str(coordinate[1]) + ") out of scope: (" + str(self.rows) + ", " + str(self.columns) + ")")
            self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(coordinate[0], coordinate[1]), color)
        
    def turn_on_point(self, points, color = Color(255, 255, 255)):
        for point in points:
            if point >= self.points:
                sys.exit("[turn_on_point] Point: " + str(point) + CONST_OUT_OF_SCOPE + str(self.points))
            self.led_strip.set_pixel_color(self.led_strip.point_to_strip_pos(point), color)
    
    def turn_on_row_ranged(self, row, columns, color = Color(255, 255, 255)):
        if row >= self.rows:
            sys.exit("[turn_on_row_ranged] Row: " + str(row) + CONST_OUT_OF_SCOPE + str(self.rows))
        for column in columns:
            if column >= self.columns:
                sys.exit("[turn_on_row_ranged] Column: " + str(column) + CONST_OUT_OF_SCOPE + str(self.columns))
            self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column), color)
            
    def turn_on_column_ranged(self, column, rows, color = Color(255, 255, 255)):
        if column >= self.columns:
            sys.exit("[turn_on_column_ranged] Column: " + str(column) + CONST_OUT_OF_SCOPE + str(self.columns))
        for row in rows:
            if row >= self.rows:
                sys.exit("[turn_on_column_ranged] Row: " + str(row) + CONST_OUT_OF_SCOPE + str(self.rows))
            self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column), color)
            
    def turn_rows_on(self, rows, color = Color(255, 255, 255)):
        for row in rows:
            if row >= self.rows:
                sys.exit("[turn_rows_on] Row: " + str(row) + CONST_OUT_OF_SCOPE + str(self.rows))
            for column in range(self.columns):
                self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column), color)
                
    def turn_columns_on(self, columns, color = Color(255, 255, 255)):
        for column in columns:
            if column >= self.columns:
                sys.exit("[turn_columns_on] Column: " + str(column) + CONST_OUT_OF_SCOPE + str(self.columns))
            for row in range(self.rows):
                self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column), color)
                
    def move_down(self, count):
        for row in range(self.rows - 1 - count, -1, -1):
            colors = [self.led_strip.get_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column)) for column in range(self.columns)]
            for column in range(self.columns):
                self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row + count, column), colors[column])
        
        self.turn_rows_on(range(count), 0)
        
    def move_up(self, count):
        for row in range(count, self.rows):
            colors = [self.led_strip.get_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column)) for column in range(self.columns)]
            for column in range(self.columns):
                self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row - count, column), colors[column])
        
        self.turn_rows_on(range(self.rows - count, self.rows), 0)
        
    def move_right(self, count):
        for column in range(self.columns - 1 - count, -1, -1):
            colors = [self.led_strip.get_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column)) for row in range(self.rows)]
            for row in range(self.rows):
                self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column  + count), colors[row])
        
        self.turn_columns_on(range(count), 0)
        
    def move_left(self, count):
        for column in range(count, self.columns):
            colors = [self.led_strip.get_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column)) for row in range(self.rows)]
            for row in range(self.rows):
                self.led_strip.set_pixel_color(self.led_strip.coordinates_to_strip_pos(row, column - count), colors[row])
        
        self.turn_columns_on(range(self.columns - count, self.columns), 0)
    
    def turn_all_on(self, color):
        self.turn_rows_on(range(self.rows), color)
    
    def turn_all_off(self):
        self.led_strip.turn_all_off()  
                
    def refresh(self):
        self.led_strip.refresh()