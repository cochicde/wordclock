from flask import Flask, render_template, request, jsonify
import _thread
from rpi_ws281x import Color

class Backend:
    app = Flask(__name__)
    
    def __init__(self, matrix, scheduler):
        self.app.matrix = matrix
        self.app.scheduler = scheduler
        _thread.start_new_thread(self.threaded_app, ())
        
    def threaded_app(self):
        port = 80 
        self.app.run(host='0.0.0.0', port=port)

@Backend.app.route('/')
def hello_world():
    return render_template("index.html")

@Backend.app.route('/row/<int:row_pos>')
def show_post(row_pos):
    Backend.app.matrix.turn_rows_on([row_pos])
    Backend.app.matrix.refresh()
    return "Ok"

@Backend.app.route('/turn_on/<int:row_pos>/<int:column_pos>/<string:color>', methods=['POST'])
def turn_on_one(row_pos, column_pos, color):
    rgb_color = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    Backend.app.matrix.turn_on_matrix_position([(row_pos, column_pos)], Color(rgb_color[0], rgb_color[1], rgb_color[2]))
    Backend.app.matrix.refresh()
    return "Ok"

@Backend.app.route('/turn_on/', methods=['POST'])
def turn_on():
    for led in request.json.get("leds", []):
        colors = led["color"].split(",")
        Backend.app.matrix.turn_on_matrix_position([(led["row"], led["column"])], Color(int(colors[0]), int(colors[1]), int(colors[2])))
    
    Backend.app.matrix.refresh()
    return "Ok"

@Backend.app.route('/state/', methods=['GET'])
def get_state():
    state = {}
    state["leds"] = []
    led_array = state["leds"] 
    
    
    all_coordinates = [] 
    for row in range(Backend.app.matrix.rows):
        for column in range(Backend.app.matrix.columns):
            all_coordinates.append((row, column))
            
    all_colors = Backend.app.matrix.get_pixel_colors_rgb(all_coordinates)
    
    for coordinate, color in zip(all_coordinates, all_colors):
        led_object = {}
        led_object["row"] = coordinate[0]
        led_object["column"] = coordinate[1]
        led_object["color"] = str(color.r) + ", " + str(color.g) + ", " + str(color.b) 
        led_array.append(led_object)
    
    return jsonify(state)    

@Backend.app.route('/clockState/<int:state>', methods=['POST'])
def change_scheduler_state(state):
    if state == 1:
        Backend.app.scheduler.pause()
    else:
        Backend.app.scheduler.resume()
    
    return "ok"