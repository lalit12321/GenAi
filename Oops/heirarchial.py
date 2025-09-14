class Test:
    def __init__(self, x=0):
        self.x = x
    def display(self):
        print("x= ",self.x)
class Test1(Test):
    def __init__(self, x =0,y=0):
        super().__init__(x)
        super().display()
        self.y = y
    def display(self):
        print("y= ",self.y)
class Test2(Test):
    def __init__(self, x=0,z=0):
        super().__init__(x)
        super().display()
        self.z = z
    def display(self):
        print("z= ",self.z)
t1 = Test1(12,20)
t2 = Test2(15,25)
t1.display()
t2.display()