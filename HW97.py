def lstr(lst,value):
    a=lst
    print(a)
    print("into function")
    for i in range(0,len(a)):
        print("into loop")
        if(a[i]==value):
            a.remove(a[i])
            print("Removed")
    print(a)
lst=[]
for i in range(0,6):
    lst.append(input("Enter list value : "))
value=input("Enter value to remove : ")
lstr(lst,value)
