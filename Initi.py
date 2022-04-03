class Calculator:
    def __init__(self,fv : int, sv : int):
        self.fv= int(fv)
        self.sv= int(sv)
        '''Sum=self.fv+self.sv
        print("Sum = ",Sum)'''
    def sum(self):
        sum=self.fv+self.sv
        print("Sum = ",sum)

f=Calculator("1","5")
s=Calculator("5","8")
t=Calculator("9","3")
f.sum()
s.sum()
t.sum()
