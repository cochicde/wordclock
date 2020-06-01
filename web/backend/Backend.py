from flask import Flask
#from flask_swagger_ui import get_swaggerui_blueprint
import _thread

class Backend:
    app = Flask(__name__)
    
    def __init__(self, matrix):
        self.app.matrix = matrix
        _thread.start_new_thread(self.threaded_app, ())
        
    def threaded_app(self):
        port = 8080 
        self.app.run(host='0.0.0.0', port=port)

@Backend.app.route('/')
def hello_world():
    return 'Hello, World!'

@Backend.app.route('/row/<int:row_pos>')
def show_post(row_pos):
    Backend.app.matrix.turn_rows_on([row_pos])
    Backend.app.matrix.refresh()
    return "Ok"