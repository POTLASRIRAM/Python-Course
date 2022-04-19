class Up:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Down(Up):
    def sum(self):
        total=self.a+self.b
        print("TOTAL = ",total)
d=Down(10,20)
d.sum()
class Downn(Up):
    def sub(self):
        sub=self.a-self.b
        print("Sub = ",sub)
m=Downn()
m.sub()