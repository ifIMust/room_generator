import numpy as np

# a should mean width, b is height.
def generate_ellipse(a, b):
    assert a > 1
    assert b > 1
    
    data = np.zeros((a*2 + 1, b*2 + 1), dtype=np.uint8)

    # Center offset
    xc = a
    yc = b
    
    a2 = a*a
    b2 = b*b
    fa2 = 4*a2

    x = 0
    y = b
    sigma = 2*b2 + a2*(1 - 2*b)

    # First half in 4 quadrants
    while b2*x <= a2*y:
        data[xc + x][yc + y] = 1
        data[xc - x][yc + y] = 1
        data[xc + x][yc - y] = 1
        data[xc - x][yc - y] = 1

        if sigma >= 0:
            sigma += fa2*(1 - y)
            y -= 1
        sigma += b2*(4*x + 6)
        x += 1

    # Second half in 4 quadrants
    fb2 = 4*b2
    x = a
    y = 0
    sigma = 2*a2 + b2*(1 - 2*a)

    while a2*y <= b2*x:
        data[xc + x][yc + y] = 1
        data[xc - x][yc + y] = 1
        data[xc + x][yc - y] = 1
        data[xc - x][yc - y] = 1
        
        if sigma >= 0:
            sigma += fb2*(1 - x)
            x -= 1
        sigma += a2*(4*y + 6)
        y += 1
    
    return data.tolist()
