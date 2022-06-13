class A:
    def sum(self,a,b):
        self.a=a
        self.b=b
        print("Sum = ",self.a+self.b)
class B(A):
    def sum(self,a,b):
        super().sum(a,b)
a=A()
a.sum(10,20)
b=B()
b.sum(50,50)