s = input()
i = 0
word_to_num = {'ONE':1, 'TWO':2,'THR':3,'FOU':4, 'FIV':5,'SIX':6,'SEV':7, 'EIG':8,'NIN':9,'ZER':0}
num_to_word = {'1':'ONE', '2':'TWO','3':'THR','4':'FOU', '5':'FIV','6':'SIX','7':'SEV', '8':'EIG','9':'NIN','0':'ZER'}
num1 = []
plus = s.index('+')
def to_int(word):
    num = 0
    for i in word:
        num *= 10
        num += word_to_num[i]
    return num
def to_string(num):
    num = str(num)
    s = ''
    for i in str(num):
        s += num_to_word[i]
    return s
while i != plus:
    num1.append(s[i:i+3])
    i += 3
cur = plus + 1
num2 = []
while cur != len(s):
    num2.append(s[cur:cur+3])
    cur += 3
print(to_string(to_int(num1) + to_int(num2)))