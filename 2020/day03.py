def part_one():
    return trees_on_slope(3, 1)


def part_two():
    product = 1
    tuples = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for tuple_ in tuples:
        product *= trees_on_slope(tuple_[0], tuple_[1])
    return product


def trees_on_slope(dx, dy):
    trees, pos_x, pos_y = 0, 0, 0
    while pos_y < len(grid):
        if grid[pos_y][pos_x] == '#':
            trees += 1
        pos_x += dx
        if pos_x >= len(grid[pos_y]):
            pos_x -= len(grid[pos_y])
        pos_y += dy
    return trees


with open('2020/input/day03') as _file:
    grid = [line.rstrip() for line in _file]

print(part_one())
print(part_two())
