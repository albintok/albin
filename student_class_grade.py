class student:
    def __init__(self):
        self.name=input("enter the name")
        self.roll=int(input("enter the roll no."))
    def display(self):
        print("name:",self.name)
        print("roll no.",self.roll)
class mark(student):
    def __init__(self):
        super().__init__()
        self.mark1=int(input("enter the mark1"))
        self.mark2=int(input("enter the mark2"))
        self.mark3=int(input("enter the mark3"))
    def displaym(self):
        print("mark1:",self.mark1)
        print("mark2:", self.mark2)
        print("mark3:", self.mark3)
class grade(mark):
    def __init__(self):
        super().__init__()
    def cal(self):
        g=((self.mark1+self.mark2+self.mark3)/300)*100
        if(g>80):
            print("a")
        elif(g>60):
            print("b")
        elif(g>50):
            print("pass")
        else:
            print("failed")
c1=grade()
c1.cal()