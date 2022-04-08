class Car:
    car_company="Ford"
    def __init__(self):
        self.mil=10
        self.tenure=20
car1=Car()
car1.car_company="Nissan"
car2=Car()
print("Car 1 \nMilage={} Tenure={} Company={}".format(car1.mil,car1.tenure,car1.car_company))
print("Car 2 \nMilage={} Tenure={} Company={}".format(car2.mil,car2.tenure,car2.car_company))