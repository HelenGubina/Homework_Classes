class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return self.pi * self.radius ** 2

    def lenghth(self):
        return 2 * self.pi * self.radius

circle1 = Circle(3)
print(circle1.square())
print(circle1.lenghth())
