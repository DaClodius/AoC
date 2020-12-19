import re

def solve(*replace_rules):
  if replace_rules:
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
  regex = re.compile(build_regex('0', 0))
  return sum([1 for message in messages if regex.fullmatch(message)])

def build_regex(node, depth):
  if depth > 20: return ''
  regex = '('
  for char in rules[node].split():
    if char == '|':
      regex += char
    elif char.isdigit():
      regex += build_regex(char, depth + 1)
    else:
      return char[1]  
  return regex + ')'

with open('2020/input/day19') as file:
    puzzle = file.read().split('\n\n')
    rules = dict([line.split(': ') for line in puzzle[0].split('\n')])
    messages = puzzle[1].split('\n')

print(solve())
print(solve(True))
