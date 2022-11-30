# -------multilevel inheritance normal------------
#
# class a:
#     def geta(self):
#         self.a=int(input("enter a"))
#     def disa(self):
#         print("a=",self.a)
# class b:
#     def getb(self):
#         self.b=int(input("enter b"))
#     def disb(self):
#         print("b=",self.b)
# class c(a,b):
#     def getc(self):
#         self.c=int(input("enter c"))
#     def disc(self):
#         print("c=",self.c)
# c1=c()
# c1.geta()
# c1.getb()
# c1.getc()
# c1.disa()
# c1.disb()
# c1.disc()

#-------multilevel inheritance using __init___------------

class a:
    def __init__(self):
        self.a=int(input("enter a"))
    def disa(self):
        print("a=",self.a)
class b:
    def __init__(self):
        a.__init__(self)
        self.b=int(input("enter b"))
    def disb(self):
        print("b=",self.b)
class c(a,b):
    def __init__(self):
        b.__init__(self)
        self.c=int(input("enter c"))
    def disc(self):
        a.disa(self)
        b.disb(self)
        print("c=",self.c)
c1=c()
c1.disc()