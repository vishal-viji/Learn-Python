class Grandfather:
    def grands(self):
        print("I am the grandfather.")

class Father(Grandfather):
    def father(self):
        print("I am the father.")
        
class Son(Father):
    def son(self):
        print("I am the son.")
        
s1=Son()
s1.son()
s1.father()
s1.grands()
        
f1=Father()
f1.father()