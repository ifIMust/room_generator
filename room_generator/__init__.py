from flask import Flask, abort, request
from . import circle
from . import ellipse
from . import rectangle
import math


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def generate():
        height = request.args.get('h', default=3, type=int)
        width = request.args.get('w', default=3, type=int)

        if height < 3 or width < 3:
            abort(400)
            return

        # Check if candidate for circle or ellipse
        if height % 2 == 1 and height >= 5:
            # Equal dimensions: do a circle.
            if height == width:
                return circle.generate_circle(math.floor(height / 2))
            elif width % 2 == 1 and width >= 5:
                return ellipse.generate_ellipse(math.floor(height / 2),
                                                math.floor(width / 2))
        return rectangle.generate_rectangle(height, width)

    return app
