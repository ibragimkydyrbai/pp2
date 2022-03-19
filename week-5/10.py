from re import sub
def a(b):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    b.replace('-', ' '))).split()).lower()

print(a(input()))