class Student:
    def stu_details(self):
       print("SR SCHOOL")
class SSC(Student):
    def __init__(self):
        self.m1=98
        self.m2=90
        self.m3=85
s=Student()
s.stu_details()
st1=SSC()
print("SSC = ",st1.m1,st1.m2,st1.m3)
class Inter(Student):
    def __init__(self):
        self.m1=67
        self.m2=68
        self.m3=69
st1=Inter()
s1=Student()
s1.stu_details()
print("INTER = ",st1.m1,st1.m2,st1.m3)
