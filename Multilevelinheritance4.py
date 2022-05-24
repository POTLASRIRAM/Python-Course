class A:
    def __init__(self,f_name):
        self.f_name=f_name
        #print("F_name ",self.f_name)
class B(A):
    def __init__(self,m_name,f_name):
        self.m_name=m_name
        #print("M ",self.m_name)
        A.__init__(self,f_name)
class C(B):
    def __init__(self,l_name,m_name,f_name):
        self.l_name=l_name
        #print("L = ",self.l_name)
        B.__init__(self,m_name,f_name)
    def names(self):
        print(self.f_name)
        print(self.m_name)
        print(self.l_name)
c=C("S","T","P")
c.names()