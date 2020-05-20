'''
Created on 26.04.2020

@author: cabral
'''

from rpi_ws281x import PixelStrip

class LedStripHorizontal1:
    
    def __init__(self, parameters):
        self.led_count = int(parameters.get("led_count", 114))
        self.led_pin = int(parameters.get("led_pin", 18))                        # GPIO pin connected to the pixels (18 uses PWM!).
        self.led_freq_hz = int(parameters.get("led_freq_hz", 800000))            # LED signal frequency in hertz (usually 800khz)
        self.led_dma = int(parameters.get("led_dma", 10))                        # DMA channel to use for generating signal (try 10)
        self.led_brightness = int(parameters.get("led_brightness", 255))         # Set to 0 for darkest and 255 for brightest
        self.led_invert = parameters.get("led_brightness", "False") == "True"   # True to invert the signal (when using NPN transistor level shift) 
        self.led_channel = int(parameters.get("led_channel", 0))                 # set to '1' for GPIOs 13, 19, 41, 45 or 53
        
        self.strip = PixelStrip(self.led_count, self.led_pin, self.led_freq_hz, self.led_dma, self.led_invert, self.led_brightness, self.led_channel)
        self.strip.begin()
        
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
    
    def point_to_strip_pos(self, point):
        points = [(2 + 11 * 9), (3 + 11 * 10), 0, (1 + 11 * 1)]
        return points[point]
    
    def set_pixel_color(self, pos, color):
        self.strip.setPixelColor(pos, color)
        
    def turn_all_off(self):
        for led in range(self.led_count):
            self.strip.setPixelColor(led, 0)   
        
    def refresh(self):
        self.strip.show()
