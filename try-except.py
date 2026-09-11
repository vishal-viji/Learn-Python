num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number :"))
try:
    print(num1/num2)
except:
    print("Error occurred")
    

num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number :"))
try:
    print(num1/num2)
except Exception as e:
    print("Error occurred",e)