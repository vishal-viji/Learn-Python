class Human():
    def __init__(self,name):
        self.name=name
    
    def intro(self):
        print("Hello my name is ",{self.name})
        
    def perform_activity(self):
        print("human activity")
        
class Teacher(Human):
    def perform_activity(self):
        print("Teacher teachs")

class Student(Human):        
    def perform_activity(self):
        print("student learns")
        
obj1=Teacher("vishal")
obj2=Student("vishnu")

people=[obj1,obj2]
 
for p in people:
    p.intro()
    p.perform_activity()