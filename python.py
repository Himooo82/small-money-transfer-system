class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance: ", self.balance)

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Debit successful. New balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Credit successful. New balance: ", self.balance)

    def get_balance(self):
        return self.balance
    
    # function to transfer money between accounts
    
    def transfer(self, receiver, amount):
        if amount > self.balance:
            print("Insufficient balance in sender's account")
        else:
            self.balance -= amount
        receiver.balance += amount
        print("Transfer successful. Sender's new balance: ", self.balance)


# create accounts 
account1 = account(10000, "123456")
account2 = account(5000, "654321")
account3 = account(2000, "111111")
accounts = {
    account1.account_number: account1,
    account2.account_number: account2,
    account3.account_number: account3
}

# user enter account number and amount to transfer

receiver_acc = input("Enter receiver's account number: ")
amount = int(input("Enter amount to transfer: "))

if receiver_acc == account1.account_number:
    print("You cannot transfer money to your own account") 

elif receiver_acc in accounts:
     account1.transfer(accounts[receiver_acc], amount)

else:
    print("Receiver account number not found")

print("Sender's balance: ", account1.get_balance())
