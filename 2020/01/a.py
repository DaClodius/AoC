with open('d') as f:
    n = [int(l.rstrip()) for l in f]

s = set()
for i in n:
    s.add(i)
    if (2020 - i in s):
        print(i * (2020 - i))