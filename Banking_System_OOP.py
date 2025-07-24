import random

accounts = {}

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"\n{self.name}, your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

def welcome():
    banks = ["CBI", "NBE", "QNB", "AIAHLY Bank", "EG BANK"]
    bank_name = random.choice(banks)
    print(f"\n🏦 Welcome to {bank_name} 🏦\n")

def show_menu():
    print("""
Main Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")

def get_amount(action):
    try:
        amount = float(input(f"Enter amount to {action}: "))
        if amount < 0:
            print("Amount cannot be negative.")
            return None
        return amount
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def banking_system():
    welcome()
    name = input("Enter your name: ")

    if name in accounts:
        account = accounts[name]
        print(f"Welcome back, {name}!")
    else:
        while True:
            try:
                balance = float(input("Enter initial balance: "))
                break
            except ValueError:
                print("Invalid number. Try again.")
        account = BankAccount(name, balance)
        accounts[name] = account

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = get_amount("deposit")
            if amount is not None:
                account.deposit(amount)
        elif choice == "3":
            amount = get_amount("withdraw")
            if amount is not None:
                account.withdraw(amount)
        elif choice == "4":
            print(f"\nThank you, {account.name}, for using our banking system. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    banking_system()
