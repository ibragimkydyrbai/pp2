import re
def a(b):
        c = 'ab?'
        if re.search(c,  b):
                return 'Found a match!'
        else:
                return('Not matched!')

print(a(input()))
