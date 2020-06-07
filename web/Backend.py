from flask import Flask, render_template
import _thread
from rpi_ws281x import Color

class Backend:
    app = Flask(__name__)
    
    def __init__(self, matrix):
        self.app.matrix = matrix
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
def turn_on(row_pos, column_pos, color):
    rgb_color = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    Backend.app.matrix.turn_on_matrix_position([(row_pos, column_pos)], Color(rgb_color[0], rgb_color[1], rgb_color[2]))
    Backend.app.matrix.refresh()
    return "Ok"

