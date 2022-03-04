def a(N):
    for i in range(N): 
        if i%3==0 and i%4==0 and i!=0:
            yield i
N=int(input())
for x in a(N):
    print(x, end=" ")