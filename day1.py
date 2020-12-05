def part_one(nums):
    for num in nums:
        if 2020 - num in set(nums):
            return num * (2020 - num)

def part_two(nums):
    for num1 in nums:
        for num2 in nums:
            if 2020 - num1 - num2 in set(nums):
                return num1 * num2 * (2020 - num1 - num2)

with open('input/day1') as _file:
    nums = [int(line.rstrip()) for line in _file]

print(part_one(nums))
print(part_two(nums))
