class Student:
    st_name="Sr"
    st_rollno=20
s1=Student()
class SSC(Student):
    def __init__(self):
        self.m1=98
        self.m2=90
        self.m3=85
st1=SSC()
print("SSC = ",st1.st_name,st1.st_rollno,st1.m1,st1.m2,st1.m3)
class Inter(Student):
    def __init__(self):
        self.m1=67
        self.m2=68
        self.m3=69
st1=Inter()
print("INTER = ",st1.st_name,st1.st_rollno,st1.m1,st1.m2,st1.m3)
