def compute_next_cube_generation(dim, cubes):
    next_cube_generation = {}
    for location in cubes:
        active_neighbours_count = get_active_neighbours_count(dim, location, cubes)
        if cubes[location] == '#':
            next_cube_generation[location] = '#' if 1 < active_neighbours_count < 4 else '.'
            process_cube_neighbours(dim, location, cubes, next_cube_generation)
        elif cubes[location] == '.':
            next_cube_generation[location] = '#' if active_neighbours_count == 3 else '.'
    return next_cube_generation


def process_cube_neighbours(dim, location, cubes, next_cube_generation):
    for location in get_neighbour_locations(dim, location):
        if location not in cubes and get_active_neighbours_count(dim, location, cubes) == 3:
            next_cube_generation[location] = '#'


def get_active_neighbours_count(dim, location, cubes):
    return len([location for location in get_neighbour_locations(dim, location) if cubes.get(location) == '#'])


def get_neighbour_locations(dim, location):
    neighbour_locations = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                add_neighbour_locations_by_dim(dim, neighbour_locations, location, x, y, z)
    return neighbour_locations


def add_neighbour_locations_by_dim(dim, neighbour_locations, location, x, y, z):
    if dim == 3:
        if (x, y, z) != (0, 0, 0):
            neighbour_locations.append((location[0] + x, location[1] + y, location[2] + z))
    elif dim == 4:
        for w in range(-1, 2):
            if (x, y, z, w) != (0, 0, 0, 0):
                neighbour_locations.append((location[0] + x, location[1] + y, location[2] + z, location[3] + w))


def load_cubes(dim):
    cubes = {}
    with open('2020/input/day17') as file:
        grid = [line.strip() for line in file]
        for y, line in enumerate(grid):
            for x, char in enumerate(line):
                if dim == 3:
                    cubes[(y, x, 0)] = char
                elif dim == 4:
                    cubes[(y, x, 0, 0)] = char
    return cubes


def run(dim):
    cubes = load_cubes(dim)
    for _ in range(6):
        cubes = compute_next_cube_generation(dim, cubes)
    return list(cubes.values()).count('#')


print(run(3))  # part_one
print(run(4))  # part_two
