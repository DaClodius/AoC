from copy import copy

def part_one(decks):
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        deal_cards(decks, 0 if decks[0][0] > decks[1][0] else 1)
    return get_result(decks, 0 if len(decks[0]) > len(decks[1]) else 1)

def part_two(decks):
    return get_result(decks, part_two_game(decks))

def part_two_game(decks):
    history = []
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        if check_history(decks, history):
            return 0
        history.append(copy(decks))
        winner = 0 if decks[0][0] > decks[1][0] else 1
        if len(decks[0])-1 >= decks[0][0] and len(decks[1])-1 >= decks[1][0]:
            winner = part_two_game([decks[0][1:decks[0][0]+1], decks[1][1:decks[1][0]+1]])
        deal_cards(decks, winner)
    return winner

def check_history(decks, history):
    for state in history:
        for index in range(len(decks)):
            if decks[index] == state[index]:
                return True
    return False

def deal_cards(decks, winner):
    w = (0, 1) if winner == 0 else (1, 0)
    decks[w[0]] = decks[w[0]][1:] + [decks[w[0]][0]] + [decks[w[1]][0]]
    decks[w[1]] = decks[w[1]][1:]

def get_result(decks, winner):
    score = 0
    for index, value in enumerate(reversed(decks[winner])):
        score += (index + 1) * value
    return score

def get_decks():
    decks = []
    with open('2020/input/day22') as file:
        for deck in file.read().strip().split('\n\n'):
            decks.append([int(n) for n in deck.split('\n')[1:]])
    return decks

print(part_one(get_decks()))
print(part_two(get_decks()))
