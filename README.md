# room_generator
## Description
room_generator is a service that generates small 2D "rooms" in json format.
This is useful for e.g. procedural roguelike/dungeon games if the rooms are aggregated into a larger level.
It is intended for use with [level_generator](https://github.com/ifIMust/level_generator).

The default (only) implementation creates a rectangle of the specified size, with walls surrounding an empty floor.

room_generator uses Python and Flask, with a venv virtual environment.

## Example usage
In the room_generator project directory, activate the venv environment:
`. .venv/bin/activate`

To run the service in debug mode on port 4949:
`flask run --port 4949`

To generate a room with height 12 and width 7, GET `/generate?h=12&w=7`
The output format is a (JSON) list of lists. Each nested list represents a row.
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

## Further Work
- Generate different types of rooms with different shapes.
- Register this service with a registry service.
