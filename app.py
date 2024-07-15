from flask import Flask, abort, request
from circle import circle
from ellipse import ellipse
from rectangle import rectangle

import math
import random

# Ugly and hopefully temporary...
# Look for srspy nearby
from os import path
import sys
sys.path.append(path.abspath('../srsr/client/srsrpy'))
from srsrpy import ServiceRegistryClient

import signal


app = Flask(__name__)
random.seed()

try:
    svc_reg = ServiceRegistryClient('http://localhost:3434', 'room_generator', 'http://localhost:4949')
    svc_reg.register()

    # Assume registration was successful. Deregister on Ctrl-C
    prev_handler = signal.getsignal(signal.SIGINT)
    def handle_sigint(sig, frame):
        svc_reg.deregister()

        if prev_handler:
            prev_handler(sig, frame)
    signal.signal(signal.SIGINT, handle_sigint)
except:
    print("Couldn't connect to registry server.")



@app.route("/generate")
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
            return ellipse.generate_ellipse(math.floor(height / 2), math.floor(width / 2))

    return rectangle.generate_rectangle(height, width)
