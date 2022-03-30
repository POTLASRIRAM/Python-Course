f=open("Day14-30-03-2022\Donkey.txt","r")
text=f.read()
if "donkey" in text:
    text=text.replace("donkey","#####")
print(text)
f=open("Day14-30-03-2022\Donkey.txt","w")
f.write(text)