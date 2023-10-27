class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.side1 * 2 + self.side2 * 2

    def squuare(self):
        return self.side1*self.side2


rect1 = Rectangle(3, 5)
print(rect1.squuare())
print(rect1.perimeter())
