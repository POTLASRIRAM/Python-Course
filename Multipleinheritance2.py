class P1:
    def p1(self):
        print("Hi this is p1")
class P2:
    def p2(self):
        print("Hi thus is p2")
class P3(P1,P2):
    pass
p=P3()
p.p1()
p.p2()
