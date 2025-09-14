class Square:
    def __init__(self, s=0):
        self.s = s
    def sq(self):
        return self.s*self.s
class Area:
    def __init__(self, l=0, b=0):
        self.l = l
        self.b = b
    def a(self):
        return self.l*self.b
class Volume(Area, Square):
    def __init__(self, l=0, b=0, h=0):
        Area.__init__(self,l,b)
        Square.__init__(self,l)
        self.h = h
    def v(self):
        return self.a()*self.h
'''class Density(Volume):
    def __init__(self, l=0, b=0, h=0, w=0):
        super().__init__(l,b,h)
        self.w = w
    def d(self):
        return self.w/self.v()'''
height = int(input("Enter height")) 
breadth = int(input("Enter breadth"))
length = int(input("Enter length"))
#weight = int(input("Enter weight"))
#ob = Density(length,breadth,height,weight)
ob = Volume(length,breadth,height)

print("Area of Square",ob.sq())
print("Area",ob.a())
print("Volume",ob.v())
#print("Density",ob.d())
  
