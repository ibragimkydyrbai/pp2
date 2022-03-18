import re
def a(b):
        c = 'ab{2,3}'
        if re.search(c,  b):
                return 'Found a match!'
        else:
                return('Not matched!')
print(a(input()))

