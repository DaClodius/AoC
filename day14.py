def part_one(value_):
    memory[0][index] = int(''.join(
        [bitmask[pointer] if bitmask[pointer].isnumeric() else value_[pointer] for pointer in range(len(bitmask))]), 2)


def part_two(index_):
    index_ = [bitmask[pointer] if bitmask[pointer] == '1' else index_[pointer] for pointer in range(len(index_))]
    for numeric in range(pow(2, bitmask.count('X'))):
        for binary_index, binary_digit in enumerate(binary_string(numeric, bitmask.count('X'))):
            index_[len(bitmask) - len(bitmask.split('X', binary_index + 1)[-1]) - 1] = binary_digit
            memory[1][int(''.join(index_), 2)] = value


def binary_string(string, length):
    binary = '{0:b}'.format(string)
    return '0' * (length - len(binary)) + binary


with open('input/day14') as file:
    memory = [{}, {}]
    for line in [line.strip() for line in file]:
        if line.startswith('mask'):
            bitmask = line[7:]
        else:
            index = int(line[4:line.index(']')])
            value = int(line[line.index('=') + 1:])
            part_one(list(binary_string(value, len(bitmask))))
            part_two(list(binary_string(index, len(bitmask))))

print(sum(memory[0].values()))
print(sum(memory[1].values()))
