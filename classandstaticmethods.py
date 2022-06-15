class A:
    name='s'
    age=21
    @staticmethod
    def details():
        print(A.age)
        print(A.name)
a=A()
a.details()