from ast import While


class Calculator:
    def display(self):  #self is a refrence variable which hold the object ref of current object of the current class
        print("hello display..........")
    def setA(self, a):
        self.a = a
        print("a=", self.a)
    def setB(self, b):
        self.b = b
        print("a=", self.b)
    def add(self):
        c = self.a + self.b
        print("add=", c)
    def sub(self):
        c = self.a - self.b
        print("sub=", c)
    def mul(self):
        c = self.a * self.b
        print("mul=", c)
    def div(self):
        c = self.a / self.b
        print("div=", c)
    def mod(self):
        c = self.a % self.b
        print("mod=", c)
    def floor(self):
        c = self.a // self.b
        print("floor=", c)
    def power(self):
        c = self.a ** self.b
        print("power=", c)

ob = Calculator()

while True:
    print("1.add 2.sub 3.mul 4.div 5.mod 6.floor 7.power 8.exit")
    ch = int(input("enter your choice:"))
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    ob.setA(a)
    ob.setB(b)
    if ch == 1:
        ob.add()
    elif ch == 2:
        ob.sub()
    elif ch == 3:
        ob.mul()
    elif ch == 4:
        ob.div()
    elif ch == 5:
        ob.mod()
    elif ch == 6:
        ob.floor()
    elif ch == 7:
        ob.power()
    elif ch == 8:
        print("exit")
        break
    else:
        print("invalid choice")