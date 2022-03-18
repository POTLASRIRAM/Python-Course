a=int(input("Enter number= "))
for i in range(a+1,1,-1):
    for j in range(1,i):
        print(j,end=" ")
    print()