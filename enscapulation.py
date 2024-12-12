# this is bundling data and methods that operate on that data withing a class

class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder # public attribute
        self.__balance = balance # private Attribute(encapsulation)

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if amount > 0:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("insufficient funds.")

    def check_balance(self):
        print(f"current balance: {self.__balance}")

account_name = input("Enter account name: ")
balance = int(input("Enter the balance: "))

account = BankAccount(account_name,balance)
print(f"Account HOlder: {account.account_holder}")

account.check_balance()

amount_to_deposit = int(input("Enter deposit amount: "))
account.deposit(amount_to_deposit)
account.check_balance()

amount_to_withdraw = int(input("Enter withdraw amount: "))
account.withdraw(amount_to_withdraw)
account.check_balance()

account.check_balance()
