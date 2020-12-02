with open('d') as f:
    n = [int(l.rstrip()) for l in f]

def s():
    for i, n1 in enumerate(n):
        for n2 in n[i:]:
            if (n1 + n2 == 2020):
                return n1 * n2

print(s())