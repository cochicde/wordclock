'''
Created on 26.04.2020

@author: cabral
'''

from rpi_ws281x import PixelStrip, Color

class LEDAccess:
    
    def __init__(self):
        self.ROWS = 10
        self.COLUMNS = 11
        self.POINTS = 4
        self.LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = 10          # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        
        self.strip = PixelStrip(self.ROWS * self.COLUMNS + self.POINTS, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        self.strip.begin()
        
        self.points = [(2 + 11 * 9), (3 + 11 * 10), 0, (1 + 11 * 1)]
            
          
    #0,0 is the top left LED, and rows increase downwards, and columns to the right    
    def coordinates_to_strip_pos(self, row, column):
        #The strip starts from the bottom
        after_first_point =  int(row < 1) #only row 0 is after the first led 
        after_second_point = int(False) # the second led is the last led in the strip
        after_third_point = int(row < 9) #only row 9 is behind the third led
        after_fourth_point = int(True) #the fourth point is the first led, so every word is after it 
        
        first_led = (9 - row) * 11  + after_first_point + after_second_point + after_third_point + after_fourth_point #The rows are inverted for the strip
        
        if(row % 2 == 0): #even rows start (column 0) is the same as the column passed as argument
            first_led += column
        else:  #odd rows start (column 0) is the the last led in the row from the strip point of view
            first_led += 11 - column - 1 
        
        return first_led
        
    #Coordinates is a tupple (row, column)
    def turn_on_matrix_position(self, coordinates, color = Color(255, 255, 255)):
        for coordinate in coordinates:
            self.strip.setPixelColor(self.coordinates_to_strip_pos(coordinate[0], coordinate[1]), color)
        
    def turn_on_point(self, points, color = Color(255, 255, 255)):
        for point in points:
            self.strip.setPixelColor(self.points[point], color)
    
    def turn_on_positions(self, positions, color = Color(255, 255, 255)):
        for position in positions:
            self.strip.setPixelColor(position, color)

    #TODO: define function that can turn row + range of column and otherwise
            
    def turn_all_off(self):
        for led in range(self.strip.numPixels()):
            self.strip.setPixelColor(led, Color(0, 0, 0))   
            
    def turn_rows_on(self, rows, color = Color(255, 255, 255)):
        for row in rows:
            for column in range(self.COLUMNS):
                self.strip.setPixelColor(self.coordinates_to_strip_pos(row, column), color)
                
    def turn_columns_on(self, columns, color = Color(255, 255, 255)):
        for column in columns:
            for row in range(self.ROWS):
                self.strip.setPixelColor(self.coordinates_to_strip_pos(row, column), color)  
        
    def refresh(self):
        self.strip.show()
        
        
'''
    def addWord(self, word):
        ledsInStrip = []
        startingLED = self.coordinates_to_strip_pos(word.row, word.column)

        for i in range(len(word.word)):
            if(word.row % 2 == 0): #even rows start (column 0) is the same as the column passed as argument, so the word goes forward
                ledsInStrip.append(startingLED + i)
            else:  #odd rows start (column 0) is the same as the column passed as argument, so the word goes backward
                ledsInStrip.append(startingLED - i)
                
        self.words_to_led.update({word: ledsInStrip})

        
    def turnWordsOn(self, words): 
        for led in range(self.strip.numPixels()):
            self.strip.setPixelColor(led, Color(0, 0, 0))

        for word in words[0]:
            for led in self.words_to_led[word]:
                self.strip.setPixelColor(led, Color(255, 255, 255))
        
        for led in range(words[1]):
            self.strip.setPixelColor(self.points[led], Color(255, 255, 255))
            
        self.strip.show()
        
'''        
        
        
        
        
    
    
