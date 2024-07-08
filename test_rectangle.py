import rectangle

class TestRectangle:
    def test_width(self):
        dim = 5
        rect = rectangle.generate_rectangle(dim, dim)
        assert len(rect) == dim

    def test_length(self):
        dim = 5
        rect = rectangle.generate_rectangle(dim, dim)
        assert len(rect) > 0
        assert len(rect[0]) == dim
        
    def test_upper_wall(self):
        dim = 3
        rect = rectangle.generate_rectangle(dim, dim)
        assert len(rect) > 0
        for i in range(0, len(rect[0])):
            assert rect[0][i] == 1
            
    def test_left_wall(self):
        dim = 3
        rect = rectangle.generate_rectangle(dim, dim)
        for i in range(0, len(rect)):
            assert rect[i][0] == 1
