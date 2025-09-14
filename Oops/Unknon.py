class Saping:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def setData(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("a=",self.a)
        print("b=",self.b)
    def sap(self):
        self.a,self.b = self.b,self.a
    def __str__(self):
        return "Na={} b={}".format(self.a,self.b)
        #return "hello student"
ob = Saping(10,20)
print(ob)
# print("before saping")  
# ob.display()
# ob.sap()
# print("after saping")
# ob.display()