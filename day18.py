def solve(calc, pre):
    while calc.find(' ') > 0:
        if calc.find('(') >= 0:
            inner = get_inner_calc(calc)
            calc = calc.replace('(' + inner + ')', solve(inner, pre), 1)
        term = []
        for item in calc.split(' '):
            term.append(item.strip('()'))
            if len(term) == 3:
                if pre and term[1] != '+' and calc.find('+') > 0:
                    term = [term[2]]
                else:
                    calc = calc.replace(' '.join(term), str(operate(term)), 1)
    return calc

def get_inner_calc(calc):
    start_index = 0
    open_braces = 0
    for index, char in enumerate(calc):
        if char == '(':
            if open_braces == 0:
                start_index = index
            open_braces += 1
        elif char == ')':
            open_braces -= 1
            if open_braces == 0:
                return calc[start_index + 1: index]

def operate(term):
    if term[1] == '+':
        return int(term[0]) + int(term[2])
    elif term[1] == '*':
        return int(term[0]) * int(term[2])

with open('input/day18') as file:
    parts = [0, 0]
    for calc in [line.strip() for line in file]:
        parts[0] += int(solve(calc, False))
        parts[1] += int(solve(calc, True))
    print(parts[0])
    print(parts[1])
    