with open('d') as f:
    a = [l.rstrip() for l in f]

t, x = 0, 0
for y, l in enumerate(a):
    if(l[x] == '#'):
        t += 1
    x += 3
    if (x >= len(l)):
        x -= len(l)

print(t)
