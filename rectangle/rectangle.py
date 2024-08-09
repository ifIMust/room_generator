# Wall tiles will fill the border. Floor tiles fill the remainder.
# 0 is floor, 1 is wall.
def generate_rectangle(height, width):
    tiles = []
    for i in range(0, height):
        # Create a row
        tiles.append([])
        for j in range(0, width):
            # Fill the column value for this row
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                tiles[i].append(1)  # Wall
            else:
                tiles[i].append(0)  # Floor
    room = {'style': 'rectangle', 'shape': [height, width], 'data': tiles}
    return room
