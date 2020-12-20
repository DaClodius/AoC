def part_one():
    matches = dict([key, 0] for key in tiles.keys())
    for root in tiles:
        for tile in tiles:         
            if tile is not root and check_match(tiles[root], tiles[tile]):
                matches[root] += 1
    result = 1
    for tile_id in [k for k, v in matches.items() if v == 2]:
        result *= tile_id
    return result

def check_match(root, tile):
    for _ in range(2):
        for _ in range(4):
            if compare_edges(root, tile):
                return True
            tile = rotate_tile(tile)
        root = rotate_tile(root)
        for _ in range(4):
            if compare_edges(root, tile):
                return True
            tile = rotate_tile(tile)
        tile = flip_tile(tile)
    return False

def compare_edges(root, tile):
    if tile[0] == root[len(tile)-1]:
        return True
    if tile[len(tile)-1] == root[0]:
        return True
    return False

def rotate_tile(tile):
    return [[tile[x][y] for x in range(len(tile))] for y in range(len(tile)-1, -1, -1)]

def flip_tile(tile):
    return [[tile[y][x] for x in range(len(tile))] for y in range(len(tile)-1, -1, -1)]

tiles = {}
with open('2020/input/day20') as file:
    for tile in file.read().strip().split('\n\n'):
        tiles[int(tile.split('\n')[0][-5: -1])] = [[char for char in line] for line in tile.split('\n')[1:]]

print(part_one())