class Tile:
    
    def __init__(self, id, pixels):
        self.id = id
        self.pixels = pixels
        self.dim = len(pixels)

    @staticmethod
    def parse_raw(raw):
        return Tile(int(raw.split('\n')[0][-5: -1]), [line for line in raw.split('\n')[1:]])

    def top(self):
        return self.pixels[0]

    def bottom(self):
        return self.pixels[-1]

    def right(self):
        return ''.join(t[-1] for t in self.pixels)

    def left(self):
        return ''.join(t[0] for t in self.pixels)

    def flip(self):
        self.pixels = [t for t in reversed(self.pixels)]

    def rotate(self):
        self.pixels = [''.join([self.pixels[self.dim - j - 1][i] for j in range(self.dim)]) for i in range(self.dim)]

    def cut_edges(self):
        self.pixels = [''.join([self.pixels[i][j] for j in range(1, self.dim - 1)]) for i in range(1, self.dim - 1)]

    transitions = [lambda t: t, lambda t: t.rotate(), lambda t: t.rotate(), lambda t: t.rotate(), \
        lambda t: t.flip(), lambda t: t.rotate(), lambda t: t.rotate(), lambda t: t.rotate()]


def sort_tiles(tiles, tiles_, used):
    if len(tiles_) == len(tiles):
        return tiles_
    for tile in tiles:
        if tile not in used:
            for transition in Tile.transitions:
                transition(tile)
                if check_border_match(tiles_, tile):
                    result = sort_tiles(tiles, tiles_ + [tile], used.union({tile}))
                    if result:
                        return result


def check_border_match(tiles_, tile):
    return not ((len(tiles_) + 1 - IMAGE_DIM > 0 and tile.top() != tiles_[len(tiles_) - IMAGE_DIM].bottom()) \
        or ((len(tiles_) + 1) % IMAGE_DIM != 1 and tile.left() != tiles_[len(tiles_) - 1].right()))


def part_one():
    return SORTED_TILES[0].id * SORTED_TILES[IMAGE_DIM - 1].id * SORTED_TILES[len(TILES) - IMAGE_DIM].id * SORTED_TILES[len(TILES) - 1].id


def part_two():

    def image_from_sorted_tiles():
        image = ['' for _ in range((TILES[0].dim - 2) * IMAGE_DIM)]
        for i, tile in enumerate(SORTED_TILES):
            tile.cut_edges()
            for j, pixels in enumerate(tile.pixels):
                image[(i // IMAGE_DIM) * (TILES[0].dim - 2) + j] += pixels
        return Tile(None, image)

    def count_monsters(monster, image):
        for transition in Tile.transitions:
            transition(image)
            count = 0
            for i in range(0, len(image.pixels) - len(monster) + 1):
                for j in range(0, len(image.pixels[0]) - len(monster[0]) + 1):
                    valid = True
                    for k in range(len(monster)):
                        for l in range(len(monster[0])):
                            if (monster[k][l] != '.') and monster[k][l] != image.pixels[i + k][j + l]:
                                valid = False
                    if valid:
                        count += 1
            if count > 0:
                return count
        return 0

    monster = [
        '..................#.',
        '#....##....##....###',
        '.#..#..#..#..#..#...',
        ]
    image = image_from_sorted_tiles()
    return sum(line.count('#') for line in image.pixels) - count_monsters(monster, image) * 15


TILES = [Tile.parse_raw(raw_tile) for raw_tile in open('2020/input/day20').read().strip().split("\n\n")]
IMAGE_DIM = int(len(TILES) ** 0.5)
SORTED_TILES = sort_tiles(TILES, [], set())

print(part_one())
print(part_two())
