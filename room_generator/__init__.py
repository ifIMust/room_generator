from flask import Flask, abort, request
from . import circle
from . import ellipse
from . import rectangle
import configparser
import math


# This style of factory function is for the flask debug server
# flask --app room_generator run
def create_app():
    init_service_registry()

    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(...)

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
                return ellipse.generate_ellipse(math.floor(height / 2),
                                                math.floor(width / 2))
        return rectangle.generate_rectangle(height, width)

    return app


def init_service_registry():
    config = configparser.ConfigParser()
    config.read('config.toml')
    use_srsrpy = config.getboolean('Service Registry', 'UseSrsrpy')

    if use_srsrpy:
        print("Using srsrpy service registry client.")
        import signal
        from srsrpy import srsrpy

        server_address = config.get('Service Registry', 'SrsrServer')
        service_registry = srsrpy.ServiceRegistryClient(server_address,
                                                        'room_generator',
                                                        port='4949')
        registered = service_registry.register()

        if registered:
            # Assume registration was successful. Deregister on Ctrl-C
            prev_handler = signal.getsignal(signal.SIGINT)

            def handle_sigint(sig, frame):
                service_registry.deregister()

                if prev_handler:
                    prev_handler(sig, frame)
            signal.signal(signal.SIGINT, handle_sigint)
