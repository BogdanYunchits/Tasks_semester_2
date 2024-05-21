class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount * 0.99

    def withdraw(self, amount):
        if amount * 1.01 <= self.balance:
            self.balance -= amount * 1.01
            return amount
        else:
            print("Insufficient funds.")
            return 0

    def get_balance(self):
        return self.balance

account = BankAccount("1234567", "Bogdan Yunchits", 1000)
account.deposit(500)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())
