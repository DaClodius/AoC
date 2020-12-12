def part_one():
    pointer = 0
    accumulator = 0
    previous_pointer = []
    while True:
        if pointer in previous_pointer:
            return accumulator
        previous_pointer.append(pointer)

        if commands[pointer][0] == 'nop':
            pointer += 1
        elif commands[pointer][0] == 'jmp':
            pointer += int(commands[pointer][1])        
        elif commands[pointer][0] == 'acc':
            accumulator += int(commands[pointer][1])
            pointer += 1
            
        #part_two
        if pointer >= len(commands):
            print(accumulator)
            return -1 

def part_two():
    checked_commands = []
    for pointer in range(len(commands)):
        if not pointer in checked_commands:
            if commands[pointer][0] == 'nop':
                checked_commands.append(pointer)
                commands[pointer][0] = 'jmp'
                if part_one() < 0:
                    return
                commands[pointer][0] = 'nop'
            elif commands[pointer][0] == 'jmp':
                checked_commands.append(pointer)
                commands[pointer][0] = 'nop'
                if part_one() < 0:
                    return
                commands[pointer][0] = 'jmp'

with open('input/day08') as file:
    commands = [line.split() for line in file]
    
print(part_one())
part_two()