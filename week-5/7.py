def a(b):
        import re
        return ''.join(x.capitalize() or '_' for x in b.split('_'))

print(a(input()))