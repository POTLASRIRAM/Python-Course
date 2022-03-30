f=open("Day14-30-03-2022\Donkey.txt","r")
f1=open("Day14-30-03-2022\Donkeycopy.txt","r")
content=True
while content:
    content=f.readline()
    content1=f1.readline()
    if content!=content1:
        print("Missmatch")
        
    else:
        print("Exact match")