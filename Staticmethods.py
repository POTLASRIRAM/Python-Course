class Car:
    car_company='KIA'
    def __init__(self):
        self.milage=30
        self.speed=140
    @staticmethod
    def c_company():
        return Car.car_company
car1=Car()
car2=Car()
print(car1.c_company(),car1.milage,car1.speed)