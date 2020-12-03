with open('d') as f:
    a = [l.rstrip() for l in f]

def s(dx, dy):
    t, x, y = 0, 0, 0
    while y < len(a):
        if(a[y][x] == '#'):
            t += 1
        x += dx
        if (x >= len(a[y])):
            x -= len(a[y])
        y += dy    
    return(t)

print(s(1, 1) * s(3, 1) * s(5, 1) * s(7, 1) * s(1, 2))
