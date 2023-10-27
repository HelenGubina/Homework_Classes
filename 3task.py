class Vehicle:
    def __init__(self, typev, speed, price):
        self.typev = typev
        self.speed = speed
        self.price = price

    def __gt__(self, other):
        if isinstance(other, Vehicle):
            return self.speed > other.speed

    def __str__(self):
        return self.typev + " | " + str(self.speed) + " | " + str(self.price)


bus = Vehicle("bus", 130, 60000)
plane = Vehicle("plane", 340, 12000000)
train = Vehicle("train", 150, 5000000)
listv = [train, bus, plane]
listv.sort()
for i in listv:
    print(i)
