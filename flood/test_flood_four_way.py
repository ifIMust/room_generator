import pytest
from os import path
import sys
sys.path.append(path.dirname(path.realpath(__file__)) + "/..")
from rectangle import rectangle
from . import flood_four_way
import numpy as np


@pytest.fixture
def rect_three():
    return rectangle.generate_rectangle(3, 3)

@pytest.fixture
def flood_tiny_square(rect_three):
    data = np.array(rect_three['data'])
    start_point = (1, 1)
    find_color = 0
    repl_color = 2
    flood_four_way.flood(data, start_point, find_color, repl_color)
    return data


def test_flood_tiny_square_set_center(flood_tiny_square):
    assert flood_tiny_square[1][1] == 2


def test_flood_tiny_square_no_set_wall(flood_tiny_square):
    assert flood_tiny_square[0][1] == 1


@pytest.fixture
def rect_five():
    return rectangle.generate_rectangle(5, 5)


@pytest.fixture
def flood_five_square(rect_five):
    data = np.array(rect_five['data'])
    start_point = (1, 1)
    find_color = 0
    repl_color = 2
    flood_four_way.flood(data, start_point, find_color, repl_color)
    return data


def test_flood_five_square_filled(flood_five_square):
    assert flood_five_square[1][1] == 2
    assert flood_five_square[1][2] == 2
    assert flood_five_square[2][1] == 2
    assert flood_five_square[2][2] == 2


def test_flood_five_square_walls_not_filled(flood_five_square):
    assert flood_five_square[0][0] == 1
    assert flood_five_square[1][0] == 1
    assert flood_five_square[0][1] == 1


@pytest.fixture
def flood_five_square_center(rect_five):
    data = np.array(rect_five['data'])
    start_point = (2, 2)
    find_color = 0
    repl_color = 2
    flood_four_way.flood(data, start_point, find_color, repl_color)
    return data


def test_flood_five_square_center_filled(flood_five_square_center):
    for i in range (1, 4):
        for j in range (1, 4):
            assert flood_five_square_center[i][j] == 2


def test_flood_five_square_center_walls_not_filled(flood_five_square_center):
    for i in range (0, 5):
        assert flood_five_square_center[0][i] == 1
        assert flood_five_square_center[4][i] == 1
        assert flood_five_square_center[i][0] == 1
        assert flood_five_square_center[i][4] == 1

