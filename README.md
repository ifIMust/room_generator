# room_generator
## Description
room_generator is a service that generates small 2D "rooms" in json format.
This is useful for e.g. procedural roguelike/dungeon games if the rooms are aggregated into a larger level.
It is intended for use with [level_generator](https://github.com/ifIMust/level_generator) (not yet released).

Depending on request criteria, it may create a rectangle, circle, or ellipse shape.
Walls have closed diagonals.

room_generator runs in Google App Engine. You can deploy it to your own application or [try it here](https://trogue.wm.r.appspot.com/)

## Usage
To generate a room with height 12 and width 7, GET `/?h=12&w=7`
`h` and `w` have a minimum size of 3 and default of 3.

The output format is a JSON document describing the room. Each nested list in `data` represents a row.
0 is floor, 1 is wall.

### Example
If a local server is running on port 4949, `http://localhost:4949/?h=3&w=4` yields (when pretty-printed):
```
{
  "data": [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
  ],
  "shape": [3, 4],
  "style": "rectangle"
}
```

## Running a local instance
In the room_generator project directory, create and set up the venv environment:
```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Using gunicorn:
```
gunicorn 'room_generator:create_app()'
```

Using the debug server:
```
flask --app room_generator run --port 4949
```

Using waitress:
```
pip install waitress
waitress-serve --host 127.0.0.1 --port 4949 --call room_generator:create_app
```

## Further Work
- Add API tests.
- Permit client to request a room type.
- Generate other, more interesting room shapes.
