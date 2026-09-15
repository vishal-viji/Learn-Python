class Employee:
    no_of_leaves=14
    def __init__(self,name,salary,role,phone):
        self.name=name
        self.salary=salary
        self.role=role
        self.phone=phone
        
    # def __str__(self):
    #     return f"Employee name is {self.name}\n Employee salary is {self.salary}\n Employee role is {self.role}\n Employee phoneNumber is {self.phone} \n this is str"
 
    # def __repr__(self):
    #     return f"{self.name} {self.salary}"
    
    def __add__(emp1,emp2):
        return emp1.salary+emp2.salary
    
    def __mul__(emp1,emp2):
        return emp1.salary*emp2.salary
    
    def __truediv__(emp1,emp2):
        return emp1.salary/emp2.salary
    
    def __floordiv__(emp1,emp2):
        return emp1.salary//emp2.salary

 
obj1=Employee("vishal",150000,"FSD",755233257)
obj2=Employee("shajii",150000,"FSD",755233257)
print(obj1)
print(obj1+obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1//obj2)
