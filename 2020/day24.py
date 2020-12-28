def part_one(series_of_steps):
    tiles = {}
    for series in series_of_steps:
        tile = (0, 0)
        for step in series:
            tile = go_step(tile, step)
        if tile not in list(tiles):
            tiles[tile] = True
        else:
            tiles[tile] = not tiles[tile]
    return len([tile for tile in tiles.values() if tile])
    
def go_step(tile, step):
    if step == 'E':
        return (tile[0] + 1, tile[1])
    if step == 'SE':
        return (tile[0] + 1, tile[1] - 1)
    if step == 'SW':
        return (tile[0], tile[1] - 1)
    if step == 'W':
        return (tile[0] - 1, tile[1])
    if step == 'NW':
        return (tile[0] - 1, tile[1] + 1)
    if step == 'NE':
        return (tile[0], tile[1] + 1)

def get_series_of_steps():
    series_of_steps = []
    with open('2020/input/day24') as file:
        for series in file.read().strip().split('\n'):
            series_of_steps.append(series_to_steps(series))
    return series_of_steps

def series_to_steps(series):
    return series\
        .replace('se', ',SE').replace('sw', ',SW')\
        .replace('nw', ',NW').replace('ne', ',NE')\
        .replace('e', ',E').replace('w', ',W')\
        .strip(',').split(',')

print(part_one(get_series_of_steps()))
