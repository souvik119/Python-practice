class Account():

    def __init__(self, name, balance):
        self.owner= name
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        return f'Deposit accepted. Current balanace is ${self.balance}'

    def withdraw(self, money):
        if money > self.balance:
            return 'Funds unavailable'
        else:
            self.balance -= money
            return f'Withdrawal accepted. Current balanace is ${self.balance}'

    def __str__(self):
        return f'Account owner : {self.owner}\nAccount balance : ${self.balance}'


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))