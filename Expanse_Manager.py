#Contains BUGS,
# Needs to be Modified

class Account:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient balance in", self.name)
            return False

    def __str__(self):
        return f"Account: {self.name}, Balance: {self.balance}"


def load_accounts(filename):
    accounts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, balance = line.strip().split(',')
                accounts[name] = Account(name, float(balance))
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts, filename):
    with open(filename, 'w') as file:
        for account in accounts.values():
            file.write(f"{account.name},{account.balance}\n")

def main():
    filename = "account_balances.txt"
    accounts = load_accounts(filename)

    while True:
        print("\n1. Credit")
        print("2. Debit")
        print("3. Display Balances")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':  # Credit
            account_name = input("Enter account name (SBI/HDFC/Amazon): ").strip().lower()
            amount = float(input("Enter amount to credit: "))
            if account_name in accounts:
                accounts[account_name].credit(amount)
            else:
                print("Invalid account name")


        elif choice == '2':  # Debit
            account_name = input("Enter account name (SBI/HDFC/Amazon): ")
            amount = float(input("Enter amount to debit: "))
            if account_name in accounts:
                accounts[account_name].debit(amount)
            else:
                print("Invalid account name")

        elif choice == '3':  # Display Balances
            for account in accounts.values():
                print(account)

        elif choice == '4':  # Exit
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

    save_accounts(accounts, filename)

if __name__ == "__main__":
    main()
