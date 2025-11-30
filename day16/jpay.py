class Bank:
    def __init__(self, name, balance:float=0.00):
        self.name = name
        self.balance = balance
        
    # withrawal method
    def withdraw(self, amount):
        # check if the amount entered is less than the balance == withdrawal successful
        if amount < self.balance:
            self.balance -= amount
            print("Withdrawal successful...")
        else:
            print("Withdrawal unsuccessful...\nInsufficient funds")
            
    # deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} successfully deposited...")
    
    # transfer method
    def transfer(self, amount, acct_num):
        if amount < self.balance:
            self.balance -= amount
            print(f"Transfer successful...\nSender {self.name}\nReceipient: {acct_num}")
        else:
            print("Transfer Unsuccessful...")
    
    # check balance method
    def check_balance(self):
        print(f"Your account balance is ₦{self.balance}")
        