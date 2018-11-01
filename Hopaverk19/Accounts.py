class Account():
    def __init__(self,accounts):
        self.accounts = accounts

    def print_accounts(self):
        for i in self.accounts:
            print(i.balance)

    def update_balance(self):
        return 

class SavingsAccount(Account):
    def __init__(self,balance,interst):
        self.balance = balance
        self.interest = interest
        

class DebitAccount(Account):
    def __init__(self,balance,interest):
        self.balance = balance
        self.interest = interest



# idk, mang
def main():
    s1 = SavingsAccount(1000)
    d1 = DebitAccount(1000)
    s2 = SavingsAccount(2000)
    d2 = DebitAccount(4000)

    accounts = [s1, d1, s2, d2]

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

main()