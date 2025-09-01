class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)

student = Student("Bob", (90, 100, 100, 93, 90))
student2 = Student("Anne", (100, 100, 100, 93, 98))
print(student.name)
print(student.grades)
print(student.average())
print(student2.average())

class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades)/len(self.grades)

student = Student()
print(student.name)
print(student.grades)
print(Student.average(student))
print(student.average())