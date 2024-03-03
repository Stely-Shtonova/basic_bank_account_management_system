class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.balance += amount
        return f'{amount}$ added to your bank account!'

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if self.balance - amount >= 0:
            self.balance -= amount
            return f'{amount}$ withdrawn from your bank account!'
        else:
            return 'Not enough money to do this operation!'

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        return f"Account number: {self.account_number} with current balance: {self.balance}$"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        self.interest_rate = interest_rate
        super().__init__(account_number, balance)

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest

# Testing the functionality of the classes
if __name__ == "__main__":
    bank_account = BankAccount("123456789", 1000)
    print(bank_account.deposit(500))
    print(bank_account.withdraw(200))
    print(bank_account.get_balance())
    savings_account = SavingsAccount("987654321", 2000, 5)
    print(savings_account.deposit(1000))
    savings_account.calculate_interest()
    print(savings_account.get_balance())
