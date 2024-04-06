def increment_char(c):
    return chr(ord(c) + 1)


def transform_coord(x, y):
    return chr(x + (ord('A') - 1)) + str(y)


def search_ships(grid, x, y):
    coord_ships = []
    

