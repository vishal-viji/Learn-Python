class Father():
    def __init__(self,name):
        self.name = name
        print("Father class constructor called")
        
    def provide(self):
        return f"{self.name} provides for the family"

class Mother():
    def __init__(self,name):
        self.name = name
        print("Mother class constructor called")
        
    def nurture(self):
        return f"{self.name} nurtures the family"
    
    
class Child(Father,Mother):
    def __init__(self,name):
        Father.__init__(self,name)
        Mother.__init__(self,name)
        print("Child class constructor called")
        
    def play(self):
        return f"{self.name} plays with the family"

obj1=Child("John")

print(obj1.provide())
print(obj1.nurture())
print(obj1.play())