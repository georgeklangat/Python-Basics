class Employee:
    id=38197188
    name="George"
    def display(self):
        print("id:%d\nname:%s"%(self.id,self.name))
emp=Employee()
emp.display()

print(emp.id)
emp.display()


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")





# Create two bank account instances
account1 = BankAccount("123456789", "John Doe", 1000)
account2 = BankAccount("987654321", "Jane Smith", 500)

# Deposit money into the accounts
account1.deposit(500)
account2.deposit(1000)

# Withdraw money from the accounts
account1.withdraw(200)
account2.withdraw(800)

# Display the account balances
account1.display_balance()
account2.display_balance()
