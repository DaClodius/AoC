from typing import List, Tuple

Ticket = List[int]
Range = Tuple[int, int]


class Rule:
    name: str
    ranges: List[Range]

    def __init__(self: any, name: str, ranges: List[Range]):
        self.name = name
        self.ranges = ranges


def parse_rule(s: str) -> Rule:
    name, ranges_ = s.split(": ")
    r1, r2 = ranges_.split(" or ")
    ranges = [parse_range(r1), parse_range(r2)]
    return Rule(
        name=name,
        ranges=ranges
    )


def parse_range(s: str) -> Range:
    min_, max_ = s.split("-")
    return int(min_), int(max_)


rules: List[Rule] = []
your_ticket: Ticket = []
nearby_tickets: List[Ticket] = []


def part_one() -> int:
    sum_of_invalid_fields = 0
    for ticket in nearby_tickets:
        for field in ticket:
            if not field_applies_to_any_rule(field):
                sum_of_invalid_fields += field
    return sum_of_invalid_fields


def part_two() -> int:
    field_order = {rule.name: [] for rule in rules}
    valid_tickets = get_valid_tickets()
    product = 1

    for field in range(len(your_ticket)):
        for rule in rules:
            if all(field_applies_to_rule(ticket[field], rule) for ticket in valid_tickets):
                field_order[rule.name].append(field)

    field_order = dict(sorted(field_order.items(), key=lambda e: len(e[1])))

    for order_item in field_order.items():
        for sub_item in field_order.items():
            if sub_item != order_item and order_item[1][0] in sub_item[1]:
                sub_item[1].remove(order_item[1][0])

    for value in dict(filter(lambda e: e[0][:9] == 'departure', field_order.items())).values():
        product *= your_ticket[value[0]]
    return product


def get_valid_tickets() -> List[Ticket]:
    valid_tickets = [your_ticket]
    for ticket in nearby_tickets:
        if all(field_applies_to_any_rule(field) for field in ticket):
            valid_tickets.append(ticket)
    return valid_tickets


def field_applies_to_any_rule(field: int) -> bool:
    for rule in rules:
        if field_applies_to_rule(field, rule):
            return True
    return False


def field_applies_to_rule(field: int, rule: Rule) -> bool:
    for range_ in rule.ranges:
        if range_[0] <= field <= range_[1]:
            return True
    return False


with open('input/day16') as file:
    data_parts = file.read().split('\n\n')
    for line in data_parts[0].split('\n'):
        rules.append(parse_rule(line))
    for line in data_parts[2].strip().split('\n')[1:]:
        nearby_tickets.append([int(n) for n in line.split(',')])
    your_ticket = [int(n) for n in data_parts[1].split('\n')[1].split(',')]

print(part_one())
print(part_two())
