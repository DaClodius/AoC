def run(laps):
    new = None
    pre = nums[-1]
    idx = {v: i for i, v in enumerate(nums)}
    for lap in range(len(nums), laps):
        new = lap - idx[pre] - 1 if pre in idx.keys() and idx[pre] < lap - 1 else 0
        idx[pre] = lap - 1
        pre = new
    return new


with open('input/day15') as file:
    nums = [int(n) for n in file.readline().strip().split(',')]

print(run(2020))  # part_one
print(run(30000000))  # part_two
