import re
def a(b):
        c = '^[a-z]+_[a-z]+$'
        if re.search(c,  b):
                return 'Found a match!'
        else:
                return('Not matched!')

print(a(input()))