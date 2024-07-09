from flask import Flask, abort, request
from rectangle import rectangle

app = Flask(__name__)

@app.route("/generate")
def generate():
    height = request.args.get('h', default=3, type=int)
    width = request.args.get('w', default=3, type=int)

    if height < 3 or width < 3:
        abort(400)
        return
    rect = rectangle.generate_rectangle(height, width)
    return rect
