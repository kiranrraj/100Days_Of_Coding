# Author    : Kiran raj R.
# Date      : 21/08/2025
# Topic     : OOP -- Class


# Class attributes live on the class and are shared by all instances. 
# Instance attributes live on self.
class BankAccount:
    bank_name = "SBI"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

a = BankAccount("Kiran", 1000)
b = BankAccount("Raj", 500)
print(a.bank_name, b.bank_name) # SBI SBI

BankAccount.bank_name = "State Bank Of India"
print(a.bank_name) # State Bank Of India
print(b.bank_name) # State Bank Of India