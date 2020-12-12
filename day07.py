def part_one():
    return len(add_parents('shinygold', set()))

def add_parents(child_color, bags):
    for relation in relations:
        if relation[1] == child_color:
            bags.add(relation[0])
            add_parents(relation[0], bags)
    return bags

def part_two():
    return count_children('shinygold', 0, 1)

def count_children(parent_color, children, factor):
    for relation in relations:
        if relation[0] == parent_color:
            _factor = factor * relation[2]
            children = count_children(relation[1], children + _factor, _factor)
    return children

relations = []
with open('input/day07') as _file:
    for line in _file:
        words = line.split()
        parent_color = words[0] + words[1]
        for index, word in enumerate(words):
            if word.startswith('bag') and index > 2:
                child_color = words[index - 2] + words[index - 1]
                if child_color != 'noother':
                    relations.append((parent_color, child_color, int(words[index - 3])))

print(part_one())
print(part_two())
