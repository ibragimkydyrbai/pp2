n = int(input())
a = {}
for i in range(n):
    b, c = input().split()
    if not(b in a):
        a[b] = 0
    if b in a:
        a[b] += int(c)
mx = max(j for j in a.values())
for s in sorted(a.keys()):
    if a[s] != mx:
        print(s + ' has to receive ' + str(mx - a[s]) + ' tenge ')
    else:
        print(s + ' is lucky!')