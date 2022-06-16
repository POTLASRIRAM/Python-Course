class Programmer:
    def __init__(self,name,id,location):
        self.name= name
        self.id  = id
        self.location= location
    def employee_details(self):
        print("Name     = ",self.name)
        print("ID       = ",self.id)
        print("Location = ",self.location)

programmer=Programmer("Sr","12345678","Hyd")
programmer.employee_details()