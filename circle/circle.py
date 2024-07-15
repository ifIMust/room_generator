import numpy as np

# Circle rasterizing code adapted from "3D Game Engine Design", 2nd Ed. David H Eberly
# Each loop iteration draws the same point in symmetry to 8 sections of the circle.
# Extra points are drawn to ensure closed orthogonal walls.
def draw_times_8(data, r, x, y):
    data[r + x][r + y] = 1
    data[r + x][r - y] = 1
    data[r - x][r + y] = 1
    data[r - x][r - y] = 1
    data[r + y][r + x] = 1
    data[r + y][r - x] = 1
    data[r - y][r + x] = 1
    data[r - y][r - x] = 1


def generate_circle(r):
    assert r > 1
    if r == 2:
        return five_by_five()
    
    dim = r * 2 + 1
    data = np.zeros((dim, dim), dtype=np.uint8)

    x = 0
    y = r
    dec = 3 - 2*r
    just_decremented_y = False

    while x <= y:
        draw_times_8(data, r, x, y)

        # This tweak to this algorithm yields a "fatter" rasterize.
        # Instead of picking the nearest next point, also draw the alternative point.
        if just_decremented_y:
            draw_times_8(data, r, x, y + 1)
        
        if dec >= 0:
            y -= 1
            dec += -4*y + 4
            just_decremented_y = True
        else:
            just_decremented_y = False
        dec += 4*x + 6
        x += 1

    # Close the final missing diagonal:
    if x > 1:
        draw_times_8(data, r, x, y + 1)

    return data.tolist()


# Special case because the algorithm draws 5x5 as a rectangle.
def five_by_five():
    return [[0, 1, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 1, 0]]

# count_ortho_neighbors was written with the intention of using it for filtering
# generated circles to fill in missing cells. It is obsolete with the addition of
# the above "fat rasterize".
# Assumption: pos is at least one space from any edge. It is safe to index +/-1.
# Count wall (1) cells in the cardinal directions neighboring pos.
def count_ortho_neighbors(data, pos):
    n = 0
    if data[pos[0] - 1][pos[1]] == 1:
        n += 1
    if data[pos[0] + 1][pos[1]] == 1:
        n += 1
    if data[pos[0]][pos[1] - 1] == 1:
        n += 1
    if data[pos[0]][pos[1] + 1] == 1:
        n += 1
    return n
