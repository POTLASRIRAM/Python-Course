no=int(input("Enter a number : "))
for i in range(1,no+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()