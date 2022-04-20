class Main:
    def __init__(self):
        self.a=10
        self.b=20
class Sub(Main):
    def __init__(self):
        Main.__init__(self)
    def sum(self):
        total=self.a+self.b
        print("Total = ",total)
s=Sub()
s.sum()
class Sub2(Main):
    def __init__(self):
        Main.__init__(self)
    def sub(self):
        total=abs(self.a-self.b)
        print("Total = ",total)
s1=Sub2()
s1.sub()
