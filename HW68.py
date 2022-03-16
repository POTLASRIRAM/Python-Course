#Values can be same for different keys but keys are not same and should be unique
languages={}
for i in range(0,4):
    print("Enter name")
    lk=input()
    print("Enter values")
    lv=input()
    languages[lk]=lv
print(languages)