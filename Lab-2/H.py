import math
arr = list(map(int, input().split()))
col = []
def point(col):
    return math.sqrt(((col[0] - arr[0])**2) + ((col[1] - arr[1])**2))
n = int(input())
for i in range(n):
    inp = list(map(int, input().split()))
    col.append(inp)
col.sort(key=point)
for i in range(n):
    for j in range(2):
        print(col[i][j], end=" ")
    print()