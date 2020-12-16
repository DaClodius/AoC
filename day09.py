def part_one():
    index = 25
    while check_sum(nums[index], nums[index - 25: index]):
        index += 1
    return nums[index]


def check_sum(num, num_set):
    return len([n1 for n1 in num_set for n2 in num_set if n1 + n2 == num]) > 0


def part_two():
    target_sum = part_one()
    num_set = []
    pointer = 0
    while sum(num_set) != target_sum:
        index = 0
        num_set.clear()
        while sum(num_set) < target_sum:
            num_set.append(nums[pointer + index])
            index += 1
        pointer += 1
    return min(sorted(num_set)) + max(sorted(num_set))


with open('input/day09') as file:
    nums = [int(line.strip()) for line in file]

print(part_one())
print(part_two())
