from copy import deepcopy

def run(seat_map, deep, max_occupied):
    while True:
        change = False
        occupied_counter = 0
        seat_map_copy = deepcopy(seat_map)
        for row in range(row_count):
            for seat in range(seat_count):
                if seat_map[row][seat] == occupied:
                    occupied_counter += 1
                if set_seat_state(seat_map, seat_map_copy, row, seat, max_occupied, deep):
                    change = True
        if change:
            seat_map = deepcopy(seat_map_copy)
        else:
            return occupied_counter

def set_seat_state(seat_map, seat_map_copy, row, seat, max_occupied, deep):
    change = False
    if seat_map[row][seat] == floor:
        return False
    elif count_adjacents(seat_map, row, seat, deep) == 0 and seat_map[row][seat] == empty:
        seat_map_copy[row][seat] = occupied
        change = True
    elif count_adjacents(seat_map, row, seat, deep) >= max_occupied and seat_map[row][seat] == occupied:
        seat_map_copy[row][seat] = empty
        change = True
    return change

def count_adjacents(seat_map, row, seat, deep):
    adjacents = 0
    for direction in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, -1), (-1, 0)]:
        adjacents += check_adjacent_in_direction(seat_map, row, seat, direction, deep)
    return adjacents

def check_adjacent_in_direction(seat_map, row, seat, direction, deep):
    while 0 <= row + direction[1] < row_count and 0 <= seat + direction[0] < seat_count:
        row += direction[1]
        seat += direction[0]
        if seat_map[row][seat] == occupied:
           return 1
        elif seat_map[row][seat] == empty:
           return 0
        elif not deep:
            return 0
    return 0

floor = '.'
empty = 'L'
occupied = '#'

with open('input/day11') as file:
    seat_map = list(list(line.strip()) for line in file)

row_count = len(seat_map)
seat_count = len(seat_map[0])

print(run(seat_map, False, 4)) #part_one
print(run(seat_map, True, 5)) #part_two
