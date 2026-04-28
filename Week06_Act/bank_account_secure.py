# bank_account_secure.py

class BankAccount:
    def __init__(self, balance_smg):
        self.__balance_smg = balance_smg   # private attribute

    # method to deposit money
    def deposit_smg(self, amount_smg):
        self.__balance_smg += amount_smg

    # method to withdraw money
    def withdraw_smg(self, amount_smg):
        if amount_smg <= self.__balance_smg:
            self.__balance_smg -= amount_smg
        else:
            print("Insufficient funds")

    # method to check balance
    def get_balance_smg(self):
        return self.__balance_smg


# create an account
account_smg = BankAccount(5000)

# perform transactions
account_smg.deposit_smg(1000)
account_smg.withdraw_smg(2000)

# display balance
print("Balance:", account_smg.get_balance_smg())