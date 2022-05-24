class A:
    def __init__(self):
        self.a=10
        self.b=20

class B(A):
    def __init__(self):
        A.__init__(self)
        self.Total=self.a+self.b
        print("Total at B = ",self.Total)
B=B()

class C(B):
    def __init__(self):
        B.__init__(self)
        self.Totalc=self.Total+30
        print("Total at C = ",self.Totalc)
c=C()