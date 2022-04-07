no=int(input("Enter a number = "))
sum=0
while no:
    i=no%10
    sum=sum+i
    no=no//10
    
print("Sum =",sum)