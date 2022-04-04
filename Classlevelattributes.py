class Employee:
    office_address="Hyderabad"
    def __init__(self,name,age : int):
        self.name=name
        self.age=age
        #print(self.name,self.age,Employee.office_address)
    def employee_details(self):
        print("Employee name Age Address")
        print(self.name,self.age,Employee.office_address)
        
        
emp1=Employee("SP",22)
emp2=Employee("PS",23)
emp1.employee_details()
emp2.employee_details()