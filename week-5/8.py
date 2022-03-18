import re
a = input()
print(re.findall('[A-Z][^A-Z]*', a))