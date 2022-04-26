class Main:
    def main(self):
        a=10
        b=20
        return a,b
class Main1:
    def main1(self):
        c=30
        d=40
        return c,d
class Sub(Main,Main1):
    def total(self):
        l=Main.main(self)
        l1=Main1.main1(self)
        print(l)
        print(l1)
        s1=0
        s2=0
        for i in range(0,len(l)):
            s1=s1+l[i]
        for i in range(0,len(l1)):
            s2=s2+l1[i]
        print("Total = ",(s1+s2))
        
s=Sub()
s.total()