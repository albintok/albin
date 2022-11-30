class student:
    def data(self,n,a,r):
        self.name=n
        self.age=a
        self.roll_no=r
    def dis(self):
        print("name:",self.name)
        print("age:",self.age)
        print("roll.no:",self.roll_no)
s1=student()
s2=student()
s3=student()
s1.data("alb",22,4)
s2.data("sij",44,3)
s3.data("ponnu",33,9)
s1.dis()
s2.dis()
s3.dis()