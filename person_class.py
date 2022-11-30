
#--------normal inheritance-----

# class person:
#     def data(self):
#         self.name=input("enter the name")
#         self.voter_id=int(input("enter the voter id"))
#     def display(self):
#         print("name:",self.name)
#         print("voter id:",self.voter_id)
# class employ(person):
#     def get(self):
#         self.salary=int(input("enter the salary"))
#         self.desgn=input("enter the designation")
#     def displayp(self):
#         print("salary:",self.salary)
#         print("designation:",self.desgn)
# c1=employ()
# c1.data()
# c1.get()
# c1.display()
# c1.displayp()
#

#-------------------inheritance using super()-------------
class person:
    def __init__(self,x,y):
        self.name=x
        self.voter_id=y
    def display(self):
        print("name:",self.name)
        print("voter id:",self.voter_id)
class employ(person):
    def __init__(self,x,y,a,b):
        super().__init__(x,y)
        self.salary=a
        self.desgn=b
    def display(self):
        super().__init__()
        print("salary:",self.salary)
        print("designation:",self.desgn)
c1=employ("albin",2,4,"itgii")
c1.display()