
# --------------------------------------------------------
# define the world by assembling the pre-set compus_spaces
# --------------------------------------------------------

world_map = {}
starting_position = (0, 0)

# return a tile at the given coordinates if it exists

def tile_exists(x, y):
    return world_map.get((x, y))


def load_tiles():

    # pulls tile organization from file

    with open('resources/map.txt', 'r') as f:
        full = f.readlines()

    x_max = len(full[0].split())

    for y in range(0,len(full)):
        row = full[y].split()

        for x in range(0,x_max):
            tile_name = row[x]

            if tile_name == 'starting_room':
                global starting_position
                starting_position = (x, y)

            if tile_name == '.':
                world_map[(x, y)] = None
            else:
                world_map[(x, y)] = getattr(__import__('tiles'), tile_name)(x, y)
