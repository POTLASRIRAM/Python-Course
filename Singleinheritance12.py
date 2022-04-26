class Main:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def gotoprint(self):
        return self.a,self.b
class Sub(Main):
    def __init__(self,a,b):
        Main.__init__(self,a,b)
    def inherit(self):
        print("SUB")
        l=Main.gotoprint(self)
        print(l)
        sum=0
        for i in range(0,len(l)):
            sum=sum+l[i]
        print("SUB = ",sum)
        print(l[1])
        
s=Sub(10,20)
s.inherit()