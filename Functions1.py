def sum(a,b):
    c=a+b
    d=a-b
    e=a/b
    f=a*b
    g=a%b
    return c,d,e,f,g
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c,d,e,f,g=sum(a,b)
print("c : ",c,"d : ",d,"e : ",e,"f : ",f,"g : ",g)