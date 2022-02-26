arr = []
while True:
    s = input()
    if s == "0":
        break
    else:
        d = s[0:2]
        m = s[3:5]
        y = s[6:]
        arr.append(y + " " + m + " " + d)
arr.sort()
for i in arr:
    y = i[0:4]
    m = i[4:8]
    d = i[8:10]
    print(d + m + y)