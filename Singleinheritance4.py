class Main:
    def __init__(self):
        self.n1=20
        self.n2=30
class Sub(Main):
    def __init__(self):
        Main.__init__(self)
        Total=self.n1+self.n2
        print("Total = ",Total)
s=Sub()

