from math import *
class sphere:
    def __init__(self):
        self.radius=int(input("enter the radius"))
        print("radius:",self.radius)
    def volume(self):
        v=(4/3)*pi*(self.radius**3)
        return v
r1=sphere()
print('volume of sphere is:',r1.volume)
