class Twod:
    def __init__(self,n,m):
        self.i=n
        self.j=m
        print(f"{self.i}i+{self.j}j")

class Threed(Twod):
    def __init__(self,h):
        
        self.k=h
        
        print(f"{self.k}k")
two=Twod(10,20)
three=Threed(4)

