# payment_system.py

# Parent Class
class Payment:
    def pay_smg(self):
        print("Processing payment")

# Child Class 1: CashPayment
class CashPayment(Payment):
    def pay_smg(self):
        print("Payment made using cash")

# Child Class 2: CardPayment
class CardPayment(Payment):
    def pay_smg(self):
        print("Payment made using credit card")

# Instantiate objects for each payment method
payments_smg = [CashPayment(), CardPayment()]

# Call the pay method for each payment
for p_smg in payments_smg:
    p_smg.pay_smg()