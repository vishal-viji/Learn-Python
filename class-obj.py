class Human:
    human_name="anonymous"
    age=0
    category=["male","female"]
    
    #method
    def humandetails(self):
        print(f"human name is {self.human_name} age is {self.age} and category is {self.category}")
    
    def greet(self):
        print("good evening...")
        
obj1=Human()
obj1.humandetails()
obj1.greet()

obj2=Human()
obj2.human_name="Vishal"
obj2.age=20
obj2.category=obj2.category[0]
obj2.humandetails()
obj2.greet()