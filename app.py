from flask import Flask, abort, request
from circle import circle
from rectangle import rectangle
import math
import random

app = Flask(__name__)
random.seed()

@app.route("/generate")
def generate():
    height = request.args.get('h', default=3, type=int)
    width = request.args.get('w', default=3, type=int)

    if height < 3 or width < 3:
        abort(400)
        return

    # Technically h=5 works too but it comes out same as rectangle
    if height == width and height % 2 == 1 and height >= 7:
        return circle.generate_circle(math.floor(height / 2))
    
    rect = rectangle.generate_rectangle(height, width)
    return rect
