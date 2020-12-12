from collections import Counter

def part_one():
    return sum([len(Counter(''.join(g))) for g in groups])

def part_two():
    return sum([len([v for v in Counter(''.join(g)).values() if v == len(g)]) for g in groups])

with open('input/day06') as f:
    groups = [l.strip().split() for l in f.read().split('\n\n')]

print(part_one())
print(part_two())
