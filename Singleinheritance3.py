class Main:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a)
class Sub(Main):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def sum(self):
        total=self.a+self.b+self.c
        return total
s=Sub(10,20,30)
print(s.sum())
