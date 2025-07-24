import random

accounts = {}

def welcome():
    banks = ["CBI", "NBE", "QNB", "AIAHLY Bank", "EG BANK"]
    bank_name = random.choice(banks)
    print(f"\nWelcome to {bank_name}\n")

def create_account():
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists.")
        return name
    while True:
        try:
            balance = float(input("Enter initial balance: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    accounts[name] = balance
    print(f"\nAccount created successfully for {name} with balance ${balance:.2f}\n")
    return name

def check_balance(name):
    balance = accounts.get(name)
    if balance is not None:
        print(f"\n{name}, your current balance is: ${balance:.2f}")
    else:
        print("Account not found.")

def deposit(name):
    if name not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to deposit: "))
        accounts[name] += amount
        print(f"Deposited ${amount:.2f}. New balance: ${accounts[name]:.2f}")
    except ValueError:
        print("Invalid amount.")

def withdraw(name):
    if name not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[name]:
            accounts[name] -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${accounts[name]:.2f}")
        else:
            print("Insufficient funds.")
    except ValueError:
        print("Invalid amount.")

def show_menu():
    print("""
Main Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
""")

def banking_system():
    welcome()
    name = create_account()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(name)
        elif choice == "2":
            deposit(name)
        elif choice == "3":
            withdraw(name)
        elif choice == "4":
            print(f"\nThank you, {name}, for using our banking system. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    banking_system()
