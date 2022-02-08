# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, a):
        self.balance = self.balance + a
        return self.balance

    def withdraw(self, b):
        self.balance = self.balance - b
        return self.balance


acct = BankAccount("Darcy")
acct.owner
acct.balance
acct.deposit(10)
acct.withdraw(3)
acct.balance
