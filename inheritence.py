class company():
    def __init__(self,name,location,branch):
            self.name = name
            self.location = location
            self.branch = branch
            print("constructor of company has been set")
            
    def companydetails(self):
        return f"\n company name is {self.name}\ncompany location is {self.location}\ncompany branch is {self.branch}"
    
class Employee(company):
    def __init__(self, name, age, salary, companyname, location, branch):
        super().__init__(companyname, location, branch)
        # self.name = name
        # self.location = location
        # self.branch = branch
        super().__init__(companyname, location, branch)
        self.age = age
        self.salary = salary
        self.company = companyname
       
        print("i have set the values",self)
        
    def employeedetails(self):
        return f"\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}\ncompany name is {self.company}"

        
        
emp1=Employee("Vishal", 20, 20000, "TCS", "Bangalore", "IT")
print(emp1.employeedetails())
        
    