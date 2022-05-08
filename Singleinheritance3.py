class Main:
    def __init__(self):
        self.n1=20
        self.n2=30
    def Sum(self):
        Total=self.n1+self.n2
        print("Total = ",Total)
class Sub(Main):
    def __init__(self):
        Main.__init__(self)
        print(self.n1)
        print(self.n2)
s=Sub()
s.Sum()
