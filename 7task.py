class Student:
    quantity = 0
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Student.quantity += 1

    @classmethod
    def show_quantity(cls):
        return cls.quantity



student1 = Student("Anton", "Popov")
student2 = Student("Anna", "Sydorova")
student3 = Student("Viktor", "Somov")

print(Student.show_quantity())
