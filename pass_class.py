class person:
    def getperson(self):
        self.name=input("enter the name")
        self.code=int(input("enter the code"))
    def displaya(self):
        print("name=",self.name)
        print("code=",self,code)
class account(person):
    def getaccount(self):
        self.payment=int(input("enter the payment"))
    def displayb(self):
        print("payment=",self.payment)
class admin(person):
    def getadmin(self):
        self.experienve=int(input("enter your experience"))
    def displayc(self):
        print('experience=',self.experienve)
class employ(account,admin):
    pass