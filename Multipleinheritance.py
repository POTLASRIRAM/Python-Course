class Main:
    def __init__(self):
        self.a=10
        self.b=20
class Main1:
    def __init__(self):
        self.c=30
        self.d=40
class Sub(Main,Main1):
    def __init__(self):
        Main.__init__(self)
        Main1.__init__(self)
        Total=self.a+self.b+self.c+self.d
        print("Total = ",Total)
s=Sub()
