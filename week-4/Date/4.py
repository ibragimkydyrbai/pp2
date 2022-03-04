import datetime as dt

a = dt.datetime(2021,1,1,00,00,00)
b = dt.datetime(2022,1,1,00,00,00)
print(int((b-a).total_seconds()))