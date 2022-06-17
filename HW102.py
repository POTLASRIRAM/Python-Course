class Calculator:

    def __init__(sri,n1):
        sri.n1=n1
    def calculations(sri):
        square = sri.n1*sri.n1
        cube   = sri.n1*(sri.n1*sri.n1)
        root   = (sri.n1)*(1/2)
        print("Square = ",square)
        print("Cube   = ",cube)
        print("Root   = ",root)
cal=Calculator(25)
cal.calculations()