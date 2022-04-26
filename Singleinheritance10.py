class Main:
    def __init__(self):
        self.a=10
        self.b=20
    def sub(self):
        total=self.a-self.b
        return total

class Sub(Main):
    def __init__(self):
        Main.__init__(self)
    def sum(self):
        total=self.a+self.b
        print(total)
        print(Main.sub(self))
s=Sub()
s.sum()