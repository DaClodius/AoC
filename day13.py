def part_one(bus_ids):
    bus_ids = [int(bus_id) for bus_id in bus_ids if bus_id != 'x']
    diff_map = [(bus_id, bus_id - timestamp % bus_id) for bus_id in bus_ids]
    min_diff = min(diff_map, key = lambda t: t[0])
    return min_diff[0] * min_diff[1]

def part_two(bus_ids): #chinese remainder theorem
    bus_ids = [int(bus_id) if bus_id != 'x' else 'x' for bus_id in bus_ids]
    id_mods = {bus_id: -index % bus_id for index, bus_id in enumerate(bus_ids) if bus_id != 'x'}
    reversed_id_mods = list(reversed(sorted(id_mods)))
    value = id_mods[reversed_id_mods[0]]
    mi = reversed_id_mods[0]
    for ni in reversed_id_mods[1:]:
        while value % ni != id_mods[ni]:
            value += mi
        mi *= ni
    return value

with open('input/day13') as file:
    timestamp = int(file.readline().strip())
    bus_ids = file.readline().strip().split(',')

print(part_one(bus_ids))
print(part_two(bus_ids))
