def a(N):
    for i in range(N,0,-1): 
        yield i
N=int(input())
for x in a(N):
    print(x, end=" ")