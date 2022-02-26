n = int(input())
num = upp = low = j = cur = 0   
arr = []
col = []
for i in range(n):
    s = input()
    for i in range(len(s)):
        if ord(s[i]) > 47 and ord(s[i]) < 58:
            num += 1
        if ord(s[i]) > 64 and ord(s[i]) < 91:
            upp += 1
        if ord(s[i]) > 96 and ord(s[i]) < 123:
            low += 1
    if num > 0 and low > 0 and upp > 0:
        arr.insert(j,s)
        j += 1
        cur += 1
    num = upp = low = 0
arr = sorted(list(set(arr)))
print(len(arr))
for i in arr:
    print(i)