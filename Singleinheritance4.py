class Main:
    fv=10
    sc=20
class Sub(Main):
    def sum(self,a,b):
        total=a+b
        print("Total = ",total)
    def sub(self,a,b):
        sub=abs(a-b)
        print("SUB = ",sub)
a=Main.fv
b=Main.sc
s=Sub()
s.sum(a,b)
s.sub(a,b)