a=int(input())
for i in range(a+1):
    if i>0:
        if i%2==0:
            if i==a or i==a-1:
                print(i)
            else:
                print(i,end=",")