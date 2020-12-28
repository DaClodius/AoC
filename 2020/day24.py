from copy import copy


def part_one(tiles):
    return len([tile for tile in tiles if not tiles[tile]])


def part_two(tiles):

    def get_adjacents(tile):
        return [(tile[0] + 1, tile[1]),\
                (tile[0] + 1, tile[1] - 1),\
                (tile[0], tile[1] - 1),\
                (tile[0] - 1, tile[1]),\
                (tile[0] - 1, tile[1] + 1),\
                (tile[0], tile[1] + 1)]

    def add_new_adjacents(tile):
        for adjacent in get_adjacents(tile):
            if adjacent not in tiles.keys():
                tiles[adjacent] = True

    def count_black_adjacents(tile):
        return len([tile_ for tile_ in get_adjacents(tile) if tile_ in tiles and not tiles[tile_]])

    for _ in range(100):
        switch = []
        for tile in copy(tiles):
            add_new_adjacents(tile)
        for tile in tiles:
            black = count_black_adjacents(tile)
            if (tiles[tile] and black == 2) or (not tiles[tile] and (black == 0 or black > 2)):
                switch.append(tile)
        for tile in switch:
            tiles[tile] = not tiles[tile]

    return len([tile for tile in tiles if not tiles[tile]])


def get_tiles():

    def get_series_of_steps():

        def series_to_steps(series):
            return series\
                .replace('se', ',SE').replace('sw', ',SW')\
                .replace('nw', ',NW').replace('ne', ',NE')\
                .replace('e', ',E').replace('w', ',W')\
                .strip(',').split(',')

        series_of_steps = []

        with open('2020/input/day24') as file:
            for series in file.read().strip().split('\n'):
                series_of_steps.append(series_to_steps(series))
                
        return series_of_steps

    def go_step(tile, step):
        if step == 'E':
            return (tile[0] + 1, tile[1])
        elif step == 'SE':
            return (tile[0] + 1, tile[1] - 1)
        elif step == 'SW':
            return (tile[0], tile[1] - 1)
        elif step == 'W':
            return (tile[0] - 1, tile[1])
        elif step == 'NW':
            return (tile[0] - 1, tile[1] + 1)
        elif step == 'NE':
            return (tile[0], tile[1] + 1)

    tiles = {}

    for series in get_series_of_steps():
        tile = (0, 0)
        for step in series:
            tile = go_step(tile, step)
        tiles[tile] = False if tile not in tiles.keys() else not tiles[tile]
        
    return tiles

print(part_one(get_tiles()))
print(part_two(get_tiles()))
