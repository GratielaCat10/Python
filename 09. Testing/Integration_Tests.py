"""Write unit tests for a BankAccount class that:
  - creates a test account
  - tests deposit functionality
  - tests withdraw functionality
  - tests interest application
  - verifies the final account balance using assert. """

class BankAccount:

    # This function runs automatically when an object is created
    # It initializes the class attributes
    def __init__(self, owner, initial_balance=0):
        # self is required in class methods
        # initial_balance is set to 0 by default
        self.owner = owner
        self.balance = initial_balance

    # This function allows depositing money into the account
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount

    # This function allows withdrawing money from the account
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    # This function applies interest to the current balance
    def apply_interest(self, percent):
        if percent < 0:
            raise ValueError("Invalid percentage")

        self.balance = self.balance + self.balance * percent / 100



#Testing the function

  from tested_file import BankAccount

# Function that tests all class methods step by step
def test_complete_operations_flow():

    # Create a test bank account
    account = BankAccount("Ana", 100)

    # Deposit 50 -> balance becomes 150
    account.deposit(50)

    # Withdraw 30 -> balance becomes 120
    account.withdraw(30)

    # Apply 10% interest -> balance becomes 132
    account.apply_interest(10)

    # Verify the final balance
    assert account.balance == 132
