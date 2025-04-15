class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def withdraw(self):
        amount = float(input("Withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("\nInsufficient balance")

    def deposit(self):
        amount = float(input("Deposit: "))
        self.balance += amount

    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Name:", self.name)
        print("Account Balance:", "$" + str(self.balance))

NewAccount = BankAccount("1234567890", "Joy", 2700)

NewAccount.withdraw()
NewAccount.deposit()
NewAccount.display()
