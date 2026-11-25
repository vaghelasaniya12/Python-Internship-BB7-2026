
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Invalid amount or insufficient balance")

    @property
    def balance(self):
        return self.__balance


# Creating object
w1 = Wallet(5000)

w1.deposit(1000)
w1.withdraw(2000)

print("Current Balance:", w1.balance)
