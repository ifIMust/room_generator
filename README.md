# room_generator
## Description
room_generator is a service that generates small 2D "rooms" in json format.
This is useful for e.g. procedural roguelike/dungeon games if the rooms are aggregated into a larger level.
It is intended for use with [level_generator](https://github.com/ifIMust/level_generator) (not yet released).

Depending on request criteria, it may create a rectangle, circle, or ellipse shape.
Walls have closed diagonals.

## Example usage
In the room_generator project directory, create and set up the venv environment:
```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Run the debug server on port 4949:
```
flask run --port 4949
```

To generate a room with height 12 and width 7, GET `/generate?h=12&w=7`
The output format is a JSON document describing the room. Each nested list in `data` represents a row.
0 is floor, 1 is wall.

`h` and `w` have a minimum size of 3 and default of 3.

For instance, `http://localhost:5000/generate?h=3&w=4` yields (when pretty-printed):
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

## Configuration
room_generator has support for the service registry [srsr](https://github.com/ifIMust/srsr).
If configured, it will self-register, using the [srsrpy](https://github.com/ifIMust/srsrpy) client.

Edit config.toml, set `UseSrsrpy = yes`, and set `SrsrServer` to the srsr server's address.

## Further Work
- Restructure the project to work with gunicorn.
- Use gunicorn configuration to standardize port binding.
- Add API tests.
- Permit client to request a room type.
- Generate other, more interesting room shapes.
