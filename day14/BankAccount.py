class BankAccount:
    def __init__(self):
        self.__balance=100000
    def deposit(self,amount):
        self.__balance+=amount
        print(self.__balance)
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount 
            print("withdraw Successful")
        else:
            print("Insufficent Balance")
    def get_balance(self):
        print(self.__balance) 

b=BankAccount()
b.deposit(100)
b.withdraw(1100)
b.get_balance()


    