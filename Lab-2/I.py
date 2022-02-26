n = int(input())
col = []
ind = 0
for i in range(n):
    arr = list(map(str, input().split()))
    if arr[0] == '1':
        col.append(arr[1])
    else:
        ind += 1
for i in range(ind):
    print(col[i], end = ' ')