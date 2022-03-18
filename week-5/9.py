import re
def a(b):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", b)

print(a(input()))