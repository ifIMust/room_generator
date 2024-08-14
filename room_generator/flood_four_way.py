import numpy as np
import numpy.ma as ma


def flood(data, start_point, find_color, repl_color):
    # Generate array of booleans as "Inside" mask
    inside = ma.equal(data, find_color).data
    flood_impl(data, inside, repl_color, start_point)


def flood_impl(data, inside, color, point):
    if is_inside(point, inside):
        print("writing point", point)
        write(data, inside, color, point)
        flood_impl(data, inside, color, (point[0], point[1] - 1))
        flood_impl(data, inside, color, (point[0], point[1] + 1))
        flood_impl(data, inside, color, (point[0] - 1, point[1]))
        flood_impl(data, inside, color, (point[0] + 1, point[1]))


def write(data, inside, color, point):
    data[point] = color
    inside[point] = False


def is_inside(point, inside):
    shape = np.shape(inside)
    if point[0] < 0 or point[1] < 0:
        return False
    if point[0] >= shape[0] or point[1] >= shape[1]:
        return False
    return inside[point]
