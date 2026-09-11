n=int(input("Enter the number to find the factorial:") )
def factorial(n):
    if n==1 or n==0:
        return 1
    print(n)
    return n*factorial(n-1)
result=factorial(n)
print(f"factorial of {n} is {result}")