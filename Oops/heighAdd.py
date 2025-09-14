#add height of to volume in inch and feet
class Height:
    def __init__(self, feet=0, inch=0):
        self.feet = feet
        self.inch = inch
    def heAdd(self, o1,o2):
        self.foot = o1.feet + o2.feet
        self.inch = o1.inch + o2.inch

        if self.inch >= 12:
            self.foot += self.inch // 12
            self.inch = self.inch % 12
        return self.foot,self.inch
h1 = Height(5, 9)
h2 = Height(6, 8)
h3 = Height(0, 0)
h3.heAdd(h1,h2)
print(h3.heAdd(h1,h2))
