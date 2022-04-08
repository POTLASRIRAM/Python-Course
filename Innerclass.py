class Student:
    school_name="SR"
    def __init__(self):
        self.name="Sriram"
        self.rollno=17
        self.ssc=self.SSC()
        self.inter=self.Intermediate()
    class SSC:
        def __init__(self):
            self.m1=int(input("Enter sub1 = "))
            self.m2=int(input("Enter sub2 = "))
        def ssc_sum(self):
            return self.m1+self.m2
        
    class Intermediate:
        def __init__(self):
            self.m1=int(input("Enter sub1 = "))
            self.m2=int(input("Enter sub2 = "))
        def inter_sum(self):
            return self.m1+self.m2


s1=Student()
print(s1.school_name,s1.name,s1.rollno)
print("----------SSC---------")
print(s1.ssc.m1,s1.ssc.m2)
print(s1.ssc.ssc_sum())
print("---------INTER-------")
print(s1.inter.m1,s1.inter.m2)
print(s1.inter.inter_sum())
