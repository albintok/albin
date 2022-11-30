class student:
    def __init__(self):
        self.name=input("enter the name ")
        self.roll=int(input("enter the roll.no"))
        self.course=input("enter the course")
    def disa(self):
        print("Name=",self.name)
        print("roll=",self.roll)
        print("course=",self.course)
class test(student):
    def __init__(self):
        self.mark1=int(input("enter the mark"))
    def disb(self):
        print("mark in test=",self.mark1)
class sports:
    def __init__(self):
        self.sports=int(input("enter the sports marks"))
    def disc(self):
        print("mark in sports=",self.sports)
class result(test,sports):
    sum=self.mark1+self.sports
    print("total mark is=",sum)
    def grade(self):
        if(sum>=480):
            print("distinction")
        elif(sum>=360):
            print("first class")
        elif(sum>=250):
            print("second class")
        else:
            print("failed")
c1=result()
c1.grade()