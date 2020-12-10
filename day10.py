def part_one():
    deltas = []
    for index in range(len(adapters) - 1):
        deltas.append(adapters[index + 1] - adapters[index])
    return (deltas.count(1)) * (deltas.count(3))

def part_two():
    return adapter_recursion(0, {})

def adapter_recursion(index, done):
    if index == len(adapters) - 1:
        return 1
    elif index in done:
        return done[index]
    counter = 0
    for next_index in range(index + 1, len(adapters)):
        if adapters[next_index] - adapters[index] <= 3:
            counter += adapter_recursion(next_index, done)
    done[index] = counter
    return counter

with open('input/day10') as file:
    adapters = [int(line.strip()) for line in file]
    adapters = sorted(adapters + [0, max(adapters) + 3])

print(part_one())
print(part_two())
