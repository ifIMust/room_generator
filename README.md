# Description
room_generator is a service that generates small 2D "rooms" in json format.
This is useful for e.g. procedural roguelike/dungeon games if the rooms are aggregated into a larger level.

The default (only) implementation creates a rectangle of the specified size, with walls surrounding an empty floor.

room_generator uses Python and Flask, with a venv virtual environment.

## Example usage
In a terminal, activate the venv environment:
`. .venv/bin/activate`

To run the service in debug mode:
`flask run`

To generate a room with width 7 and height 12, GET `/generate/w=7&h=12`
The output format is a (JSON) list of lists. Each nested list represents a column.
0 is floor, 1 is wall.

`w` and `h` have a minimum size of 3 and default of 3.

For instance, `http://localhost:5000/generate?w=4&h=3` yields `[[1,1,1,1],[1,0,0,1],[1,1,1,1]]`
