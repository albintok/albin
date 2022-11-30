class account:
    def __init__(self):
        self.balance=0
    def deposit(self):
        a=int(input("enter the amount to deposit"))
        self.balance=self.balance+a
        print("your credited balance is",self.balance)
    def withdraw(self):
        b=int(input("enter the amount to withdraw"))
        if(self.balance>b):
            self.balance=self.balance-b
            print("your debited balance is:",self.balance)
        else:
            print("no sufficent balance")
    def enquiry(self):
        print("your current balance is",self.balance)
a1=account()
a1.deposit()
a1.withdraw()
a1.enquiry()