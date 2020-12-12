import math

def solve(direction, position, waypoint):
    for action in actions:
        if action[0] == 'F':
            if waypoint:
                position = move_towards_waypoint(position, waypoint, action)
            else:
                position = move_forward(direction, position, action)
        elif action[0] in ['L', 'R']:
            if waypoint:
                waypoint = rotate_waypoint(position, waypoint, action)
            else:
                direction = change_direction(direction, action)
        elif action[0] in ['N', 'E', 'S', 'W']:
            if waypoint:
                waypoint = change_position(waypoint, action)
            else:
                position = change_position(position, action)
    return round(abs(position[0]) + abs(position[1]))

def move_forward(direction, position, action):
    return [position[0] + action[1] * math.sin(math.radians(direction)),
            position[1] + action[1] * math.cos(math.radians(direction))]

def move_towards_waypoint(position, waypoint, action):
    return [position[0] + action[1] * waypoint[0], 
            position[1] + action[1] * waypoint[1]]

def change_direction(direction, action):
    return direction + action[1] if action[0] == 'R' else direction - action[1]

def rotate_waypoint(position, waypoint, action):
    rad = math.radians(action[1]) if action[0] == 'R' else -math.radians(action[1])
    return [waypoint[0] * math.cos(rad) + waypoint[1] * math.sin(rad),
            -waypoint[0] * math.sin(rad) + waypoint[1] * math.cos(rad)]

def change_position(position, action):
    if action[0] == 'N':
        position[1] += action[1]
    elif action[0] == 'E':
        position[0] += action[1]
    elif action[0] == 'S':
        position[1] -= action[1]
    elif action[0] == 'W':
        position[0] -= action[1]
    return position

with open('input/day12') as file:
    actions = [(line[:1], int(line.strip()[1:])) for line in file]

print(solve(90, [0, 0], None)) #part_one
print(solve(90, [0, 0], [10, 1])) #part_two