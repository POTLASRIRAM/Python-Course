class A:
    name='s'
    def age(self):
        self.age=20
        print(self.age)
    @staticmethod
    def roll():
        rollno=82
        print(A.name)
        print(rollno)
    @classmethod
    def details(cls):
        
        cls.age(cls)
        cls.roll()
        return cls.age
a=A()
a.details()
print(a.age)
print(a.roll)
