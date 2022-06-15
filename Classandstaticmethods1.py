class A:
    name='s'
    age=21
    def details(self):
        self.name=A.name
        self.age=A.age
        A.age=24
        print(self.name)
        print(self.age)
a=A()
a.details()
print(A.age)