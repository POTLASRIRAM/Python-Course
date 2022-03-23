import random
print("Welcome to Snake-Water-Gun!")
no=int(input("Enter number of rounds : "))
Computer=0
User=0
lst=["snake","water","gun"]
for i in range(0,no):
    value=input("Enter snake or water or gun : ")
    picker=random.choice(lst)
    if(value=="snake" and picker=="snake"):
        print("Picker=",picker)
        print("Match draw")
        continue
    elif(value=="snake" and picker=="water"):
        print("Picker=",picker)
        User=User+1
        print("User got one point")
    elif(value=="snake" and picker=="gun"):
        print("Picker=",picker)
        Computer=Computer+1
        print("Computer got one point")
    elif(value=="gun" and picker=="gun"):
        print("Picker=",picker)
        print("Match draw")
        continue
    elif(value=="gun" and picker=="water"):
        print("Picker=",picker)
        Computer=Computer+1
        print("Computer got one point")
    elif(value=="gun" and picker=="snake"):
        print("Picker=",picker)
        User=User+1
        print("User got one point")
    if(value=="water" and picker=="water"):
        print("Picker=",picker)
        print("Match draw")
        continue
    elif(value=="water" and picker=="snake"):
        print("Picker=",picker)
        Computer=Computer+1
        print("Computer got one point")
    elif(value=="water" and picker=="gun"):
        print("Picker=",picker)
        User=User+1
        print("User got one point")
print(User,Computer)
if(User>Computer):
    print("User won's the battle")
elif(User<Computer):
    print("Computer won the battle")
elif(User==Computer):
    print("Match Draw")