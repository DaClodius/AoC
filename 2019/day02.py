from copy import copy

def part_one(code):
    code[1] = 12
    code[2] = 2
    return run(copy(code))[0]

def part_two(code):
    for noun in range(100):
        for verb in range(100):
            code_ = copy(code)
            code_[1] = noun
            code_[2] = verb
            run(code_)
            if code_[0] == 19690720:
                return str(noun) + str(verb)

def run(code):
    pointer = 0
    while code[pointer] != 99:
        if code[pointer] == 1:
            code[code[pointer + 3]] =  code[code[pointer + 1]] + code[code[pointer + 2]]
        elif code[pointer] == 2:
            code[code[pointer + 3]] =  code[code[pointer + 1]] * code[code[pointer + 2]]
        pointer += 4
    return code

with open('2019/input/day02') as file:
    int_code = [int(n) for n in file.read().strip().split(',')]

print(part_one(int_code))
print(part_two(int_code))