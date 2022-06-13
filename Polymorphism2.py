class A:
    def greet(self):
        print("Hi")
    def wish(self):
        print("Happy new year")
class B(A):
    def name(self):
        print("Hi sr")
class C(A):
    def roll(self):
        print("1")
a=A()
b=B()
c=C()
a.greet()
a.wish()
b.greet()
b.name()
c.wish()
c.roll()