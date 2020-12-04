def part_one(nums, set_nums):
    for num in nums:
        if 2020 - num in set_nums:
            return num * (2020 - num)

def part_two(nums, set_nums):
    for num in nums:
        for num2 in nums:
            if 2020 - num - num2 in set_nums:
                return num * num2 * (2020 - num - num2)

with open('input/day1') as _file:
    nums = [int(line.rstrip()) for line in _file]
    set_nums = set(nums)

print(part_one(nums, set_nums))
print(part_two(nums, set_nums))