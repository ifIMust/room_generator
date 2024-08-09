from . import rectangle
import pytest

square_dim = 5

@pytest.fixture
def square():
    return rectangle.generate_rectangle(square_dim, square_dim)


class TestRectangle:
    def test_style(self, square):
        assert square['style'] == 'rectangle'
    
    def test_data_height(self, square):
        assert len(square['data']) == square_dim

    def test_shape_height(self, square):
        assert square['shape'][0] == square_dim

    def test_data_width(self, square):
        assert len(square['data']) > 0
        assert len(square['data'][0]) == square_dim

    def test_shape_width(self, square):
        assert square['shape'][1] == square_dim

    def test_floor(self):
        dim = 3
        rect = rectangle.generate_rectangle(dim, dim)
        assert(rect['data'][1][1] == 0)
        
    def test_upper_wall(self):
        dim = 3
        rect = rectangle.generate_rectangle(dim, dim)
        assert len(rect['data']) > 0
        for i in range(0, len(rect['data'][0])):
            assert rect['data'][0][i] == 1
            
    def test_left_wall(self):
        dim = 3
        rect = rectangle.generate_rectangle(dim, dim)
        for i in range(0, len(rect['data'])):
            assert rect['data'][i][0] == 1

    def test_rectangle(self):
        width = 4
        height = 3
        rect = rectangle.generate_rectangle(height, width)
        expected = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
        assert expected == rect['data']
        assert rect['shape'][0] == height
        assert rect['shape'][1] == width
