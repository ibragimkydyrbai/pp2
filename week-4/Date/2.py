import datetime

x=datetime.datetime.now()
d =datetime.timedelta(days=-1)
e =datetime.timedelta(days=1)
y=x+d
a=x+e
print(y)
print(x)
print(a)