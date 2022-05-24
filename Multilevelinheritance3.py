class A:
    a=10
    b=20
class B(A):

    def sum(self):
        B.Tot=A.a+A.b
        print("Total = ",B.Tot)
   
    
class C(B):
    def sub(self):
        Sub= B.Tot-20
        print("Sub = ",Sub) 
c=C()
c.sum()
c.sub()