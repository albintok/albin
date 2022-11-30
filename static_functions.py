class student:
    studentcount=0
    def __init__(self):
        self.rollno=int(input("enter the roll no."))
        self.name=input("enter the name")
        student.studentcount+=1
    def displaya(self):
        super().__init__()
        print("Roll no.",self.rollno)
        print("name=",self.name)
    def displayb():
        print("total strength=",student.studentcount)
s1=student()
s1.displaya()
s2=student()
s2.displaya()
student.displayb()