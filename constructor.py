# class Person:
#     def __init__(self):
#         print("I am a Consrtuctor whenever an object is created i will come into action")
        
# p1=Person()
# p2=Person()
# p3=Person()


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print("i have set the values",self)
        
    def employeedetails(self):
        return f"\nEmployee Name: {self.name}\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}"
    
    
employee1=Employee("Vishal", 20, 20000)
employee2=Employee("Vis", 25, 30000)
employee3=Employee("suba", 23, 30000)
print(employee1.employeedetails())
print(employee2.employeedetails())
print(employee3.employeedetails())

    

