class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0, transaction=None):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transactions = [transaction] if transaction else []
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transactions = [transaction]
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = f"Deposited ${amount} into account {self.account_number}"
            self.transactions.append(transaction)
            return True
        else:
            return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            transaction = f"Withdrew ${amount} from account {self.account_number}"
            self.transactions.append(transaction)
            return True
        else:
            return False
    
    def get_balance(self):

        return self.balance
    
    def transfer(self, recipient_account, amount):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            transaction = f"Transferred ${amount} to account {recipient_account.account_number}"
            self.transactions.append(transaction)
            recipient_account.transactions.append(f"Received ${amount} from account {self.account_number}")
            return True
        else:
            return False
            
    
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance}")
    
    def generate_statement(self):
        print(f"Account Statement for {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

# Example usage:

account1 = BankAccount("1234567890", "John Doe")
account2 = BankAccount("9876543210", "Jane Smith")

account1.deposit(1000)
account1.withdraw(500)

account1.transfer(account2, 200)

account1.display_account_info()

account1.generate_statement()

account2.display_account_info()

account2.generate_statement()
