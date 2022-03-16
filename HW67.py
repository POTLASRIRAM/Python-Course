#Dictionary doesn't allows duplicate keys
languages={}
for i in range(0,4):
    print("Enter name")
    lk=input()
    print("Enter values")
    lv=input()
    languages[lk]=lv
print(languages)