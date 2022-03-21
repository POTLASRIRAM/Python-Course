def greatest(a,b,c):
    if(a>b and a>c):
        print("A is greatest")
    elif(b>a and b>c):
        print("B is greatest")
    else:
        print("C is greatest")
a=int(input("Enter A value : "))
b=int(input("Enter B value : "))
c=int(input("Enter C value : "))
greatest(a,b,c)