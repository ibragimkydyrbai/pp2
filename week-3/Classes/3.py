from prob2 import Square

class Rectange(Square):

    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        return self.length * self.width


a, b = list(map(int, input("insert length and width separated by space\n:").split()))
rectange = Rectange(a,b)