class Age:
    def __init__(self,Age,Weight):
        self.age=Age
        self.weight=Weight
    def Compare_Ages(self,person2):
        if self.age == person2.age:
            return True
        else:
            return False

person1=Age(45,50)
person2=Age(45,67)
if person1.Compare_Ages(person2):
    print("Ages are equal")
else:
    print("Not Equal")