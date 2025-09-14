from abc import abstractmethod,ABC
class Test(ABC):
    def __init__(self, x=0):
        self.x = x
    @abstractmethod
    def display(self):
        pass
class Test1(Test):
    def __init__(self, x=0, y=0):
        super().__init__(x)
        self.y = y
    def display(self):
        print("x= ", self.x, end=" ")
        print("y= ", self.y )
class Test2(Test):
    def __init__(self, x =0, z =0):
        super().__init__(x)
        self.z = z
    def display(self):
        print("x= ",self.x, end=" ")
        print("y= ", self.z)
ob= Test1(12,20)
ob.display()
ob1= Test2(15,25)
ob1.display()