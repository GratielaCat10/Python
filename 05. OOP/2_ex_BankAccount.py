""" Write a Python program that implements a Bank system using OOP.
The program should:
  - Define a BankAccount class with owner and balance
  - Define a SavingsAccount class that inherits from BankAccount and adds interest functionality
  - Define a Bank class that manages multiple accounts (has-a relationship)
Allow:
  - adding accounts
  - depositing money
  - withdrawing money
  - adding interest (only for savings accounts)
  - displaying all accounts
  - calculating total money in the bank
Use a menu-driven interface
Handle invalid input using try/except.  """

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Invalid amount")
        else:
            self.balance -= amount
            print("Withdrawal successful!")

    def __str__(self):
        return f"Owner: {self.owner} | Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, initial_balance=0, interest_rate=0):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest added successfully!")

    def __str__(self):
        return f"Owner: {self.owner} | Balance: {self.balance} | Interest: {self.interest_rate}"


class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, owner):
        for account in self.accounts:
            if account.owner == owner:
                return account
        return None

    def add_account(self, account):
        if self.find_account(account.owner):
            print("Account already exists!")
        else:
            self.accounts.append(account)
            print("Account added successfully!")

    def delete_account(self, account):
        if account is None:
            print("Account not found!")
        else:
            self.accounts.remove(account)
            print("Account removed successfully!")

    def show_all(self):
        if not self.accounts:
            print("No accounts found!")
            return

        print("\nAccounts list:")
        for account in self.accounts:
            print(account)

    def total_money(self):
        total = []
        for account in self.accounts:
            total.append(account.balance)
        return sum(total)


def main():
    bank = Bank()

    while True:
        try:
            print("\nBANK MENU")
            print("\n1. Add bank account")
            print("2. Add savings account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Add interest (savings only)")
            print("6. Show accounts")
            print("7. Show total money in bank")
            print("8. Exit")

            option = int(input("\nChoose an option: "))

            if option == 1:
                owner = input("Owner: ")
                balance = int(input("Balance: "))
                account = BankAccount(owner, balance)
                bank.add_account(account)

            if option == 2:
                owner = input("Owner: ")
                balance = int(input("Balance: "))
                interest = int(input("Interest rate: "))
                account = SavingsAccount(owner, balance, interest)
                bank.add_account(account)

            if option == 3:
                owner = input("Owner: ")
                amount = int(input("Deposit amount: "))
                account = bank.find_account(owner)

                if account is None:
                    print("Account not found!")
                else:
                    account.deposit(amount)

            if option == 4:
                owner = input("Owner: ")
                amount = int(input("Withdraw amount: "))
                account = bank.find_account(owner)

                if account is None:
                    print("Account not found!")
                else:
                    account.withdraw(amount)

            if option == 5:
                owner = input("Owner: ")
                account = bank.find_account(owner)

                if account is None:
                    print("Account not found!")
                elif isinstance(account, SavingsAccount):
                    account.add_interest()
                else:
                    print("This is not a savings account")

            if option == 6:
                bank.show_all()

            if option == 7:
                print(f"Total money in bank: {bank.total_money()}")

            if option == 8:
                print("Exit")
                break

        except ValueError:
            print("Invalid input!")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
  
