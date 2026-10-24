class Account:
    def _init_(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        self.history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.history.append(f"Withdraw: {amount}")


class Bank:
    def _init_(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.acc_no] = acc

    def transfer(self, from_acc, to_acc, amount):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            raise ValueError("Account not found")

        self.accounts[from_acc].withdraw(amount)
        self.accounts[to_acc].deposit(amount)

        self.accounts[from_acc].history.append(
            f"Transfer to {to_acc}: {amount}"
        )
        self.accounts[to_acc].history.append(
            f"Transfer from {from_acc}: {amount}"
        )

    def show_accounts(self):
        for acc in self.accounts.values():
            print(acc.acc_no, "Balance:", acc.balance)


# Main program
bank = Bank()

n = int(input("Enter number of accounts: "))

for i in range(n):
    acc_no = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    bank.add_account(Account(acc_no, balance))

q = int(input("Enter number of transactions: "))

for i in range(q):
    try:
        print("\n1. Deposit  2. Withdraw  3. Transfer")
        choice = int(input("Enter choice: "))

        if choice == 1:
            acc = input("Account number: ")
            amount = float(input("Amount: "))
            bank.accounts[acc].deposit(amount)

        elif choice == 2:
            acc = input("Account number: ")
            amount = float(input("Amount: "))
            bank.accounts[acc].withdraw(amount)

        elif choice == 3:
            sender = input("From account: ")
            receiver = input("To account: ")
            amount = float(input("Amount: "))
            bank.transfer(sender, receiver, amount)

        else:
            print("Invalid choice")

    except Exception as e:
        print("Transaction failed:", e)

print("\nFinal Account Details:")
bank.show_accounts()