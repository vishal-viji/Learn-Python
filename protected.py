# 


class BankAccount:

        def __init__(self,accountNumber,balance):
            self._accountNumber=accountNumber #protectedd   
            self.__balance=balance # private
            
        def getbalance(self):
            return self.__balance
        
        def setBalance(self,newbalance):
            if(newbalance>=0):
                self.__balance=newbalance
                
                
        def deposit(self,amount):
            if amount>0:
                self.__balance+=amount
                
        def withdraw(self,amount):
            if 0<amount<=self.__balance:
                self.__balance-=amount
                
            else:
                print("insufficient balance.......")
                
account=BankAccount(73463646384737,50000)
print(account.getbalance())
account.deposit(5000)
print(account.getbalance())
account.withdraw(10000)
print(account.getbalance())

print(account._accountNumber)
print(account._BankAccount__balance)
                
        