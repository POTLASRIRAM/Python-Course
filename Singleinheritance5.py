class Main:
    def __init__(self,a,b):
        self.fv=a
        self.sv=b
        print(self.fv,self.sv)
class Sub(Main):
    def sum(self):
        a=super().self.fv
        b=super().self.sv
        print(a,b)



m=Main(20,20)
s=Sub()
s.sum()
'''
s.sub(a,b)'''