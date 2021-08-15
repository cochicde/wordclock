from rpi_ws281x import Color

def get_color_from_row(row):
    return {
            0: Color(255, 0, 0), #red
            1: Color(255, 0, 0), #red
                    
            2: Color(255, 128, 0), #orange
            3: Color(255, 128, 0), #orange
            
            4: Color(255, 255, 0), #yellow
            
            5: Color(0, 255, 0), #green
            6: Color(0, 255, 0), #green
            
            7: Color(0, 0, 255), #blue
            
            8: Color(128, 0, 128), #purple
            9: Color(128, 0, 128), #purple
        }[row]
     