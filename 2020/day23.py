def part_one(cups):
    index = 0
    for _ in range(100):
        current = cups[index]
        pick = (2 * cups)[cups.index(current) + 1: cups.index(current) + 4]
        for cup in pick:
            cups.remove(cup)
        destination = current - 1       
        while not destination in cups:
            destination -= 1
            if destination < min(cups):
                destination = max(cups)        
        destination_index = cups.index(destination) + 1
        cups[destination_index:destination_index] = pick
        while cups[index] != current:
            cups = cups[1:] + cups[:1]
        index = index + 1 if index + 1 < len(cups) else 0
    while cups[0] != 1:
        cups = cups[1:] + cups[:1]
    return ''.join([str(n) for n in cups[1:]])

def get_cups():
    return [int(n) for n in open('2020/input/day23').read().strip()]

print(part_one(get_cups()))