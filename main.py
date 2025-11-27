class BankAccount:
    def __init__(self, Satyam, balance=0.0):
        self.account_holder = Satyam
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposited amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal!")
        else:
            self.balance -= amount
            print(f"Withdraw successful of amount {amount}. New balance is {self.balance}")

    def display_balance(self):
        print(f"{self.account_holder}'s balance is {self.balance}")

# Loop for multiple transactions
account = BankAccount(input("Enter account holder name: "))
while True:
    print("Choose a transaction:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Log out")
    choice = input("Select action 1/2/3/4: ")

    if choice == "1":
        amount = float(input("Enter amount you want to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the amount you want to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Logging out..")
        break
    else:
        print("Invalid choice, Please enter correct one ")