import re

r = 0
for l in open('d'):
    a = re.split('-| |: ', l.rstrip())
    c = a[3].count(a[2])
    if c >= int(a[0]) and c <= int(a[1]):
        r += 1

print(r)