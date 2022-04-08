class Student:
    def __init__(self):
        self.name=input("Enter student name : ")
        self.age=input("Enter student age : ")
        self.m1=int(input("Enter subject1 marks : "))
        self.m2=int(input("Enter subject2 marks : "))
    def total_marks(self):
        return self.m1+self.m2
s1=Student()
s2=Student()
print("Student 1 details")
print(s1.name,s1.age)
print(s1.total_marks())
print("Student 2 details")
print(s2.name,s2.age)
print(s2.total_marks())