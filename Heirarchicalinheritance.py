class A:
    a=10
    b=30
class B(A):
    Sum=A.a+A.b
    print("Sum = ",Sum)
class C(A):
    Sub=A.b-A.a
    print("Sub = ",Sub)