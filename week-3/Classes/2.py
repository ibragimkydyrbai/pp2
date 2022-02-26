class Shape:

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return pow(self.length, 2)


shape = Shape()
print(f'Area of shape is {shape.area()}')

length_of_square = int(input("Insert length of square:\n"))
square = Square(length_of_square)
print(f'Area={square.area()}')