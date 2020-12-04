import re

def part_one():
    valid = 0
    for line in open('input/day2'):
        data = re.split('-| |: ', line.rstrip())
        if int(data[0]) <= data[3].count(data[2]) <= int(data[1]):
            valid += 1
    return valid

def part_two():
    valid = 0
    for line in open('input/day2'):
        data = re.split('-| |: ', line.rstrip())
        if (data[3][int(data[0])-1] == data[2]) ^ (data[3][int(data[1])-1] == data[2]):
            valid += 1
    return valid

print(part_one())
print(part_two())