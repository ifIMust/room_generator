import ellipse
import numpy as np
import pytest

def test_gen_ellipse_min_a():
    with pytest.raises(AssertionError):
        ellipse.generate_ellipse(1, 4)

def test_gen_ellipse_min_b():
    with pytest.raises(AssertionError):
        ellipse.generate_ellipse(4, 1)


def test_gen_ellipse_any():
    el = ellipse.generate_ellipse(3, 4)
