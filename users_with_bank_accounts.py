class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 1.02, balance = 0)
    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.account.balance} Interest Rate: {self.account.int_rate}")
        return self


class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance <= 0:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance} Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self

account1 = User("Johnny", "johnny@appleseed.com")
account1.make_deposit(100).make_withdrawal(50).display_account_info()

account1.account.yield_interest()
account1.display_account_info()