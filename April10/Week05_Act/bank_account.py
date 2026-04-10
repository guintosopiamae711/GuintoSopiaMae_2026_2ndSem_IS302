class BankAccount_nbs:
    def __init__(self_nbs, account_name_nbs, balance_nbs):
        self_nbs.account_name_nbs = account_name_nbs
        self_nbs.balance_nbs = balance_nbs
    
    def deposit_nbs(self_nbs, amount_nbs):
        self_nbs.balance_nbs += amount_nbs
        print("Deposit successful")
    
    def withdraw_nbs(self_nbs, amount_nbs):
        if amount_nbs <= self_nbs.balance_nbs:
            self_nbs.balance_nbs -= amount_nbs
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_nbs(self_nbs):
        print("Balance:", self_nbs.balance_nbs)

account_nbs = BankAccount_nbs("Juan", 5000)
account_nbs.deposit_nbs(1000)
account_nbs.withdraw_nbs(2000)
account_nbs.display_balance_nbs()
