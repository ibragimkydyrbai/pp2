def Z(a,b):
    for i in range(a,b): 
        yield i**2
a=int(input())
b=int(input())
for x in Z(a,b):
    print(x, end=" ")