print('Write a raduis of sphere: ')
def volume(radius: int):
    v=(4/3)*3.14*pow(radius,3)
    return v

r = int(input())

print(volume(r))