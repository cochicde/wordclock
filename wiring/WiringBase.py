'''
Created on 26.04.2020

@author: cabral
'''

from rpi_ws281x import PixelStrip

class WiringBase:
    
    def __init__(self, parameters):
        self.led_count = int(parameters.get("led_count", 114))
        led_pin = int(parameters.get("led_pin", 18))                        # GPIO pin connected to the pixels (18 uses PWM!).
        led_freq_hz = int(parameters.get("led_freq_hz", 800000))            # LED signal frequency in hertz (usually 800khz)
        led_dma = int(parameters.get("led_dma", 10))                        # DMA channel to use for generating signal (try 10)
        led_brightness = int(parameters.get("led_brightness", 255))         # Set to 0 for darkest and 255 for brightest
        led_invert = parameters.get("led_brightness", "False") == "True"    # True to invert the signal (when using NPN transistor level shift) 
        led_channel = int(parameters.get("led_channel", 0))                 # set to '1' for GPIOs 13, 19, 41, 45 or 53
        gamma_factor = float(parameters.get("gamma_factor", 1))                    
        gamma_table = None
        if gamma_factor != 1:
            gamma_table = self._get_gamma_table(gamma_factor) 
        
        self.strip = PixelStrip(self.led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel, gamma=gamma_table)
        self.strip.begin()
     
    def _get_gamma_table(self, factor):
        gamma_table = []
        for i in range(256):
            gamma_table.append(int(((i/255) ** factor) * 255 + 0.5))
        
        return gamma_table
        
    # Transform a row column to a position in the strip
    # 0,0 is the top left LED, and rows increase downwards, and columns to the right    
    def coordinates_to_strip_pos(self, row, column):
        pass
    
    # In case the the clock have the points in the corners (or more) this function returns the led position in the strip according to the point number
    # Similar to the coordinates, the first point (0) starts in the top left and goes clockwise
    def point_to_strip_pos(self, point):
        pass
    
    def set_pixel_color(self, pos, color):
        self.strip.setPixelColor(pos, color)
        
    def get_pixel_color(self, pos):
        return self.strip.getPixelColor(pos)
        
    def turn_all_off(self):
        for led in range(self.led_count):
            self.strip.setPixelColor(led, 0)   
        
    def refresh(self):
        self.strip.show()
        
def get_wiring_instance(class_name):
    name_and_classes = {cls.__name__ : cls for cls in WiringBase.__subclasses__()}
    return name_and_classes[class_name]
