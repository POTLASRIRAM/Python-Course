class Train:
    def __init__(self,train_name,fare,number_of_seats):
        self.train_name=train_name
        self.fare=fare
        self.number_of_seats=number_of_seats
    def seats(self):
        self.a=self.number_of_seats
        print(f"Satavahana has {self.a} seats available for booking")
    def fares(self):
        print(f"Fair of each ticket is {self.fare}")
    def booking(self,booking):
        if(booking==True):
            print("Your booking is successful")
            print("Thank you for checking IRCTC")
            self.number_of_seats=self.number_of_seats-1
        else:
            print("Thank you for checking IRCTC!")

train=Train("Satavahana",70,350)
train.seats()
train.fares()
train.booking(2)
