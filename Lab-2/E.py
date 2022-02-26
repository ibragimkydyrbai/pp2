import sys

arr = list(map(int, sys.stdin.read().split()))
sum = 0
n = arr[0]
x = arr[1]
for i in range(n):
    sum = sum ^ (x)
    x += 2
print(sum)