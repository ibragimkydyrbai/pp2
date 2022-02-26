alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
arr = list(map(str, input().split()))
col = []
for i in arr:
    word = ''
    for j in i:
        if j in alphabet:
            word += j
    if col.count(word) == 0:
       col.append(word)
print(len(col))
col = sorted(col)
#print('\n'.join([i for i in sorted(col)]))
print('\n'.join([str(col[i]) for i in range(len(col))]))
