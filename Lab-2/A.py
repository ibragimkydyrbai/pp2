list = [int(i) for i in input().split()]
a = 0
b = len(list)-1
for i in range(len(list)):
    if i > a:
        print(0)
        break
    if list[i] + i > a:
        a = list[i]+i
    if a >= b:
        print(1)
        break