def part_one():
    return count_answers(False)

def part_two():
    return count_answers(True)

def count_answers(everyone):
    summa = 0
    for group in groups:
        answers_counter = [0] * 26
        for answers in group.split('\n'):
            for answer in answers:
                answers_counter[ord(answer) - 97] += 1
        if everyone:
            summa += answers_counter.count(group.count('\n') + 1)
        else:
            summa += 26 - answers_counter.count(0)
    return summa

with open('input/day6') as _file:
    groups = _file.read().strip('\n').split('\n\n')

print(part_one())
print(part_two())
