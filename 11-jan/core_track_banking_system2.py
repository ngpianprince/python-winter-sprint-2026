# Base Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDepositing {amount}...")
        print("Deposit successful.")

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")


# Child Class
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print(f"\nWithdrawing {amount}...")
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance. Withdrawal failed.")


# -------- Run the Program --------
name = input("Enter account holder name: ")
initial_balance = int(input("Enter initial balance: "))

account = SavingsAccount(name, initial_balance)

deposit_amount = int(input("Enter deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("Enter withdraw amount: "))
account.withdraw(withdraw_amount)

account.show_balance()
