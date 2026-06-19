"""Question 4: Bank Account
Create a class called BankAccount.
Attributes:
account_holder
balance
Methods:
deposit()
withdraw()
check_balance()"""
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposite(self):
        dip_amount=int(input("enter ur dip amount:"))
        amount=dip_amount+self.balance
        print(self.account_holder,"amount deposited",amount)
    def withdraw(self):
        draw_amount=int(input('enter ur drae amount:'))
        amount=self.balance-draw_amount
        print(amount)
    def check_balance(self):
        print(self.balance)
m1=BankAccount("Ajibun",10000000)
m2=BankAccount("dhana",100)
m1.deposite()
m1.withdraw()
m1.check_balance()