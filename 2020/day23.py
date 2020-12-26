def part_one():
    cups_dict = run_game(get_cups(), 100)
    result = [cups_dict[1]]
    while result[-1] != 1:
        result.append(cups_dict[result[-1]])
    print(''.join([str(c) for c in result[:-1]]))

def part_two():
    cups = get_cups()
    cups = cups + list(range(len(cups) + 1, 10**6 + 1))
    cups = run_game(cups, 10**7)
    print(cups[1] * cups[cups[1]])

def run_game(cups, moves):
    current = cups[0]
    min_max = (min(cups), max(cups))
    cups_dict = dict(zip(cups, cups[1:]))
    cups_dict[cups[-1]] = cups[0]
    for _ in range(moves):
        pick = pick_three(cups_dict, current)
        destination = current - 1
        while destination in pick or destination < min_max[0]:
            destination = get_destination(destination, min_max)
        cups_dict[current] = cups_dict[pick[-1]]
        cups_dict[pick[-1]] = cups_dict[destination]
        cups_dict[destination] = pick[0]
        current = cups_dict[current]
    return cups_dict

def pick_three(cups_dict, current):
    pick = [cups_dict[current]]
    pick.append(cups_dict[pick[-1]])
    pick.append(cups_dict[pick[-1]])
    return pick

def get_destination(current, min_max):
    destination = current - 1
    if destination < min_max[0]:
        destination = min_max[1]
    return destination

def get_cups():
    return [int(n) for n in open('2020/input/day23').read().strip()]

part_one()
part_two()
