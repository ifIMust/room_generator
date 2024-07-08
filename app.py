from flask import Flask
from flask import request
from rectangle import rectangle

app = Flask(__name__)

@app.route("/generate")
def generate():
    width = request.args.get('w', default=3, type=int)
    height = request.args.get('h', default=3, type=int)
    rect = rectangle.generate_rectangle(width, height)
    return rect
