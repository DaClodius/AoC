with open('d') as f:
    n = [int(l.rstrip()) for l in f]

def s():
    for i, n1 in enumerate(n):
        for j, n2 in enumerate(n[i:]):
            for n3 in n[j:]:
                if (n1 + n2 + n3 == 2020):
                    return n1 * n2 * n3

print(s())