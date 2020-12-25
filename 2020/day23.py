class Cup:
    previous: int
    next_: int

    def __init__(self, previous, next_):
        self.previous = previous
        self.next_ = next_

def part_one(cups):
    run_game(cups, next(iter(cups)), 100)
    print_chain(cups)

def print_chain(cups):
    chain = []
    next_cup = 1
    for _ in range(len(cups)):
        chain.append(next_cup)
        next_cup = cups[next_cup].next_
    print(''.join(str(label) for label in chain[1:]))

def part_two(cups):
    cups = one_million_cups(cups)
    run_game(cups, next(iter(cups)), 10**7)
    print(cups[1].next_ * cups[cups[1].next_].next_)

def run_game(cups, current, moves):
    min_max = (min(cups.keys()), max(cups.keys()))
    for _ in range(moves):
        # pick three cups and close chain
        three_cups = pick_three_cups(cups, current)
        cups[current].next_ = cups[three_cups[2]].next_
        cups[three_cups[2]].previous = current        
        # get destination
        destination = get_destination(cups, current, min_max)
        while destination in three_cups:
            destination = get_destination(cups, destination, min_max)
        # insert three_cups after destination
        post_destination = cups[destination].next_
        cups[destination].next_ = three_cups[0]
        cups[three_cups[0]].previous = destination
        cups[post_destination].previous = three_cups[2]
        cups[three_cups[2]].next_ = post_destination
        # choose next cup
        current = cups[current].next_

def pick_three_cups(cups, current):
    return [
        cups[current].next_,
        cups[cups[current].next_].next_,
        cups[cups[cups[current].next_].next_].next_
        ]

def get_destination(cups, current, min_max):
    destination = current - 1
    if destination < min_max[0]:
        destination = min_max[1]
    return destination

def build_cup_chain():
    cups = {}
    cups_ = get_cups()
    for index, label in enumerate(cups_):
        next_ = index + 1
        if next_ >= len(cups_):
            next_ = 0
        previous = index - 1
        if previous < 0:
            previous = len(cups_) - 1
        cups[label] = Cup(cups_[previous], cups_[next_])
    return cups

def one_million_cups(cups):
    first_cup = next(iter(cups))
    last_cup = cups[first_cup].previous
    # fix chain
    cups[first_cup].previous = 10**6
    cups[last_cup].next_ = max(cups.keys()) + 1
    # add cups...
    for i in range(cups[last_cup].next_, 10**6 + 1):
        cups[i] = Cup(i - 1, i + 1)
    # close chain
    cups[cups[last_cup].next_].previous = last_cup
    cups[10**6].next_ = first_cup
    return cups

def get_cups():
    return [int(n) for n in open('2020/input/day23').read().strip()]

part_one(build_cup_chain())
part_two(build_cup_chain())
