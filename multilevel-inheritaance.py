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
        self.age = age
        self.salary = salary
        self.company = companyname
       
        print("i have set the values",self)
        
    def employeedetails(self):
        return f"\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}\ncompany name is {self.company}"
    
class manager(Employee): #sub child class
    def __init__(self, name, age, salary, companyname, location, branch, department,managername,deliverystream):
        super().__init__(name, age, salary, companyname, location, branch)
        self.department = department
        self.managername = managername
        self.deliverystream = deliverystream
        print("i have set the values")
    def managerdetails(self):
        return f"\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}\ncompany name is {self.company}\nDepartment: {self.department}\nManager Name: {self.managername}\nDelivery Stream: {self.deliverystream}"

    
obj1=manager("Vishal", 20, 20000, "TCS", "Bangalore", "IT", "IT", "Ramesh", "Delivery")
print(obj1.managerdetails())
print(obj1.companydetails())
print(obj1.employeedetails())
        