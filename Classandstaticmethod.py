class A:
    name='s'
    age=21
    @classmethod
    def details(cls):
        print(cls.age)
        print(cls.name)
a=A()
a.details()