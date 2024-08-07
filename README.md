# room_generator
## Description
room_generator is a service that generates small 2D "rooms" in json format.
This is useful for e.g. procedural roguelike/dungeon games if the rooms are aggregated into a larger level.
It is intended for use with [level_generator](https://github.com/ifIMust/level_generator).

The main implementation creates a rectangle of the specified size, with walls surrounding an empty floor.
If conditions are right, a circular room may be generated.

## Example usage
Example setup with venv:
In the room_generator project directory, create and set up the venv environment:
```
python3 -m venv .venv
. .venv/bin/activate
pip install flask numpy
```
To run the service in debug mode on port 4949:
`flask run --port 4949`

To generate a room with height 12 and width 7, GET `/generate?h=12&w=7`
The output format is a JSON-style list of lists. Each nested list represents a row.
0 is floor, 1 is wall.

`h` and `w` have a minimum size of 3 and default of 3.

For instance, `http://localhost:5000/generate?h=3&w=4` yields `[[1,1,1,1],[1,0,0,1],[1,1,1,1]]` or pretty-printed:
```
[
  [1, 1, 1, 1],
  [1, 0, 0, 1],
  [1, 1, 1, 1]
]
```

## Configuration
room_generator supports registration with [srsr](https://github.com/ifIMust/srsr).
Install the srsrpy client from the PyPI test instance:
```
pip install -i https://test.pypi.org/simple/ srsrpy
pip install requests
```
Edit config.toml, set `UseSrsrpy = yes`, and set `SrsrServer` to the srsr server's address.

## Further Work
- Use a more formal flask app project structure.
- Get the flask app address dynamically, to use for service registration.
- Write API tests.
- Permit client to request a room type.
- Generate other, more interesting room shapes.
- Use a logger.
