n = 1
arr = []
while n != 0:
    n = int(input())
    arr.append(n)
arr.pop()
k = len(arr)
i = 0
if len(arr) % 2 == 0:
    while i != k/2:
        print(arr[i] + arr[k-i - 1],end = " ")
        i += 1
elif k % 2 == 1:
    middle = int(int(len(arr) - 1) / 2)
    while i != (k - 1) / 2:
        print(arr[i] + arr[k-i-1],end = " ")
        i += 1
    print(arr[middle],end=" ")