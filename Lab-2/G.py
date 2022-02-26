n = int(input())
a = {}
b = {}
for i in range(n):
    c, d = input().split()
    if d in a:
        a[d] += 1
    else:
        a[d] = 1
m = int(input())
for i in range(m):
    e, x, g = input().split()
    if x in b:
        b[x] += int(g)
    else:
        b[x] = int(g)
s = 0
for spec in a:
    if not spec in b:
        s += a[spec]
    elif a[spec] - b[spec] >= 0 and spec in b:
        s += a[spec] - b[spec]
print('Demons left: ' + str(s))