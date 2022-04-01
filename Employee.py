class Employee:
    def Emp_details(self,name,startyear,endyear):
        self.n=name
        self.s=startyear
        self.e=endyear
        print("Name = {}\nStart Year = {}\nEnd Year = {}".format(self.n,self.s,self.e))

emp1=Employee()
emp1.name="KIA"
emp1.startyear=2015
emp1.endyear="sr"
emp1.Emp_details(emp1.name,emp1.startyear,emp1.endyear)