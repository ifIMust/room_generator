from . import circle
import numpy as np
import pytest

def test_gen_circle_r1_too_small():
    with pytest.raises(AssertionError):
        circle.generate_circle(1)

        
def test_circle_style_r2():
    assert circle.generate_circle(2)['style'] == 'circle'

    
def test_circle_shape_r2():
    assert circle.generate_circle(2)['shape'] == [5, 5]

    
def test_gen_circle_r2():
    expected = [[0, 1, 1, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0]]
    output = circle.generate_circle(2)
    assert expected == output['data']


def test_circle_style_r3():
    assert circle.generate_circle(3)['style'] == 'circle'

    
def test_circle_shape_r3():
    assert circle.generate_circle(3)['shape'] == [7, 7]

    
def test_gen_circle_r3():
    expected = [[0, 1, 1, 1, 1, 1, 0],
                [1, 1, 0, 0, 0, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1],
                [0, 1, 1, 1, 1, 1, 0]]
    output = circle.generate_circle(3)
    assert expected == output['data']


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
    assert expected == output['data']


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
    assert expected == output['data']
