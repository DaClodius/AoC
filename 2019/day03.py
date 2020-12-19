def run(paths):
    first_wire = get_locations(paths[0], None)
    second_wire = get_locations(paths[1], None)
    intersections = get_locations(paths[1], first_wire)
    # part_one
    print(min(map(lambda x: abs(x[0]) + abs(x[1]), intersections)))
    # part_two
    print(min(first_wire[inter] + second_wire[inter] for inter in intersections))

def get_locations(paths, check_interceptions):
    steps = 0
    locations = {}
    location = (0, 0)
    for path in paths:
        for _ in range(int(path[1:])):
            steps += 1
            if path[0] == 'R':
                location = (location[0] + 1, location[1])
            elif path[0] == 'L':
                location = (location[0] - 1, location[1])
            elif path[0] == 'U':
                location = (location[0], location[1] + 1)
            elif path[0] == 'D':
                location = (location[0], location[1] - 1)
            add_location(location, locations, check_interceptions, steps)
    return locations

def add_location(location, locations, check_interceptions, steps):
    if check_interceptions:
        if location in check_interceptions:
            locations[location] = None
    else:
        locations[location] = steps

paths = []
for line in open('2019/input/day03'):
    paths.append(line.strip().split(','))
run(paths)