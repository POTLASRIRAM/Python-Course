marks=[]
count=0
for i in range(0,3):
    marks.append(int(input("Enter marks")))
    if(marks[i]>=33):
        count+=1
if(count==3):
    print("Pass")
else:
    print("Fail")