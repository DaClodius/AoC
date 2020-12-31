def get_keys():
    with open('2020/input/day25') as file:
        return int(file.readline()), int(file.readline())

def part_one():
    
    card_key, door_key = get_keys()
    modulo = 20201227
    subject = 7

    value = 1
    for loop_size in range(1, modulo):
        value = (value * subject) % modulo
        if value == door_key:
            break

    encryption_key = 1
    for _ in range(0, loop_size):
        encryption_key = (encryption_key * card_key) % modulo

    return encryption_key

print(part_one())
