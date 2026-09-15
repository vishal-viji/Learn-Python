from abc import ABC,abstractmethod

#abstract method
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        print("i want to find the area of perimeter")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
obj=Circle(5)
# print(obj.radius())
print(obj.area())
print(obj.perimeter())
        

