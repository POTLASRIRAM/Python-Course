class Main:
    def gotoprint(self):
        a=10
        b=30
        return a,b
class Sub(Main):
    def inherit(self):
        print("SUB")
        l=Main.gotoprint(self)
        print(l)
        sum=0
        for i in range(0,len(l)):
            sum=sum+l[i]
        print("SUB = ",sum)
        print(l[1])
        
s=Sub()
s.inherit()