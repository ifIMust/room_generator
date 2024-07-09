from flask import Flask, abort, request
from rectangle import rectangle

app = Flask(__name__)

@app.route("/generate")
def generate():
    width = request.args.get('w', default=3, type=int)
    height = request.args.get('h', default=3, type=int)
    if width < 3 or height < 3:
        abort(400)
        return
    rect = rectangle.generate_rectangle(width, height)
    return rect
