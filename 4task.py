class Student:
    def __init__(self, name, surname, gradelist):
        self.name = name
        self.surname = surname
        self.gradelist = gradelist

    def __len__(self):
        return len(self.gradelist)

    def __gt__(self, other):
        if isinstance(other, Student):
            return len(self.gradelist) > len(other.gradelist)

    def __str__(self):
        return f"{self.name} {self.surname} has {len(self.gradelist)} grades "

student1 = Student("Anton", "Popov", [3, 4, 5, 3, 4, 4])
student2 = Student("Anna", "Sydorova", [2, 5, 4, 4, 4, 3, 4, 4])
student3 = Student("Viktor", "Somov", [5, 5, 5])

listSt = [student1, student2, student3]

listSt.sort()
for i in listSt:
    print(i)
