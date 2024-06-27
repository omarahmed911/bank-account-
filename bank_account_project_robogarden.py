import os

import random
class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = self.generate_account_number()
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        self.create_transaction_file()

    def generate_account_number(self):
        # Generate a unique account number based on some logic
        a= random.randint(10000,55550000)
        return a

    def create_transaction_file(self):
        # Create a new transaction file for the user
        with open(self.filename, 'w') as file:
            file.write(f"Transaction history for {self.name}'s {self.accountType} account:\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            with open(self.filename, 'a') as file:
                file.write(f"Deposited ${amount}\n")
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            with open(self.filename, 'a') as file:
                file.write(f"Withdrew ${amount}\n")
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNumber

    def get_name(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "No transactions yet."

# Testing the BankAccount class
if __name__ == "__main__":
    # Creating accounts and testing functionalities
    account1 = BankAccount("Omar mahmoud", "savings")
    account1.deposit(1000)
    account1.withdraw(911)
    print(f"Balance: ${account1.get_balance()}")
    print(f"Account Number: {account1.get_account_number()}")
    print(f"Account Holder: {account1.get_name()}")
    print(f"Account Type: {account1.get_account_type()}")
    print("Transaction History:")
    print(account1.get_transaction_history())
