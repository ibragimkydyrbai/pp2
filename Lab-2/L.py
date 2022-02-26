s = input()
first = ['(', '[', '{']
second = [')', ']', '}']
arr = []
ok = 1
for i in s:
    if i in first:
        arr.append(i)
    else:
        index = second.index(i)
        if len(arr) != 0 and first[index] == arr[len(arr) - 1]:
            arr.pop()
        else:
            ok = 0
            break
print("Yes") if ok == 1 and len(arr) < 1 else print("No")