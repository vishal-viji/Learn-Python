

class Employee:
    company="TCS"
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("i have set the values",self)
        
    def employeedetails(self):
        return f"\n company is {self.company}\nEmployee Name: {self.name}\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}"
    
    @staticmethod
    def greet():
        print("Good morning")
        
    @classmethod
    def changecompany(self, cls):
        self.company = cls
        print("company name is changed to")
    
    
employee1=Employee("Vishal", 20, 20000)
employee2=Employee("suba", 23, 50000)
employee3=Employee("vicky", 40, 30000)
# print(employee1.employeedetails())
# employee1.greet()
employee1.changecompany("Infosys")

print(employee1.employeedetails())
print(employee2.employeedetails())
print(employee3.employeedetails())