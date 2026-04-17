class BankAccount_smg:
    def __init__(self_smg, account_name_smg, balance_smg):
        self_smg.account_name_smg = account_name_smg
        self_smg.balance_smg = balance_smg
    
    def deposit_smg(self_smg, amount_smg):
        self_smg.balance_smg += amount_smg
        print("Deposit successful")
    
    def withdraw_smg(self_smg, amount_smg):
        if amount_smg <= self_smg.balance_smg:
            self_smg.balance_smg -= amount_smg
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    
    def display_balance_smg(self_smg):
        print("Balance:", self_smg.balance_smg)

account_smg = BankAccount_smg("Juan", 5000)
account_smg.deposit_smg(1000)
account_smg.withdraw_smg(2000)
account_smg.display_balance_smg()
