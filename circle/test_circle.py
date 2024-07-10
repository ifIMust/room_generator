import circle
import numpy as np
import pytest

def test_gen_circle_r1_too_small():
    with pytest.raises(AssertionError):
        circle.generate_circle(1)


def test_gen_circle_r2():
    expected = [[0, 1, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0]]
    output = circle.generate_circle(2)
    assert expected == output


def test_gen_circle_r3():
    expected = [[0, 1, 1, 1, 1, 1, 0],
                [1, 1, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1],
                [0, 1, 1, 1, 1, 1, 0]]
    output = circle.generate_circle(3)
    assert expected == output


def test_gen_circle_r4():
    expected = [[0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 1],
                [0, 1, 1, 0, 0, 0, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 0, 0]]
    output = circle.generate_circle(4)
    assert expected == output


def test_gen_circle_r5():
    expected = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]]
    output = circle.generate_circle(5)
    assert expected == output


@pytest.fixture
def grid_tiny():
    return np.zeros((3, 3), dtype=np.uint8)


def test_count_ortho_neighbors_none(grid_tiny):
    pos = (1, 1)
    grid_tiny[pos] = 1
    assert circle.count_ortho_neighbors(grid_tiny, (1, 1)) == 0


def test_count_ortho_neighbors_one_north(grid_tiny):
    pos = (1, 1)
    grid_tiny[pos] = 1
    grid_tiny[(0, 1)] = 1
    assert circle.count_ortho_neighbors(grid_tiny, (1, 1)) == 1


def test_count_ortho_neighbors_one_south(grid_tiny):
    pos = (1, 1)
    grid_tiny[pos] = 1
    grid_tiny[(2, 1)] = 1
    assert circle.count_ortho_neighbors(grid_tiny, (1, 1)) == 1


def test_count_ortho_neighbors_one_west(grid_tiny):
    pos = (1, 1)
    grid_tiny[pos] = 1
    grid_tiny[(1, 0)] = 1
    assert circle.count_ortho_neighbors(grid_tiny, (1, 1)) == 1


def test_count_ortho_neighbors_one_east(grid_tiny):
    pos = (1, 1)
    grid_tiny[pos] = 1
    grid_tiny[(1, 2)] = 1
    assert circle.count_ortho_neighbors(grid_tiny, (1, 1)) == 1


def test_count_ortho_neighbors_four(grid_tiny):
    pos = (1, 1)
    grid_tiny[pos] = 1
    grid_tiny[(0, 1)] = 1
    grid_tiny[(2, 1)] = 1
    grid_tiny[(1, 0)] = 1
    grid_tiny[(1, 2)] = 1
    assert circle.count_ortho_neighbors(grid_tiny, (1, 1)) == 4
