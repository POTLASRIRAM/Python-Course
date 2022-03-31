class Car:
    def car_details(self,model,releaseyear,boughtby):
        self.m=model
        self.r=releaseyear
        self.b=boughtby
        print("Model = {}\nRelease Year = {}\nBought by = {}".format(self.m,self.r,self.b))

car1=Car()
car1.model="KIA"
car1.releaseyear=2015
car1.Boughtby="sr"
car1.car_details(car1.model,car1.releaseyear,car1.Boughtby)