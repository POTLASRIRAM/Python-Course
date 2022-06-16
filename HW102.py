class Calculator:

    def __init__(self,n1):
        self.n1=n1
    def calculations(self):
        square = self.n1*self.n1
        cube   = self.n1*(self.n1*self.n1)
        root   = (self.n1)*(1/2)
        print("Square = ",square)
        print("Cube   = ",cube)
        print("Root   = ",root)
cal=Calculator(25)
cal.calculations()