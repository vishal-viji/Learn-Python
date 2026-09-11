class Human:
    human_name="anonymous"
    age=0
    category=["male","female"]
    
    #method
    def humandetails(self):
        print(f"human name is {self.human_name} age is {self.age} and category is {self.category}")
    
    def greet(self):
        print("good evening...")


# objects
        
obj1=Human()
obj1.humandetails()
obj1.greet()

obj2=Human()
obj2.human_name="Vishal"
obj2.age=20
obj2.category=obj2.category[0]
obj2.humandetails()
obj2.greet()


obj3=Human()
obj3.human_name="Suba"
obj3.age=18
obj3.category=obj3.category[1]
obj3.humandetails()
obj3.greet()