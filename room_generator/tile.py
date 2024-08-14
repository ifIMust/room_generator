from enum import IntFlag


class Tile(IntFlag):
    FLOOR = 0
    WALL = 1
    VOID = 0x7F
