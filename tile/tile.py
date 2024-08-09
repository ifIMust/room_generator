from enum import IntFlag


class Tile(IntFlag):
    VOID = 0
    FLOOR = 1
    WALL = 2
