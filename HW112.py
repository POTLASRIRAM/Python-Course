class A:
    def __init__(self):
        self.a=10
        print(self.a)

class B:
    def __init__(self):
        self.b=20
        print(self.b)


class C(A,B):
    def __init__(self,c):
        self.c=c
        A.__init__(self)
        B.__init__(self)
        print(self.a,self.b,self.c)
c=C(30)
