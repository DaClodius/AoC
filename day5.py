def part_one(codes):
    max_seat_id = 0
    for code in codes:
        seat_id = get_seat_id(code)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def part_two(codes):
    seat_ids = []
    for code in codes:
        seat_ids.append(get_seat_id(code))
    seat_ids.sort()
    for index, seat_id in enumerate(seat_ids):
        if seat_ids[index - 1] == seat_id - 2:
            return seat_id - 1
    return -1

def get_seat_id(code):
    row = binary_code_to_int(code[:-3], 'F', 'B')
    column = binary_code_to_int(code[-3:], 'L', 'R')
    return row * 8 + column

def binary_code_to_int(code, c0, c1):
    return int((code.replace(c0, '0').replace(c1, '1')), 2)

with open('input/day5') as _file:
    codes = [line.rstrip() for line in _file]

print(part_one(codes))
print(part_two(codes))