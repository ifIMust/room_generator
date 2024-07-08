
# 0 is floor, 1 is wall

# x and y are the outer dimensions. Wall tiles will fill the border. Floor tiles fill the remainder.
def generate_rectangle(x, y):
    tiles = []
    for i in range(0, x):
        tiles.append([])
        for j in range(0, y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                tiles[i].append(1) # Wall
            else:
                tiles[i].append(0) # Floor
    return tiles
