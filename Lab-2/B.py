num = int(input())
list = [int(i) for i in input().split()]
mult = []
for i in range(len(list) - 1):
    for j in range(i + 1, len(list)):
        mult.append(list[i] * list[j])
print(max(mult))