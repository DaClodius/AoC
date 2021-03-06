import re


def part_one():
    valid = 0
    for data in data_set:
        if int(data[0]) <= data[3].count(data[2]) <= int(data[1]):
            valid += 1
    return valid


def part_two():
    valid = 0
    for data in data_set:
        if (data[3][int(data[0]) - 1] == data[2]) ^ (data[3][int(data[1]) - 1] == data[2]):
            valid += 1
    return valid


def get_data_set(lines):
    data_set_ = []
    for line in lines:
        data_set_.append(re.split('-| |: ', line.rstrip()))
    return data_set_


with open('2020/input/day02') as _file:
    data_set = get_data_set(_file.readlines())

print(part_one())
print(part_two())
