import re

r = 0
for l in open('d'):
    a = re.split('-| |: ', l.rstrip())
    if (a[3][int(a[0])-1] == a[2]) ^ (a[3][int(a[1])-1] == a[2]):
        r += 1

print(r)