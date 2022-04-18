class Parent:
    def __init__(self,fname,age):
        self.fn=fname
        self.age=age
        print("Class = Parent")
        print(self.age,self.fn)
class Child(Parent):
    def __init__(self,fname,age):
        super().__init__(fname,age)
        self.lname="P"
        self.rollno=20
    def view(self):
        print("Class = Child")
        print(self.fn,self.age,self.lname,self.rollno)
c=Child("Sr",23)
c.view()