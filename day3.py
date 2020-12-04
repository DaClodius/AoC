def part_one(grid):
    return trees_on_slope(grid, 3, 1)

def part_two(grid):
    product = 1
    input = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for tuple in input:
        product *= trees_on_slope(grid, tuple[0], tuple[1])
    return product

def trees_on_slope(grid, dx, dy):
    trees, pos_x, pos_y = 0, 0, 0
    while pos_y < len(grid):
        if grid[pos_y][pos_x] == '#':
            trees += 1
        pos_x += dx
        if pos_x >= len(grid[pos_y]):
            pos_x -= len(grid[pos_y])
        pos_y += dy    
    return trees

with open('input/day3') as _file:
    grid = [line.rstrip() for line in _file]

print(part_one(grid))
print(part_two(grid))
