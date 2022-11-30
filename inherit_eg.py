class parent:
    def displayp(self):
        print("im parent")
class child(parent):
        def display(self):
            print("im child")
c1=child()
c1.displayp()
c1.display()