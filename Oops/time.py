
class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def display(self):
        print("time is {}:{}:{}".format(self.h, self.m, self.s))

    def add(self, o1,o2):
        self.h =  o1.h + o2.h
        self.m =  o1.m + o2.m
        self.s =  o1.s + o2.s

        if self.s >= 60:
            self.m += self.s // 60
            self.s = self.s % 60
        if self.m >= 60:
            self.h += self.m // 60
            self.m = self.m % 60

        return Time(self.h,self.m,self.s)
    
t1 = Time(10, 50, 30)
t2 = Time(5, 20, 40)
t3 = Time(0, 0, 0)
t3.add(t2,t1)
t3.display()
