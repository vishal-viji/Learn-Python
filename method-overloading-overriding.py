"""# Overloading method

class Calculator:
    # def add (self,a,b):
    #     return a+b
    
    # def add (self,a,b,c):
    #     return a+b+c
    
    # def add (self,a,b,c,d):
    #     return a+b+c+d
    
    def add(self,*args):
        res=0
        for n in args:
            res+=n
        return res
        
        
obj=Calculator()
print(obj.add(3,3,3,3))
print(obj.add(3,3,3,343,34,234,3,4,34,))"""

# overriding
"""
class animal:
    def  speak(self):
        print("animal doesnt speak")

class dog(animal):
    def speak (self):
        print("dogs bark")
        
class cat(animal):
    def speak(self):
        print("cat meows")
        
obj=cat()
obj.speak()"""