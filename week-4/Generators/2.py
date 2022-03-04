def a(N):
    for i in range(N): 
        if i%2==0 and i!=0:
            yield i
N=int(input())
for x in a(N+1):
    if x==N or x==N-1:
        print(x)
    else:
        print(x, end=",")