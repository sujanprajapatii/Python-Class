#Encapsulation:
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #Private Attribute
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
    
account=BankAccount(100)
account.deposit(50)
print(account.get_balance()) #Output:150