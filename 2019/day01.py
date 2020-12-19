def part_one(masses):
    return sum(int(mass / 3) - 2 for mass in masses)

def part_two(masses):
    total_fuel = 0
    for mass in masses:
        fuel = 0
        while mass >= 6:
            mass = int(mass / 3) - 2
            fuel += mass
        total_fuel += fuel
    return total_fuel

with open('2019/input/day01') as file:
    masses = [int(line.strip()) for line in file]

print(part_one(masses))
print(part_two(masses))
