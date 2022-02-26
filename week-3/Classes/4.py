class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'x={self.x}, y={self.y}')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, x1, y1):
        dx2 = pow(x1 - self.x, 2)
        dy2 = pow(y1 - self.y, 2)

        distance = pow((dx2 + dy2), 0.5)

        return distance


#
# point = Point()

point = Point(0, 0)

while True:
    choice = input("Press [1] to initialize point\n"
                   "Press [2] to view coordinates\n"
                   "Press [3] to move point\n"
                   "Press [4] to find distance\n"
                   "Press [0] to stop\n")
    if choice == "1":
        x = int(input("x="))
        y = int(input("y="))
        point = Point(x, y)
    elif choice == "2":
        point.show()
    elif choice == "3":
        dx = int(input("На сколько клеток нужно переместить точку вправо? Если влево, то введите отрицательное число.\n"))
        dy = int(input("На сколько клеток нужно переместить точку вверх? Если вниз, то введите отрицательное число.\n"))
        point.move(dx, dy)
    elif choice == "4":
        print("Введите координаты второй точки:")
        x1 = int(input("x="))
        y1 = int(input("y="))
        distance = point.dist(x1,y1)
        print(distance)
    elif choice == "0":
        break