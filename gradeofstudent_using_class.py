class student:
    def data(self,x,y,z):
        self.mark1=x
        self.mark2=y
        self.mark3=z
    def total(self):
        print("total mark",self.mark1+self.mark2+self.mark3)
s1=student()
s1.data(22,3,44)
s1.total()