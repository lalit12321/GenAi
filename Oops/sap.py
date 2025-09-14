class Saping:
    def setData(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("a=",self.a)
        print("b=",self.b)
    def sap(self):
        self.a,self.b = self.b,self.a
ob = Saping()
ob.setData(10,20)
print("before saping")  
ob.display()
ob.sap()
print("after saping")
ob.display()