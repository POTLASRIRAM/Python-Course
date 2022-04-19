class Parent:
    def __init__(self):
        self.a=10
        self.b=20
    def sum(self):
        total=self.a+self.b
        print("Sum = ",total)
    def sub(self):
        Sub=self.a+self.b
        print("Sub = ",Sub)
    def mul(self):
        mul=self.a*self.b
        print("Mul = ",mul)
p=Parent()
p.sum()
p.sub()
p.mul()

