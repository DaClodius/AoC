import math

rules = []
your_ticket = []
nearby_tickets = []

def part_one():
    sum_of_invalid_fields = 0
    for ticket in nearby_tickets:
        for field in ticket:
            if not field_applies_to_any_rule(int(field)):
                sum_of_invalid_fields += int(field)
    return sum_of_invalid_fields

def part_two():
    field_order = {rule[0]: [] for rule in rules}
    valid_tickets = get_valid_tickets()
    product = 1

    for field in range(len(your_ticket)):
        for rule in rules:
            if all(field_applies_to_rule(int(ticket[field]), rule) for ticket in valid_tickets):
                field_order[rule[0]].append(field)

    field_order = dict(sorted(field_order.items(), key=lambda e: len(e[1])))

    for order_item in field_order.items():
        for sub_item in field_order.items():
            if sub_item != order_item and order_item[1][0] in sub_item[1]:
                sub_item[1].remove(order_item[1][0])

    for value in dict(filter(lambda e: e[0][:9] == 'departure', field_order.items())).values():
        product *= int(your_ticket[value[0]])
    return product

def get_valid_tickets():
    valid_tickets = [your_ticket]
    for ticket in nearby_tickets:
        if all(field_applies_to_any_rule(int(field)) for field in ticket):
            valid_tickets.append(ticket)
    return valid_tickets

def field_applies_to_any_rule(field):
    for rule in rules:
        if field_applies_to_rule(field, rule):
            return True
    return False

def field_applies_to_rule(field, rule):
    for range_ in rule[1].split(' or '):
        if int(range_.split('-')[0]) <= field <= int(range_.split('-')[1]):
            return True
    return False

with open('input/day16') as file:
    data_parts = file.read().split('\n\n')
    for line in data_parts[0].strip().split('\n'):
        rules.append((line[:line.index(':')], line[line.index(':') + 2:]))
    your_ticket = data_parts[1].strip().split('\n')[1].split(',')
    for line in data_parts[2].strip().split('\n')[1:]:
        nearby_tickets.append(line.split(','))

print(part_one())
print(part_two())
