class vechicle:
    def getdata(self,n,a):
        self.name=n
        self.fuel_capacity=a
    def display(self):
        print("name is:",self.name)
        print("fuel capacity",self.fuel_capacity)
car=vechicle()
bike=vechicle()
car.getdata("auto",5)
bike.getdata("fz",6)
car.display()
bike.display()