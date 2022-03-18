from re import x
def a(b):
  return '_'.join(
    x('([A-Z][a-z]+)', r' \1',
    x('([A-Z]+)', r' \1',
    b.replace('-', ' '))).split()).lower()

print(a(input()))